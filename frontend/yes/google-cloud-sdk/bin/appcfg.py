#!/usr/bin/env python
#
# Copyright 2013 Google Inc. All Rights Reserved.
#

"""A convenience wrapper for starting appengine for python."""

import bootstrapping.bootstrapping as bootstrapping

from googlecloudsdk.core import config
from googlecloudsdk.core.credentials import devshell


def main():
  """Launches appcfg.py."""

  unused_project, account = bootstrapping.GetActiveProjectAndAccount()
  json_creds = config.Paths().LegacyCredentialsJSONPath(account)

  args = ['--skip_sdk_update_check']
  try:
    creds = devshell.DevshellCredentials()
    args.extend([
        '--oauth2_access_token=' + creds.access_token
    ])
  except devshell.NoDevshellServer:
    args.extend([
        '--oauth2',
        '--oauth2_client_id=32555940559.apps.googleusercontent.com',
        '--oauth2_client_secret=ZmssLNjJy2998hD4CTg2ejr2',
        '--oauth2_credential_file={0}'.format(json_creds),
    ])
  bootstrapping.ExecutePythonTool('platform/google_appengine', 'appcfg.py', *args)


if __name__ == '__main__':
  bootstrapping.CommandStart('appcfg', component_id='gae-python')
  bootstrapping.PrerunChecks()
  main()
