# Copyright 2014 Google Inc. All Rights Reserved.

"""Delete cluster command."""
from googlecloudapis.apitools.base import py as apitools_base
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.container.lib import util
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core.util import console_io


# TODO(user): prompt for confirmation, take multiple resource args
class Delete(base.Command):
  """Delete an existing cluster for running containers."""

  @staticmethod
  def Args(parser):
    """Register flags for this command.

    Args:
      parser: An argparse.ArgumentParser-like object. It is mocked out in order
          to capture some information, but behaves like an ArgumentParser.
    """
    parser.add_argument(
        'names',
        metavar='NAME',
        nargs='+',
        help='The names of the clusters to delete.')
    parser.add_argument(
        '--no-wait',
        dest='wait',
        action='store_false',
        help='Return after issuing delete request without polling the operation'
        ' for completion.')

  @exceptions.RaiseToolExceptionInsteadOf(util.Error)
  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Returns:
      Some value that we want to have printed later.
    """
    adapter = self.context['api_adapter']

    cluster_refs = []
    for name in args.names:
      cluster_refs.append(adapter.ParseCluster(name))

    if not console_io.PromptContinue(
        message=util.ConstructList(
            'The following clusters will be deleted.',
            ['[{name}] in [{zone}]'.format(name=ref.clusterId,
                                           zone=adapter.Zone(ref))
             for ref in cluster_refs]),
        throw_if_unattended=True):
      raise exceptions.ToolException('Deletion aborted by user.')

    operations = []
    errors = []
    # Issue all deletes first
    for cluster_ref in cluster_refs:
      try:
        # Make sure it exists (will raise appropriate error if not)
        adapter.GetCluster(cluster_ref)

        op_ref = adapter.DeleteCluster(cluster_ref)
        operations.append((op_ref, cluster_ref))
      except apitools_base.HttpError as error:
        errors.append(util.GetError(error))
      except util.Error as error:
        errors.append(error)
    if args.wait:
      # Poll each operation for completion
      for operation_ref, cluster_ref in operations:
        try:
          adapter.WaitForOperation(
              operation_ref,
              'Deleting cluster {0}'.format(cluster_ref.clusterId))
          # Purge cached config files
          util.ClusterConfig.Purge(cluster_ref.clusterId,
                                   adapter.Zone(cluster_ref),
                                   cluster_ref.projectId)
          if properties.VALUES.container.cluster.Get() == cluster_ref.clusterId:
            properties.PersistProperty(
                properties.VALUES.container.cluster, None)
          log.DeletedResource(cluster_ref)
        except apitools_base.HttpError as error:
          errors.append(util.GetError(error))
        except util.Error as error:
          errors.append(error)

    if errors:
      raise exceptions.ToolException(util.ConstructList(
          'Some requests did not succeed:', errors))
