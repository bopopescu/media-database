"""Generated client library for logging version v1beta3."""
# NOTE: This file is autogenerated and should not be edited by hand.

from googlecloudapis.apitools.base.py import base_api
from googlecloudapis.logging.v1beta3 import logging_v1beta3_messages as messages


class LoggingV1beta3(base_api.BaseApiClient):
  """Generated client library for service logging version v1beta3."""

  MESSAGES_MODULE = messages

  _PACKAGE = u'logging'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/logging.admin', u'https://www.googleapis.com/auth/logging.read', u'https://www.googleapis.com/auth/logging.write']
  _VERSION = u'v1beta3'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = ''
  _CLIENT_CLASS_NAME = u'LoggingV1beta3'
  _URL_VERSION = u'v1beta3'

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new logging handle."""
    url = url or u'https://logging.googleapis.com/'
    super(LoggingV1beta3, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.projects_logEntries = self.ProjectsLogEntriesService(self)
    self.projects_logServices_indexes = self.ProjectsLogServicesIndexesService(self)
    self.projects_logServices_sinks = self.ProjectsLogServicesSinksService(self)
    self.projects_logServices = self.ProjectsLogServicesService(self)
    self.projects_logs_entries = self.ProjectsLogsEntriesService(self)
    self.projects_logs_sinks = self.ProjectsLogsSinksService(self)
    self.projects_logs = self.ProjectsLogsService(self)
    self.projects_metrics = self.ProjectsMetricsService(self)
    self.projects_sinks = self.ProjectsSinksService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLogEntriesService(base_api.BaseApiService):
    """Service class for the projects_logEntries resource."""

    _NAME = u'projects_logEntries'

    def __init__(self, client):
      super(LoggingV1beta3.ProjectsLogEntriesService, self).__init__(client)
      self._method_configs = {
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.projects.logEntries.list',
              ordered_params=[u'projectsId'],
              path_params=[u'projectsId'],
              query_params=[u'filter', u'orderBy', u'pageSize', u'pageToken'],
              relative_path=u'v1beta3/projects/{projectsId}/logEntries',
              request_field='',
              request_type_name=u'LoggingProjectsLogEntriesListRequest',
              response_type_name=u'ListLogEntriesResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Lists log entries in the specified project.

      Args:
        request: (LoggingProjectsLogEntriesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLogEntriesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsLogServicesIndexesService(base_api.BaseApiService):
    """Service class for the projects_logServices_indexes resource."""

    _NAME = u'projects_logServices_indexes'

    def __init__(self, client):
      super(LoggingV1beta3.ProjectsLogServicesIndexesService, self).__init__(client)
      self._method_configs = {
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.projects.logServices.indexes.list',
              ordered_params=[u'projectsId', u'logServicesId'],
              path_params=[u'logServicesId', u'projectsId'],
              query_params=[u'depth', u'indexPrefix', u'log', u'pageSize', u'pageToken'],
              relative_path=u'v1beta3/projects/{projectsId}/logServices/{logServicesId}/indexes',
              request_field='',
              request_type_name=u'LoggingProjectsLogServicesIndexesListRequest',
              response_type_name=u'ListLogServiceIndexesResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Lists log service indexes associated with a log service.

      Args:
        request: (LoggingProjectsLogServicesIndexesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLogServiceIndexesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsLogServicesSinksService(base_api.BaseApiService):
    """Service class for the projects_logServices_sinks resource."""

    _NAME = u'projects_logServices_sinks'

    def __init__(self, client):
      super(LoggingV1beta3.ProjectsLogServicesSinksService, self).__init__(client)
      self._method_configs = {
          'Create': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'logging.projects.logServices.sinks.create',
              ordered_params=[u'projectsId', u'logServicesId'],
              path_params=[u'logServicesId', u'projectsId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/logServices/{logServicesId}/sinks',
              request_field=u'logSink',
              request_type_name=u'LoggingProjectsLogServicesSinksCreateRequest',
              response_type_name=u'LogSink',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'logging.projects.logServices.sinks.delete',
              ordered_params=[u'projectsId', u'logServicesId', u'sinksId'],
              path_params=[u'logServicesId', u'projectsId', u'sinksId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/logServices/{logServicesId}/sinks/{sinksId}',
              request_field='',
              request_type_name=u'LoggingProjectsLogServicesSinksDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.projects.logServices.sinks.get',
              ordered_params=[u'projectsId', u'logServicesId', u'sinksId'],
              path_params=[u'logServicesId', u'projectsId', u'sinksId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/logServices/{logServicesId}/sinks/{sinksId}',
              request_field='',
              request_type_name=u'LoggingProjectsLogServicesSinksGetRequest',
              response_type_name=u'LogSink',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.projects.logServices.sinks.list',
              ordered_params=[u'projectsId', u'logServicesId'],
              path_params=[u'logServicesId', u'projectsId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/logServices/{logServicesId}/sinks',
              request_field='',
              request_type_name=u'LoggingProjectsLogServicesSinksListRequest',
              response_type_name=u'ListLogServiceSinksResponse',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'logging.projects.logServices.sinks.update',
              ordered_params=[u'projectsId', u'logServicesId', u'sinksId'],
              path_params=[u'logServicesId', u'projectsId', u'sinksId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/logServices/{logServicesId}/sinks/{sinksId}',
              request_field=u'logSink',
              request_type_name=u'LoggingProjectsLogServicesSinksUpdateRequest',
              response_type_name=u'LogSink',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates the specified log service sink resource.

      Args:
        request: (LoggingProjectsLogServicesSinksCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogSink) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes the specified log service sink.

      Args:
        request: (LoggingProjectsLogServicesSinksDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Gets the specified log service sink resource.

      Args:
        request: (LoggingProjectsLogServicesSinksGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogSink) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists log service sinks associated with the specified service.

      Args:
        request: (LoggingProjectsLogServicesSinksListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLogServiceSinksResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Creates or update the specified log service sink resource.

      Args:
        request: (LoggingProjectsLogServicesSinksUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogSink) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsLogServicesService(base_api.BaseApiService):
    """Service class for the projects_logServices resource."""

    _NAME = u'projects_logServices'

    def __init__(self, client):
      super(LoggingV1beta3.ProjectsLogServicesService, self).__init__(client)
      self._method_configs = {
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.projects.logServices.list',
              ordered_params=[u'projectsId'],
              path_params=[u'projectsId'],
              query_params=[u'log', u'pageSize', u'pageToken'],
              relative_path=u'v1beta3/projects/{projectsId}/logServices',
              request_field='',
              request_type_name=u'LoggingProjectsLogServicesListRequest',
              response_type_name=u'ListLogServicesResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Lists log services associated with log entries ingested for a project.

      Args:
        request: (LoggingProjectsLogServicesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLogServicesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsLogsEntriesService(base_api.BaseApiService):
    """Service class for the projects_logs_entries resource."""

    _NAME = u'projects_logs_entries'

    def __init__(self, client):
      super(LoggingV1beta3.ProjectsLogsEntriesService, self).__init__(client)
      self._method_configs = {
          'Write': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'logging.projects.logs.entries.write',
              ordered_params=[u'projectsId', u'logsId'],
              path_params=[u'logsId', u'projectsId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/logs/{logsId}/entries:write',
              request_field=u'writeLogEntriesRequest',
              request_type_name=u'LoggingProjectsLogsEntriesWriteRequest',
              response_type_name=u'WriteLogEntriesResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Write(self, request, global_params=None):
      """Creates one or more log entries in a log.  You must supply a list of.
`LogEntry` objects, named `entries`.  Each `LogEntry` object must contain a
payload object and a `LogEntryMetadata` object that describes the
entry. You must fill in all the fields of the entry, metadata, and payload.
You can also supply a map, `commonLabels`, that supplies default (key,
value) data for the `entries[].metadata.labels` maps, saving you the
trouble of creating identical copies for each entry.

      Args:
        request: (LoggingProjectsLogsEntriesWriteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (WriteLogEntriesResponse) The response message.
      """
      config = self.GetMethodConfig('Write')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsLogsSinksService(base_api.BaseApiService):
    """Service class for the projects_logs_sinks resource."""

    _NAME = u'projects_logs_sinks'

    def __init__(self, client):
      super(LoggingV1beta3.ProjectsLogsSinksService, self).__init__(client)
      self._method_configs = {
          'Create': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'logging.projects.logs.sinks.create',
              ordered_params=[u'projectsId', u'logsId'],
              path_params=[u'logsId', u'projectsId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/logs/{logsId}/sinks',
              request_field=u'logSink',
              request_type_name=u'LoggingProjectsLogsSinksCreateRequest',
              response_type_name=u'LogSink',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'logging.projects.logs.sinks.delete',
              ordered_params=[u'projectsId', u'logsId', u'sinksId'],
              path_params=[u'logsId', u'projectsId', u'sinksId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/logs/{logsId}/sinks/{sinksId}',
              request_field='',
              request_type_name=u'LoggingProjectsLogsSinksDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.projects.logs.sinks.get',
              ordered_params=[u'projectsId', u'logsId', u'sinksId'],
              path_params=[u'logsId', u'projectsId', u'sinksId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/logs/{logsId}/sinks/{sinksId}',
              request_field='',
              request_type_name=u'LoggingProjectsLogsSinksGetRequest',
              response_type_name=u'LogSink',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.projects.logs.sinks.list',
              ordered_params=[u'projectsId', u'logsId'],
              path_params=[u'logsId', u'projectsId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/logs/{logsId}/sinks',
              request_field='',
              request_type_name=u'LoggingProjectsLogsSinksListRequest',
              response_type_name=u'ListLogSinksResponse',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'logging.projects.logs.sinks.update',
              ordered_params=[u'projectsId', u'logsId', u'sinksId'],
              path_params=[u'logsId', u'projectsId', u'sinksId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/logs/{logsId}/sinks/{sinksId}',
              request_field=u'logSink',
              request_type_name=u'LoggingProjectsLogsSinksUpdateRequest',
              response_type_name=u'LogSink',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates the specified log sink resource.

      Args:
        request: (LoggingProjectsLogsSinksCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogSink) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes the specified log sink resource.

      Args:
        request: (LoggingProjectsLogsSinksDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Gets the specified log sink resource.

      Args:
        request: (LoggingProjectsLogsSinksGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogSink) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists log sinks associated with the specified log.

      Args:
        request: (LoggingProjectsLogsSinksListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLogSinksResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Creates or updates the specified log sink resource.

      Args:
        request: (LoggingProjectsLogsSinksUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogSink) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsLogsService(base_api.BaseApiService):
    """Service class for the projects_logs resource."""

    _NAME = u'projects_logs'

    def __init__(self, client):
      super(LoggingV1beta3.ProjectsLogsService, self).__init__(client)
      self._method_configs = {
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'logging.projects.logs.delete',
              ordered_params=[u'projectsId', u'logsId'],
              path_params=[u'logsId', u'projectsId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/logs/{logsId}',
              request_field='',
              request_type_name=u'LoggingProjectsLogsDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.projects.logs.list',
              ordered_params=[u'projectsId'],
              path_params=[u'projectsId'],
              query_params=[u'pageSize', u'pageToken', u'serviceIndexPrefix', u'serviceName'],
              relative_path=u'v1beta3/projects/{projectsId}/logs',
              request_field='',
              request_type_name=u'LoggingProjectsLogsListRequest',
              response_type_name=u'ListLogsResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      """Deletes the specified log resource and all log entries contained in it.

      Args:
        request: (LoggingProjectsLogsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists log resources belonging to the specified project.

      Args:
        request: (LoggingProjectsLogsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLogsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsMetricsService(base_api.BaseApiService):
    """Service class for the projects_metrics resource."""

    _NAME = u'projects_metrics'

    def __init__(self, client):
      super(LoggingV1beta3.ProjectsMetricsService, self).__init__(client)
      self._method_configs = {
          'Create': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'logging.projects.metrics.create',
              ordered_params=[u'projectsId'],
              path_params=[u'projectsId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/metrics',
              request_field=u'logMetric',
              request_type_name=u'LoggingProjectsMetricsCreateRequest',
              response_type_name=u'LogMetric',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'logging.projects.metrics.delete',
              ordered_params=[u'projectsId', u'metricsId'],
              path_params=[u'metricsId', u'projectsId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/metrics/{metricsId}',
              request_field='',
              request_type_name=u'LoggingProjectsMetricsDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.projects.metrics.get',
              ordered_params=[u'projectsId', u'metricsId'],
              path_params=[u'metricsId', u'projectsId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/metrics/{metricsId}',
              request_field='',
              request_type_name=u'LoggingProjectsMetricsGetRequest',
              response_type_name=u'LogMetric',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.projects.metrics.list',
              ordered_params=[u'projectsId'],
              path_params=[u'projectsId'],
              query_params=[u'pageSize', u'pageToken'],
              relative_path=u'v1beta3/projects/{projectsId}/metrics',
              request_field='',
              request_type_name=u'LoggingProjectsMetricsListRequest',
              response_type_name=u'ListLogMetricsResponse',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'logging.projects.metrics.update',
              ordered_params=[u'projectsId', u'metricsId'],
              path_params=[u'metricsId', u'projectsId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/metrics/{metricsId}',
              request_field=u'logMetric',
              request_type_name=u'LoggingProjectsMetricsUpdateRequest',
              response_type_name=u'LogMetric',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Create the specified log metric resource.

      Args:
        request: (LoggingProjectsMetricsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogMetric) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes the specified log metric.

      Args:
        request: (LoggingProjectsMetricsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Get the specified log metric resource.

      Args:
        request: (LoggingProjectsMetricsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogMetric) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """List log metrics associated with the specified project.

      Args:
        request: (LoggingProjectsMetricsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLogMetricsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Create or update the specified log metric resource.

      Args:
        request: (LoggingProjectsMetricsUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogMetric) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsSinksService(base_api.BaseApiService):
    """Service class for the projects_sinks resource."""

    _NAME = u'projects_sinks'

    def __init__(self, client):
      super(LoggingV1beta3.ProjectsSinksService, self).__init__(client)
      self._method_configs = {
          'Create': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'logging.projects.sinks.create',
              ordered_params=[u'projectsId'],
              path_params=[u'projectsId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/sinks',
              request_field=u'logSink',
              request_type_name=u'LoggingProjectsSinksCreateRequest',
              response_type_name=u'LogSink',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'logging.projects.sinks.delete',
              ordered_params=[u'projectsId', u'sinksId'],
              path_params=[u'projectsId', u'sinksId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/sinks/{sinksId}',
              request_field='',
              request_type_name=u'LoggingProjectsSinksDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.projects.sinks.get',
              ordered_params=[u'projectsId', u'sinksId'],
              path_params=[u'projectsId', u'sinksId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/sinks/{sinksId}',
              request_field='',
              request_type_name=u'LoggingProjectsSinksGetRequest',
              response_type_name=u'LogSink',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'logging.projects.sinks.list',
              ordered_params=[u'projectsId'],
              path_params=[u'projectsId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/sinks',
              request_field='',
              request_type_name=u'LoggingProjectsSinksListRequest',
              response_type_name=u'ListSinksResponse',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'logging.projects.sinks.update',
              ordered_params=[u'projectsId', u'sinksId'],
              path_params=[u'projectsId', u'sinksId'],
              query_params=[],
              relative_path=u'v1beta3/projects/{projectsId}/sinks/{sinksId}',
              request_field=u'logSink',
              request_type_name=u'LoggingProjectsSinksUpdateRequest',
              response_type_name=u'LogSink',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates the specified sink resource.

      Args:
        request: (LoggingProjectsSinksCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogSink) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes the specified sink.

      Args:
        request: (LoggingProjectsSinksDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Gets the specified sink resource.

      Args:
        request: (LoggingProjectsSinksGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogSink) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists sinks associated with the specified project.

      Args:
        request: (LoggingProjectsSinksListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListSinksResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Creates or update the specified sink resource.

      Args:
        request: (LoggingProjectsSinksUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LogSink) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(LoggingV1beta3.ProjectsService, self).__init__(client)
      self._method_configs = {
          }

      self._upload_configs = {
          }