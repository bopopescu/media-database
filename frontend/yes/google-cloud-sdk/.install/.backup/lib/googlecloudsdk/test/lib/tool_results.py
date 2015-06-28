# Copyright 2015 Google Inc. All Rights Reserved.

"""A utility library to support interaction with the Tool Results service."""

import collections
import time
import urllib
import urlparse

from googlecloudsdk.core import properties
from googlecloudsdk.core.util import console_io


STATUS_INTERVAL_SECS = 1


class ToolResultsIds(
    collections.namedtuple('ToolResultsIds', ['history_id', 'execution_id'])):
  """A tuple to hold the history & execution IDs returned from Tool Results.

  Fields:
    history_id: a string with the Tool Results history ID to publish to.
    execution_id: a string with the ID of the Tool Results execution.
  """


def CreateToolResultsUiUrl(project_id, tool_results_ids):
  """Create a URL to the Tool Results UI for a test.

  Args:
    project_id: string containing the user's GCE project ID.
    tool_results_ids: a ToolResultsIds object holding history & execution IDs.

  Returns:
    A url to the Tool Results UI.
  """
  url_base = properties.VALUES.test.results_base_url.Get()
  if not url_base:
    url_base = 'https://console.developers.google.com'
  url_end = (
      'project/{p}/testlab/mobile/histories/{h}/executions/{e}'.format(
          p=urllib.quote(project_id),
          h=urllib.quote(tool_results_ids.history_id),
          e=urllib.quote(tool_results_ids.execution_id)))
  return urlparse.urljoin(url_base, url_end)


def GetToolResultsIds(matrix, testing_api_helper,
                      status_interval=STATUS_INTERVAL_SECS):
  """Gets the Tool Results history ID and execution ID for a test matrix.

  Sometimes the IDs are available immediately after a test matrix is created.
  If not, we keep checking the matrix until the Testing and Tool Results
  services have had enough time to create/assign the IDs, giving the user
  continuous feedback using gcloud core's ProgressTracker class.

  Args:
    matrix: a TestMatrix which was just created by the Testing service.
    testing_api_helper: a TestingApiHelper object.
    status_interval: float, number of seconds to sleep between status checks.

  Returns:
    A ToolResultsIds tuple containing the history ID and execution ID, which
    are shared by all TestExecutions in the TestMatrix.

  Raises:
    ToolException if either ID is missing from the TestMatrix.
  """
  history_id = None
  execution_id = None
  msg = 'Creating individual test executions'
  with console_io.ProgressTracker(msg, autotick=False) as pt:
    while True:
      if matrix.resultStorage.toolResultsExecution:
        history_id = matrix.resultStorage.toolResultsExecution.historyId
        execution_id = matrix.resultStorage.toolResultsExecution.executionId
        if history_id and execution_id:
          break

      pt.Tick()
      time.sleep(status_interval)
      matrix = testing_api_helper.GetTestMatrixStatus(matrix.testMatrixId)

  return ToolResultsIds(history_id=history_id, execution_id=execution_id)
