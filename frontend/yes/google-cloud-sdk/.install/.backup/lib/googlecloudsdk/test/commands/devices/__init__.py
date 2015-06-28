# Copyright 2014 Google Inc. All Rights Reserved.

"""The 'gcloud test devices' sub-group."""

from googlecloudsdk.calliope import base


class Devices(base.Group):
  """Command group for discovery of device environments."""

  @staticmethod
  def Args(parser):
    """Method called by Calliope to register flags common to this sub-group.

    Args:
      parser: An argparse parser used to add arguments that immediately follow
          this group in the CLI. Positional arguments are allowed.
    """
    pass
