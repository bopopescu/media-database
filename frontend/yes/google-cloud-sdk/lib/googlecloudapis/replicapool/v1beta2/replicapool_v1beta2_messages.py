"""Generated message classes for replicapool version v1beta2.

The Google Compute Engine Instance Group Manager API provides groups of
homogenous Compute Engine Instances.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from protorpc import messages as _messages


package = 'replicapool'


class InstanceGroupManager(_messages.Message):
  """An Instance Group Manager resource.

  Fields:
    autoHealingPolicies: The autohealing policy for this managed instance
      group. You can specify only one value.
    baseInstanceName: The base instance name to use for instances in this
      group. The value must be a valid RFC1035 name. Supported characters are
      lowercase letters, numbers, and hyphens (-). Instances are named by
      appending a hyphen and a random four-character string to the base
      instance name.
    creationTimestamp: [Output only] The time the instance group manager was
      created, in RFC3339 text format.
    currentSize: [Output only] The number of instances that currently exist
      and are a part of this group. This includes instances that are starting
      but are not yet RUNNING, and instances that are in the process of being
      deleted or abandoned.
    description: An optional textual description of the instance group
      manager.
    fingerprint: [Output only] Fingerprint of the instance group manager. This
      field is used for optimistic locking. An up-to-date fingerprint must be
      provided in order to modify the Instance Group Manager resource.
    group: [Output only] The full URL of the instance group created by the
      manager. This group contains all of the instances being managed, and
      cannot contain non-managed instances.
    id: [Output only] A server-assigned unique identifier for the resource.
    instanceTemplate: The full URL to an instance template from which all new
      instances will be created.
    kind: [Output only] The resource type. Always
      replicapool#instanceGroupManager.
    name: The name of the instance group manager. Must be 1-63 characters long
      and comply with RFC1035. Supported characters include lowercase letters,
      numbers, and hyphens.
    selfLink: [Output only] The fully qualified URL for this resource.
    targetPools: The full URL of all target pools to which new instances in
      the group are added. Updating the target pool values does not affect
      existing instances.
    targetSize: [Output only] The number of instances that the manager is
      attempting to maintain. Deleting or abandoning instances affects this
      number, as does resizing the group.
  """

  autoHealingPolicies = _messages.MessageField('ReplicaPoolAutoHealingPolicy', 1, repeated=True)
  baseInstanceName = _messages.StringField(2)
  creationTimestamp = _messages.StringField(3)
  currentSize = _messages.IntegerField(4, variant=_messages.Variant.INT32)
  description = _messages.StringField(5)
  fingerprint = _messages.BytesField(6)
  group = _messages.StringField(7)
  id = _messages.IntegerField(8, variant=_messages.Variant.UINT64)
  instanceTemplate = _messages.StringField(9)
  kind = _messages.StringField(10, default=u'replicapool#instanceGroupManager')
  name = _messages.StringField(11)
  selfLink = _messages.StringField(12)
  targetPools = _messages.StringField(13, repeated=True)
  targetSize = _messages.IntegerField(14, variant=_messages.Variant.INT32)


class InstanceGroupManagerList(_messages.Message):
  """A InstanceGroupManagerList object.

  Fields:
    id: Unique identifier for the resource; defined by the server (output
      only).
    items: A list of instance resources.
    kind: Type of resource.
    nextPageToken: A token used to continue a truncated list request (output
      only).
    selfLink: Server defined URL for this resource (output only).
  """

  id = _messages.StringField(1)
  items = _messages.MessageField('InstanceGroupManager', 2, repeated=True)
  kind = _messages.StringField(3, default=u'replicapool#instanceGroupManagerList')
  nextPageToken = _messages.StringField(4)
  selfLink = _messages.StringField(5)


class InstanceGroupManagersAbandonInstancesRequest(_messages.Message):
  """A InstanceGroupManagersAbandonInstancesRequest object.

  Fields:
    instances: The names of one or more instances to abandon. For example: {
      'instances': [ 'instance-c3po', 'instance-r2d2' ] }
  """

  instances = _messages.StringField(1, repeated=True)


class InstanceGroupManagersDeleteInstancesRequest(_messages.Message):
  """A InstanceGroupManagersDeleteInstancesRequest object.

  Fields:
    instances: Names of instances to delete.  Example: 'instance-foo',
      'instance-bar'
  """

  instances = _messages.StringField(1, repeated=True)


class InstanceGroupManagersRecreateInstancesRequest(_messages.Message):
  """A InstanceGroupManagersRecreateInstancesRequest object.

  Fields:
    instances: The names of one or more instances to recreate. For example: {
      'instances': [ 'instance-c3po', 'instance-r2d2' ] }
  """

  instances = _messages.StringField(1, repeated=True)


class InstanceGroupManagersSetAutoHealingPolicyRequest(_messages.Message):
  """A InstanceGroupManagersSetAutoHealingPolicyRequest object.

  Fields:
    autoHealingPolicies: The autohealing policy for this managed instance
      group. You can specify only one value.
  """

  autoHealingPolicies = _messages.MessageField('ReplicaPoolAutoHealingPolicy', 1, repeated=True)


class InstanceGroupManagersSetInstanceTemplateRequest(_messages.Message):
  """A InstanceGroupManagersSetInstanceTemplateRequest object.

  Fields:
    instanceTemplate: The full URL to an Instance Template from which all new
      instances will be created.
  """

  instanceTemplate = _messages.StringField(1)


class InstanceGroupManagersSetTargetPoolsRequest(_messages.Message):
  """A InstanceGroupManagersSetTargetPoolsRequest object.

  Fields:
    fingerprint: The current fingerprint of the Instance Group Manager
      resource. If this does not match the server-side fingerprint of the
      resource, then the request will be rejected.
    targetPools: A list of fully-qualified URLs to existing Target Pool
      resources. New instances in the Instance Group Manager will be added to
      the specified target pools; existing instances are not affected.
  """

  fingerprint = _messages.BytesField(1)
  targetPools = _messages.StringField(2, repeated=True)


class Operation(_messages.Message):
  """An operation resource, used to manage asynchronous API requests.

  Enums:
    StatusValueValuesEnum: [Output Only] Status of the operation.

  Messages:
    ErrorValue: [Output Only] If errors occurred during processing of this
      operation, this field will be populated.
    WarningsValueListEntry: A WarningsValueListEntry object.

  Fields:
    clientOperationId: [Output only] An optional identifier specified by the
      client when the mutation was initiated. Must be unique for all operation
      resources in the project.
    creationTimestamp: [Output Only] The time that this operation was
      requested, in RFC3339 text format.
    endTime: [Output Only] The time that this operation was completed, in
      RFC3339 text format.
    error: [Output Only] If errors occurred during processing of this
      operation, this field will be populated.
    httpErrorMessage: [Output only] If operation fails, the HTTP error message
      returned.
    httpErrorStatusCode: [Output only] If operation fails, the HTTP error
      status code returned.
    id: [Output Only] Unique identifier for the resource, generated by the
      server.
    insertTime: [Output Only] The time that this operation was requested, in
      RFC3339 text format.
    kind: [Output only] Type of the resource.
    name: [Output Only] Name of the resource.
    operationType: [Output only] Type of the operation. Operations include
      insert, update, and delete.
    progress: [Output only] An optional progress indicator that ranges from 0
      to 100. There is no requirement that this be linear or support any
      granularity of operations. This should not be used to guess at when the
      operation will be complete. This number should be monotonically
      increasing as the operation progresses.
    region: [Output Only] URL of the region where the operation resides. Only
      available when performing regional operations.
    selfLink: [Output Only] Server-defined fully-qualified URL for this
      resource.
    startTime: [Output Only] The time that this operation was started by the
      server, in RFC3339 text format.
    status: [Output Only] Status of the operation.
    statusMessage: [Output Only] An optional textual description of the
      current status of the operation.
    targetId: [Output Only] Unique target ID which identifies a particular
      incarnation of the target.
    targetLink: [Output only] URL of the resource the operation is mutating.
    user: [Output Only] User who requested the operation, for example:
      user@example.com.
    warnings: [Output Only] If there are issues with this operation, a warning
      is returned.
    zone: [Output Only] URL of the zone where the operation resides. Only
      available when performing per-zone operations.
  """

  class StatusValueValuesEnum(_messages.Enum):
    """[Output Only] Status of the operation.

    Values:
      DONE: <no description>
      PENDING: <no description>
      RUNNING: <no description>
    """
    DONE = 0
    PENDING = 1
    RUNNING = 2

  class ErrorValue(_messages.Message):
    """[Output Only] If errors occurred during processing of this operation,
    this field will be populated.

    Messages:
      ErrorsValueListEntry: A ErrorsValueListEntry object.

    Fields:
      errors: [Output Only] The array of errors encountered while processing
        this operation.
    """

    class ErrorsValueListEntry(_messages.Message):
      """A ErrorsValueListEntry object.

      Fields:
        code: [Output Only] The error type identifier for this error.
        location: [Output Only] Indicates the field in the request which
          caused the error. This property is optional.
        message: [Output Only] An optional, human-readable error message.
      """

      code = _messages.StringField(1)
      location = _messages.StringField(2)
      message = _messages.StringField(3)

    errors = _messages.MessageField('ErrorsValueListEntry', 1, repeated=True)

  class WarningsValueListEntry(_messages.Message):
    """A WarningsValueListEntry object.

    Enums:
      CodeValueValuesEnum: [Output only] The warning type identifier for this
        warning.

    Messages:
      DataValueListEntry: A DataValueListEntry object.

    Fields:
      code: [Output only] The warning type identifier for this warning.
      data: [Output only] Metadata for this warning in key:value format.
      message: [Output only] Optional human-readable details for this warning.
    """

    class CodeValueValuesEnum(_messages.Enum):
      """[Output only] The warning type identifier for this warning.

      Values:
        DEPRECATED_RESOURCE_USED: <no description>
        DISK_SIZE_LARGER_THAN_IMAGE_SIZE: <no description>
        INJECTED_KERNELS_DEPRECATED: <no description>
        NEXT_HOP_ADDRESS_NOT_ASSIGNED: <no description>
        NEXT_HOP_CANNOT_IP_FORWARD: <no description>
        NEXT_HOP_INSTANCE_NOT_FOUND: <no description>
        NEXT_HOP_INSTANCE_NOT_ON_NETWORK: <no description>
        NEXT_HOP_NOT_RUNNING: <no description>
        NO_RESULTS_ON_PAGE: <no description>
        REQUIRED_TOS_AGREEMENT: <no description>
        RESOURCE_NOT_DELETED: <no description>
        SINGLE_INSTANCE_PROPERTY_TEMPLATE: <no description>
        UNREACHABLE: <no description>
      """
      DEPRECATED_RESOURCE_USED = 0
      DISK_SIZE_LARGER_THAN_IMAGE_SIZE = 1
      INJECTED_KERNELS_DEPRECATED = 2
      NEXT_HOP_ADDRESS_NOT_ASSIGNED = 3
      NEXT_HOP_CANNOT_IP_FORWARD = 4
      NEXT_HOP_INSTANCE_NOT_FOUND = 5
      NEXT_HOP_INSTANCE_NOT_ON_NETWORK = 6
      NEXT_HOP_NOT_RUNNING = 7
      NO_RESULTS_ON_PAGE = 8
      REQUIRED_TOS_AGREEMENT = 9
      RESOURCE_NOT_DELETED = 10
      SINGLE_INSTANCE_PROPERTY_TEMPLATE = 11
      UNREACHABLE = 12

    class DataValueListEntry(_messages.Message):
      """A DataValueListEntry object.

      Fields:
        key: [Output Only] Metadata key for this warning.
        value: [Output Only] Metadata value for this warning.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    code = _messages.EnumField('CodeValueValuesEnum', 1)
    data = _messages.MessageField('DataValueListEntry', 2, repeated=True)
    message = _messages.StringField(3)

  clientOperationId = _messages.StringField(1)
  creationTimestamp = _messages.StringField(2)
  endTime = _messages.StringField(3)
  error = _messages.MessageField('ErrorValue', 4)
  httpErrorMessage = _messages.StringField(5)
  httpErrorStatusCode = _messages.IntegerField(6, variant=_messages.Variant.INT32)
  id = _messages.IntegerField(7, variant=_messages.Variant.UINT64)
  insertTime = _messages.StringField(8)
  kind = _messages.StringField(9, default=u'replicapool#operation')
  name = _messages.StringField(10)
  operationType = _messages.StringField(11)
  progress = _messages.IntegerField(12, variant=_messages.Variant.INT32)
  region = _messages.StringField(13)
  selfLink = _messages.StringField(14)
  startTime = _messages.StringField(15)
  status = _messages.EnumField('StatusValueValuesEnum', 16)
  statusMessage = _messages.StringField(17)
  targetId = _messages.IntegerField(18, variant=_messages.Variant.UINT64)
  targetLink = _messages.StringField(19)
  user = _messages.StringField(20)
  warnings = _messages.MessageField('WarningsValueListEntry', 21, repeated=True)
  zone = _messages.StringField(22)


class OperationList(_messages.Message):
  """A OperationList object.

  Fields:
    id: Unique identifier for the resource; defined by the server (output
      only).
    items: The operation resources.
    kind: Type of resource.
    nextPageToken: A token used to continue a truncated list request (output
      only).
    selfLink: Server defined URL for this resource (output only).
  """

  id = _messages.StringField(1)
  items = _messages.MessageField('Operation', 2, repeated=True)
  kind = _messages.StringField(3, default=u'replicapool#operationList')
  nextPageToken = _messages.StringField(4)
  selfLink = _messages.StringField(5)


class ReplicaPoolAutoHealingPolicy(_messages.Message):
  """A ReplicaPoolAutoHealingPolicy object.

  Fields:
    healthCheck: The URL for the HealthCheck that signals autohealing.
  """

  healthCheck = _messages.StringField(1)


class ReplicapoolInstanceGroupManagersAbandonInstancesRequest(_messages.Message):
  """A ReplicapoolInstanceGroupManagersAbandonInstancesRequest object.

  Fields:
    instanceGroupManager: The name of the instance group manager.
    instanceGroupManagersAbandonInstancesRequest: A
      InstanceGroupManagersAbandonInstancesRequest resource to be passed as
      the request body.
    project: The Google Developers Console project name.
    zone: The name of the zone in which the instance group manager resides.
  """

  instanceGroupManager = _messages.StringField(1, required=True)
  instanceGroupManagersAbandonInstancesRequest = _messages.MessageField('InstanceGroupManagersAbandonInstancesRequest', 2)
  project = _messages.StringField(3, required=True)
  zone = _messages.StringField(4, required=True)


class ReplicapoolInstanceGroupManagersDeleteInstancesRequest(_messages.Message):
  """A ReplicapoolInstanceGroupManagersDeleteInstancesRequest object.

  Fields:
    instanceGroupManager: The name of the instance group manager.
    instanceGroupManagersDeleteInstancesRequest: A
      InstanceGroupManagersDeleteInstancesRequest resource to be passed as the
      request body.
    project: The Google Developers Console project name.
    zone: The name of the zone in which the instance group manager resides.
  """

  instanceGroupManager = _messages.StringField(1, required=True)
  instanceGroupManagersDeleteInstancesRequest = _messages.MessageField('InstanceGroupManagersDeleteInstancesRequest', 2)
  project = _messages.StringField(3, required=True)
  zone = _messages.StringField(4, required=True)


class ReplicapoolInstanceGroupManagersDeleteRequest(_messages.Message):
  """A ReplicapoolInstanceGroupManagersDeleteRequest object.

  Fields:
    instanceGroupManager: Name of the Instance Group Manager resource to
      delete.
    project: The Google Developers Console project name.
    zone: The name of the zone in which the instance group manager resides.
  """

  instanceGroupManager = _messages.StringField(1, required=True)
  project = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ReplicapoolInstanceGroupManagersGetRequest(_messages.Message):
  """A ReplicapoolInstanceGroupManagersGetRequest object.

  Fields:
    instanceGroupManager: Name of the instance resource to return.
    project: The Google Developers Console project name.
    zone: The name of the zone in which the instance group manager resides.
  """

  instanceGroupManager = _messages.StringField(1, required=True)
  project = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ReplicapoolInstanceGroupManagersInsertRequest(_messages.Message):
  """A ReplicapoolInstanceGroupManagersInsertRequest object.

  Fields:
    instanceGroupManager: A InstanceGroupManager resource to be passed as the
      request body.
    project: The Google Developers Console project name.
    size: Number of instances that should exist.
    zone: The name of the zone in which the instance group manager resides.
  """

  instanceGroupManager = _messages.MessageField('InstanceGroupManager', 1)
  project = _messages.StringField(2, required=True)
  size = _messages.IntegerField(3, required=True, variant=_messages.Variant.INT32)
  zone = _messages.StringField(4, required=True)


class ReplicapoolInstanceGroupManagersListRequest(_messages.Message):
  """A ReplicapoolInstanceGroupManagersListRequest object.

  Fields:
    filter: Optional. Filter expression for filtering listed resources.
    maxResults: Optional. Maximum count of results to be returned. Maximum
      value is 500 and default value is 500.
    pageToken: Optional. Tag returned by a previous list request truncated by
      maxResults. Used to continue a previous list request.
    project: The Google Developers Console project name.
    zone: The name of the zone in which the instance group manager resides.
  """

  filter = _messages.StringField(1)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.UINT32, default=500)
  pageToken = _messages.StringField(3)
  project = _messages.StringField(4, required=True)
  zone = _messages.StringField(5, required=True)


class ReplicapoolInstanceGroupManagersRecreateInstancesRequest(_messages.Message):
  """A ReplicapoolInstanceGroupManagersRecreateInstancesRequest object.

  Fields:
    instanceGroupManager: The name of the instance group manager.
    instanceGroupManagersRecreateInstancesRequest: A
      InstanceGroupManagersRecreateInstancesRequest resource to be passed as
      the request body.
    project: The Google Developers Console project name.
    zone: The name of the zone in which the instance group manager resides.
  """

  instanceGroupManager = _messages.StringField(1, required=True)
  instanceGroupManagersRecreateInstancesRequest = _messages.MessageField('InstanceGroupManagersRecreateInstancesRequest', 2)
  project = _messages.StringField(3, required=True)
  zone = _messages.StringField(4, required=True)


class ReplicapoolInstanceGroupManagersResizeRequest(_messages.Message):
  """A ReplicapoolInstanceGroupManagersResizeRequest object.

  Fields:
    instanceGroupManager: The name of the instance group manager.
    project: The Google Developers Console project name.
    size: Number of instances that should exist in this Instance Group
      Manager.
    zone: The name of the zone in which the instance group manager resides.
  """

  instanceGroupManager = _messages.StringField(1, required=True)
  project = _messages.StringField(2, required=True)
  size = _messages.IntegerField(3, required=True, variant=_messages.Variant.INT32)
  zone = _messages.StringField(4, required=True)


class ReplicapoolInstanceGroupManagersSetAutoHealingPolicyRequest(_messages.Message):
  """A ReplicapoolInstanceGroupManagersSetAutoHealingPolicyRequest object.

  Fields:
    instanceGroupManager: The name of the instance group manager.
    instanceGroupManagersSetAutoHealingPolicyRequest: A
      InstanceGroupManagersSetAutoHealingPolicyRequest resource to be passed
      as the request body.
    project: The Google Developers Console project name.
    zone: The name of the zone in which the instance group manager resides.
  """

  instanceGroupManager = _messages.StringField(1, required=True)
  instanceGroupManagersSetAutoHealingPolicyRequest = _messages.MessageField('InstanceGroupManagersSetAutoHealingPolicyRequest', 2)
  project = _messages.StringField(3, required=True)
  zone = _messages.StringField(4, required=True)


class ReplicapoolInstanceGroupManagersSetInstanceTemplateRequest(_messages.Message):
  """A ReplicapoolInstanceGroupManagersSetInstanceTemplateRequest object.

  Fields:
    instanceGroupManager: The name of the instance group manager.
    instanceGroupManagersSetInstanceTemplateRequest: A
      InstanceGroupManagersSetInstanceTemplateRequest resource to be passed as
      the request body.
    project: The Google Developers Console project name.
    zone: The name of the zone in which the instance group manager resides.
  """

  instanceGroupManager = _messages.StringField(1, required=True)
  instanceGroupManagersSetInstanceTemplateRequest = _messages.MessageField('InstanceGroupManagersSetInstanceTemplateRequest', 2)
  project = _messages.StringField(3, required=True)
  zone = _messages.StringField(4, required=True)


class ReplicapoolInstanceGroupManagersSetTargetPoolsRequest(_messages.Message):
  """A ReplicapoolInstanceGroupManagersSetTargetPoolsRequest object.

  Fields:
    instanceGroupManager: The name of the instance group manager.
    instanceGroupManagersSetTargetPoolsRequest: A
      InstanceGroupManagersSetTargetPoolsRequest resource to be passed as the
      request body.
    project: The Google Developers Console project name.
    zone: The name of the zone in which the instance group manager resides.
  """

  instanceGroupManager = _messages.StringField(1, required=True)
  instanceGroupManagersSetTargetPoolsRequest = _messages.MessageField('InstanceGroupManagersSetTargetPoolsRequest', 2)
  project = _messages.StringField(3, required=True)
  zone = _messages.StringField(4, required=True)


class ReplicapoolZoneOperationsGetRequest(_messages.Message):
  """A ReplicapoolZoneOperationsGetRequest object.

  Fields:
    operation: Name of the operation resource to return.
    project: Name of the project scoping this request.
    zone: Name of the zone scoping this request.
  """

  operation = _messages.StringField(1, required=True)
  project = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ReplicapoolZoneOperationsListRequest(_messages.Message):
  """A ReplicapoolZoneOperationsListRequest object.

  Fields:
    filter: Optional. Filter expression for filtering listed resources.
    maxResults: Optional. Maximum count of results to be returned. Maximum
      value is 500 and default value is 500.
    pageToken: Optional. Tag returned by a previous list request truncated by
      maxResults. Used to continue a previous list request.
    project: Name of the project scoping this request.
    zone: Name of the zone scoping this request.
  """

  filter = _messages.StringField(1)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.UINT32, default=500)
  pageToken = _messages.StringField(3)
  project = _messages.StringField(4, required=True)
  zone = _messages.StringField(5, required=True)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    AltValueValuesEnum: Data format for the response.

  Fields:
    alt: Data format for the response.
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters. Overrides userIp if both are provided.
    trace: A tracing token of the form "token:<tokenid>" or "email:<ldap>" to
      include in api requests.
    userIp: IP address of the site where the request originates. Use this if
      you want to enforce per-user limits.
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for the response.

    Values:
      json: Responses with Content-Type of application/json
    """
    json = 0

  alt = _messages.EnumField('AltValueValuesEnum', 1, default=u'json')
  fields = _messages.StringField(2)
  key = _messages.StringField(3)
  oauth_token = _messages.StringField(4)
  prettyPrint = _messages.BooleanField(5, default=True)
  quotaUser = _messages.StringField(6)
  trace = _messages.StringField(7)
  userIp = _messages.StringField(8)


