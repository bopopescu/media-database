# Copyright 2014 Google Inc. All Rights Reserved.

"""The 'gcloud test run' command."""

import types

from googlecloudsdk.calliope import base
from googlecloudsdk.core import log
from googlecloudsdk.core.util import list_printer
from googlecloudsdk.test.lib import arg_util
from googlecloudsdk.test.lib import ctrl_c_handler
from googlecloudsdk.test.lib import exit_code
from googlecloudsdk.test.lib import history_picker
from googlecloudsdk.test.lib import results_bucket
from googlecloudsdk.test.lib import results_summary
from googlecloudsdk.test.lib import testing_api
from googlecloudsdk.test.lib import tool_results
from googlecloudsdk.test.lib import util


class Run(base.Command):
  """Encapsulation of the 'gcloud test run' command.

  Invoke a test in the Google Cloud Test Lab and monitor results.
  """

  @staticmethod
  def Args(parser):
    """Method called by Calliope to register flags for this command.

    Args:
      parser: An argparse parser used to add arguments that follow this
          command in the CLI. Positional arguments are allowed.
    """
    arg_util.AddCommonTestRunArgs(parser)
    arg_util.AddSharedCommandArgs(parser)
    arg_util.AddMatrixArgs(parser)
    arg_util.AddInstrumentationTestArgs(parser)
    arg_util.AddMonkeyTestArgs(parser)
    arg_util.AddRoboTestArgs(parser)

  def Run(self, args):
    """Run the 'gcloud test run' command to invoke a test in the Cloud Test Lab.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation (i.e. group and command arguments combined).

    Returns:
      One of:
        - a list of TestOutcome tuples (if ToolResults are available).
        - a URL string pointing to the user's results in ToolResults or GCS.
    """
    arg_util.Prepare(args, self.context['android_catalog'])

    project = util.GetProject()
    test_client = self.context['testing_client']
    test_messages = self.context['testing_messages']
    tr_client = self.context['toolresults_client']
    tr_messages = self.context['toolresults_messages']

    bucket_ops = results_bucket.ResultsBucketOps(project, args.results_bucket,
                                                 tr_client, tr_messages)
    bucket_ops.UploadApkFileToGcs(args.app)
    if args.test:
      bucket_ops.UploadApkFileToGcs(args.test)
    bucket_ops.LogGcsResultsUrl()

    tr_history_picker = history_picker.ToolResultsHistoryPicker(
        project, tr_client, tr_messages)
    history_id = tr_history_picker.FindToolResultsHistoryId(args)
    helper = testing_api.TestingApiHelper(project, args, history_id,
                                          bucket_ops.gcs_results_root,
                                          test_client, test_messages)
    matrix = helper.CreateTestMatrix()

    with ctrl_c_handler.CancellableTestSection(matrix.testMatrixId, helper):
      # TODO(user): call resources.Create(matrix.id, ...) here
      supported_executions = helper.HandleUnsupportedExecutions(matrix)
      tr_ids = tool_results.GetToolResultsIds(matrix, helper)
      url = tool_results.CreateToolResultsUiUrl(project, tr_ids)
      log.status.Print('Test results will be streamed to [{0}].'.format(url))
      if args.async:
        return url

      # If we have exactly one testExecution, show detailed progress info.
      if len(supported_executions) == 1:
        helper.MonitorTestExecutionProgress(matrix.testMatrixId,
                                            supported_executions[0].id)
      else:
        helper.MonitorTestMatrixProgress(matrix.testMatrixId)

    log.status.Print('\nMore details are available at [{0}].\n'.format(url))
    # Fetch the per-dimension test outcomes list, and also the "rolled-up"
    # matrix outcome from the Tool Results service.
    summary_fetcher = results_summary.ToolResultsSummaryFetcher(
        project, tr_client, tr_messages, tr_ids)
    self.exit_code = exit_code.ExitCodeFromRollupOutcome(
        summary_fetcher.FetchMatrixRollupOutcome(),
        tr_messages.Outcome.SummaryValueValuesEnum)
    return summary_fetcher.CreateMatrixOutcomeSummary()

  def Display(self, args, result):
    """Method called by Calliope to print the result of the Run() method.

    Args:
      args: The arguments that command was run with.
      result: one of:
        - a list of TestOutcome tuples (if ToolResults are available).
        - a URL string pointing to the user's raw results in GCS.
    """
    log.debug('gcloud test exit_code is: {0}'.format(self.exit_code))
    if type(result) == types.ListType:
      list_printer.PrintResourceList('test.run.outcomes', result)
    elif type(result) == types.StringType:
      log.out.Print('\nMore details are available at [{0}].'.format(result))
    elif result is not None:
      log.out.Print(result)
