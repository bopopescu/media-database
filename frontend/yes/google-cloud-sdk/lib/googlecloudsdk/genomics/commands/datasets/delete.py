# Copyright 2015 Google Inc. All Rights Reserved.

"""Implementation of gcloud genomics datasets delete.
"""

from googlecloudsdk.calliope import base
from googlecloudsdk.core import log
from googlecloudsdk.core.util import console_io
from googlecloudsdk.genomics import commands
from googlecloudsdk.genomics.lib import genomics_util
from googlecloudsdk.genomics.lib.exceptions import GenomicsError


class DatasetsDelete(base.Command):
  """Deletes a dataset.
  """

  @staticmethod
  def Args(parser):
    """Register flags for this command."""
    parser.add_argument('id',
                        type=int,
                        help='The ID of the dataset to be deleted.')

  @genomics_util.ReraiseHttpException
  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace, All the arguments that were provided to this
        command invocation.

    Raises:
      HttpException: An http error response was received while executing api
          request.
    Returns:
      None
    """
    prompt_message = (
        'Deleting dataset {0} will delete all objects in the dataset. '
        'Deleted datasets can be recovered with the "restore" command '
        'up to one week after the deletion occurs.').format(args.id)

    if not console_io.PromptContinue(message=prompt_message):
      raise GenomicsError('Deletion aborted by user.')

    apitools_client = self.context[commands.GENOMICS_APITOOLS_CLIENT_KEY]
    genomics_messages = self.context[commands.GENOMICS_MESSAGES_MODULE_KEY]

    dataset = genomics_messages.GenomicsDatasetsDeleteRequest(
        datasetId=str(args.id),
    )

    apitools_client.datasets.Delete(dataset)
    log.Print('Deleted dataset {0}'.format(args.id))
