# internal

### Available Operations

* [create_membership](#create_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [create_organization](#create_organization) - Create an organization
* [create_user](#create_user) - Create a user.
* [delete_organization](#delete_organization) - Delete an org
* [generate_report](#generate_report) - Generate an admin report
* [get_aws_marketplace_metadata](#get_aws_marketplace_metadata) - Get marketplace metadata for an org if any exists.
* [get_api_key](#get_api_key) - Get an api key by its id
* [get_connection](#get_connection) - Get the connection metadata for a given org
* [get_default_membership_for_email](#get_default_membership_for_email) - Get the default membership for a user.
* [get_feature_flags](#get_feature_flags) - Get feature flags for the specified user/org
* [get_memberships](#get_memberships) - Get memberships for a user.
* [get_memberships_by_email](#get_memberships_by_email) - Get memberships for a user given that user's email address.
* [get_memberships_by_org](#get_memberships_by_org) - Get memberships for an org.
* [get_monitor_config_v3_version](#get_monitor_config_v3_version) - Get the monitor config document version for a given dataset.
* [get_notification_settings](#get_notification_settings) - Get notification settings for an org
* [get_organization](#get_organization) - Get the metadata about an organization.
* [get_user](#get_user) - Get a user by their id.
* [get_user_by_email](#get_user_by_email) - Get a user by their email.
* [hide_segments](#hide_segments) - Hides a list of segments
* [list_api_keys](#list_api_keys) - List API key metadata for a given organization and user
* [list_jobs](#list_jobs) - List all of the jobs in a workspace.
* [list_monitor_config_v3_versions](#list_monitor_config_v3_versions) - List the monitor config document versions for a given dataset.
* [list_organizations](#list_organizations) - Get a list of all of the organization ids.
* [list_segments](#list_segments) - Returns a list of segments
* [~~partially_update_org~~](#partially_update_org) - Update some fields of an organization to non-null values :warning: **Deprecated**
* [partially_update_organization](#partially_update_organization) - Update some fields of an organization to non-null values
* [post_monitor_config_validation_job](#post_monitor_config_validation_job) - Create a monitor config validation job for all configs
* [provision_aws_marketplace_new_user](#provision_aws_marketplace_new_user) - Create resources for a new user coming from AWS Marketplace
* [provision_databricks_connection](#provision_databricks_connection) - Create resources for a new user coming from Databricks
* [provision_new_user](#provision_new_user) - Create the resources that a new user needs to use WhyLabs via the website.
* [put_request_monitor_run_config](#put_request_monitor_run_config) - Put the RequestMonitorRun config into S3.
* [refresh_connection](#refresh_connection) - Refresh metadata for a workspace connection.
* [register_databricks_connection](#register_databricks_connection) - Register databricks metadata, temporarily storing it against a UUID so that it can be used to provision a databricks connection after email authentication
* [remove_membership_by_email](#remove_membership_by_email) - Removes membership in a given org from a user, using the user's email address.
* [run_job](#run_job) - Run an existing job in a given databricks workspace.
* [set_default_membership](#set_default_membership) - Sets the organization that should be used when logging a user in
* [stripe_payment_endpoint](#stripe_payment_endpoint) - Endpoint for Stripe payment webhooks
* [update_connection](#update_connection) - Update the connection metadata for a given org
* [update_membership_by_email](#update_membership_by_email) - Updates the role in an membership
* [update_notification_settings](#update_notification_settings) - Update notification settings for an org
* [~~update_org~~](#update_org) - Update an existing organization :warning: **Deprecated**
* [update_organization](#update_organization) - Update an existing organization
* [update_user](#update_user) - Update a user.
* [why_labs_search](#why_labs_search) - WhyLabs Search
* [why_labs_search_indexing](#why_labs_search_indexing) - WhyLabs Search Indexing

## create_membership

Create a membership for a user, making them apart of an organization. Uses the user's current email address.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.AddMembershipRequest(
    created_by='totam',
    default=False,
    email='Haskell18@gmail.com',
    org_id='impedit',
    role=shared.Role.VIEWER,
)

res = s.internal.create_membership(req, operations.CreateMembershipSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.AddMembershipRequest](../../models/shared/addmembershiprequest.md)                 | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.CreateMembershipSecurity](../../models/operations/createmembershipsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.CreateMembershipResponse](../../models/operations/createmembershipresponse.md)**


## create_organization

Create an organization

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.CreateOrganizationRequest(
    domain='acme.ai',
    email_domains='acme.ai,acme.com',
    name='ACME, Inc',
    notification_email_address='notifications@acme.ai',
    observatory_url='https://hub.whylabsapp.com',
    override_id='org-123',
    pager_duty_key='abc-def-ghi-jkl',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.PAID,
)

res = s.internal.create_organization(req, operations.CreateOrganizationSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateOrganizationRequest](../../models/operations/createorganizationrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.CreateOrganizationSecurity](../../models/operations/createorganizationsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.CreateOrganizationResponse](../../models/operations/createorganizationresponse.md)**


## create_user

Create a user.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.CreateUserRequest(
    email='Keshaun32@gmail.com',
)

res = s.internal.create_user(req, operations.CreateUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.CreateUserRequest](../../models/shared/createuserrequest.md)           | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.CreateUserSecurity](../../models/operations/createusersecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.CreateUserResponse](../../models/operations/createuserresponse.md)**


## delete_organization

Delete an org

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.DeleteOrganizationRequest(
    org_id='natus',
)

res = s.internal.delete_organization(req, operations.DeleteOrganizationSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.DeleteOrganizationRequest](../../models/operations/deleteorganizationrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.DeleteOrganizationSecurity](../../models/operations/deleteorganizationsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.DeleteOrganizationResponse](../../models/operations/deleteorganizationresponse.md)**


## generate_report

Generate an admin report

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.GenerateReportRequest(
    report_type=shared.AdminReportType.SESSIONS,
)

res = s.internal.generate_report(req, operations.GenerateReportSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GenerateReportRequest](../../models/operations/generatereportrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GenerateReportSecurity](../../models/operations/generatereportsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GenerateReportResponse](../../models/operations/generatereportresponse.md)**


## get_aws_marketplace_metadata

Get marketplace metadata for an org if any exists.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetAWSMarketplaceMetadataRequest(
    org_id='sed',
)

res = s.internal.get_aws_marketplace_metadata(req, operations.GetAWSMarketplaceMetadataSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetAWSMarketplaceMetadataRequest](../../models/operations/getawsmarketplacemetadatarequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.GetAWSMarketplaceMetadataSecurity](../../models/operations/getawsmarketplacemetadatasecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.GetAWSMarketplaceMetadataResponse](../../models/operations/getawsmarketplacemetadataresponse.md)**


## get_api_key

Get an api key by its id

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetAPIKeyRequest(
    key_id='fh4dUNV3WQ',
    org_id='org-123',
)

res = s.internal.get_api_key(req, operations.GetAPIKeySecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetAPIKeyRequest](../../models/operations/getapikeyrequest.md)   | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `security`                                                                   | [operations.GetAPIKeySecurity](../../models/operations/getapikeysecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.GetAPIKeyResponse](../../models/operations/getapikeyresponse.md)**


## get_connection

Get the connection metadata for a given org

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.GetConnectionRequest(
    org_id='iste',
    workspace_id='dolor',
)

res = s.internal.get_connection(req, operations.GetConnectionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.GetConnectionRequest](../../models/shared/getconnectionrequest.md)           | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.GetConnectionSecurity](../../models/operations/getconnectionsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.GetConnectionResponse](../../models/operations/getconnectionresponse.md)**


## get_default_membership_for_email

Get the default membership for a user.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetDefaultMembershipForEmailRequest(
    email='Gertrude_Welch44@yahoo.com',
)

res = s.internal.get_default_membership_for_email(req, operations.GetDefaultMembershipForEmailSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetDefaultMembershipForEmailRequest](../../models/operations/getdefaultmembershipforemailrequest.md)   | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `security`                                                                                                         | [operations.GetDefaultMembershipForEmailSecurity](../../models/operations/getdefaultmembershipforemailsecurity.md) | :heavy_check_mark:                                                                                                 | The security requirements to use for the request.                                                                  |


### Response

**[operations.GetDefaultMembershipForEmailResponse](../../models/operations/getdefaultmembershipforemailresponse.md)**


## get_feature_flags

Get feature flags for the specified user/org

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetFeatureFlagsRequest(
    org_id='corporis',
    user_id='iste',
)

res = s.internal.get_feature_flags(req, operations.GetFeatureFlagsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetFeatureFlagsRequest](../../models/operations/getfeatureflagsrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.GetFeatureFlagsSecurity](../../models/operations/getfeatureflagssecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.GetFeatureFlagsResponse](../../models/operations/getfeatureflagsresponse.md)**


## get_memberships

Get memberships for a user.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetMembershipsRequest(
    user_id='iure',
)

res = s.internal.get_memberships(req, operations.GetMembershipsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetMembershipsRequest](../../models/operations/getmembershipsrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GetMembershipsSecurity](../../models/operations/getmembershipssecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GetMembershipsResponse](../../models/operations/getmembershipsresponse.md)**


## get_memberships_by_email

Get memberships for a user given that user's email address.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetMembershipsByEmailRequest(
    email='Maxie96@hotmail.com',
)

res = s.internal.get_memberships_by_email(req, operations.GetMembershipsByEmailSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetMembershipsByEmailRequest](../../models/operations/getmembershipsbyemailrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.GetMembershipsByEmailSecurity](../../models/operations/getmembershipsbyemailsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.GetMembershipsByEmailResponse](../../models/operations/getmembershipsbyemailresponse.md)**


## get_memberships_by_org

Get memberships for an org.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetMembershipsByOrgRequest(
    org_id='est',
)

res = s.internal.get_memberships_by_org(req, operations.GetMembershipsByOrgSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetMembershipsByOrgRequest](../../models/operations/getmembershipsbyorgrequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.GetMembershipsByOrgSecurity](../../models/operations/getmembershipsbyorgsecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.GetMembershipsByOrgResponse](../../models/operations/getmembershipsbyorgresponse.md)**


## get_monitor_config_v3_version

Get the monitor config document version for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetMonitorConfigV3VersionRequest(
    dataset_id='model-123',
    org_id='org-123',
    version_id='4920545486e2a4cdf0f770c09748e663',
)

res = s.internal.get_monitor_config_v3_version(req, operations.GetMonitorConfigV3VersionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetMonitorConfigV3VersionRequest](../../models/operations/getmonitorconfigv3versionrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.GetMonitorConfigV3VersionSecurity](../../models/operations/getmonitorconfigv3versionsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.GetMonitorConfigV3VersionResponse](../../models/operations/getmonitorconfigv3versionresponse.md)**


## get_notification_settings

Get notification settings for an org

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetNotificationSettingsRequest(
    org_id='mollitia',
)

res = s.internal.get_notification_settings(req, operations.GetNotificationSettingsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetNotificationSettingsRequest](../../models/operations/getnotificationsettingsrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.GetNotificationSettingsSecurity](../../models/operations/getnotificationsettingssecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.GetNotificationSettingsResponse](../../models/operations/getnotificationsettingsresponse.md)**


## get_organization

Returns various metadata about an organization

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetOrganizationRequest(
    org_id='laborum',
)

res = s.internal.get_organization(req, operations.GetOrganizationSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetOrganizationRequest](../../models/operations/getorganizationrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.GetOrganizationSecurity](../../models/operations/getorganizationsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.GetOrganizationResponse](../../models/operations/getorganizationresponse.md)**


## get_user

Get a user by their id.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetUserRequest(
    user_id='dolores',
)

res = s.internal.get_user(req, operations.GetUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetUserRequest](../../models/operations/getuserrequest.md)   | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `security`                                                               | [operations.GetUserSecurity](../../models/operations/getusersecurity.md) | :heavy_check_mark:                                                       | The security requirements to use for the request.                        |


### Response

**[operations.GetUserResponse](../../models/operations/getuserresponse.md)**


## get_user_by_email

Get a user by their email.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetUserByEmailRequest(
    email='Florian.Champlin60@gmail.com',
)

res = s.internal.get_user_by_email(req, operations.GetUserByEmailSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetUserByEmailRequest](../../models/operations/getuserbyemailrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GetUserByEmailSecurity](../../models/operations/getuserbyemailsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GetUserByEmailResponse](../../models/operations/getuserbyemailresponse.md)**


## hide_segments

Returns a list of segments that were hidden for a dataset.

        

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.HideSegmentsRequest(
    segments_list_request=shared.SegmentsListRequest(
        segments=[
            'minima',
            'excepturi',
        ],
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.internal.hide_segments(req, operations.HideSegmentsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.HideSegmentsRequest](../../models/operations/hidesegmentsrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.HideSegmentsSecurity](../../models/operations/hidesegmentssecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.HideSegmentsResponse](../../models/operations/hidesegmentsresponse.md)**


## list_api_keys

Returns the API key metadata for a given organization and user

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.ListAPIKeysRequest(
    org_id='org-123',
    user_id='user-123',
)

res = s.internal.list_api_keys(req, operations.ListAPIKeysSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListAPIKeysRequest](../../models/operations/listapikeysrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.ListAPIKeysSecurity](../../models/operations/listapikeyssecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.ListAPIKeysResponse](../../models/operations/listapikeysresponse.md)**


## list_jobs

List all of the jobs in a workspace.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.ListJobsRequest(
    org_id='accusantium',
    workspace_id='iure',
)

res = s.internal.list_jobs(req, operations.ListJobsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.ListJobsRequest](../../models/shared/listjobsrequest.md)           | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [operations.ListJobsSecurity](../../models/operations/listjobssecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |


### Response

**[operations.ListJobsResponse](../../models/operations/listjobsresponse.md)**


## list_monitor_config_v3_versions

List the monitor config document versions for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.ListMonitorConfigV3VersionsRequest(
    dataset_id='model-123',
    org_id='org-123',
)

res = s.internal.list_monitor_config_v3_versions(req, operations.ListMonitorConfigV3VersionsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.ListMonitorConfigV3VersionsRequest](../../models/operations/listmonitorconfigv3versionsrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.ListMonitorConfigV3VersionsSecurity](../../models/operations/listmonitorconfigv3versionssecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.ListMonitorConfigV3VersionsResponse](../../models/operations/listmonitorconfigv3versionsresponse.md)**


## list_organizations

Get a list of all of the organization ids.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()


res = s.internal.list_organizations(operations.ListOrganizationsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `security`                                                                                   | [operations.ListOrganizationsSecurity](../../models/operations/listorganizationssecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.ListOrganizationsResponse](../../models/operations/listorganizationsresponse.md)**


## list_segments

Returns a list of segments for the dataset.

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.ListSegmentsRequest(
    model_id='model-123',
    org_id='org-123',
)

res = s.internal.list_segments(req, operations.ListSegmentsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListSegmentsRequest](../../models/operations/listsegmentsrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.ListSegmentsSecurity](../../models/operations/listsegmentssecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.ListSegmentsResponse](../../models/operations/listsegmentsresponse.md)**


## ~~partially_update_org~~

Update some fields of an organization to non-null values, leaving all other existing values the same

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.PartiallyUpdateOrgRequest(
    request_body=operations.PartiallyUpdateOrgRequestBody(
        org_id='culpa',
    ),
    domain='acme.ai',
    name='ACME, Inc',
    notification_email_address='notifications@acme.ai',
    observatory_url='https://hub.whylabsapp.com',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.SUBSCRIPTION,
)

res = s.internal.partially_update_org(req, operations.PartiallyUpdateOrgSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PartiallyUpdateOrgRequest](../../models/operations/partiallyupdateorgrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.PartiallyUpdateOrgSecurity](../../models/operations/partiallyupdateorgsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.PartiallyUpdateOrgResponse](../../models/operations/partiallyupdateorgresponse.md)**


## partially_update_organization

Update some fields of an organization to non-null values, leaving all other existing values the same

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.PartiallyUpdateOrganizationRequest(
    domain='acme.ai',
    email_domains='acme.ai,acme.com',
    name='ACME, Inc',
    notification_email_address='notifications@acme.ai',
    observatory_url='https://hub.whylabsapp.com',
    org_id='sapiente',
    pager_duty_key='abc-def-ghi-jkl',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.FREE,
)

res = s.internal.partially_update_organization(req, operations.PartiallyUpdateOrganizationSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PartiallyUpdateOrganizationRequest](../../models/operations/partiallyupdateorganizationrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.PartiallyUpdateOrganizationSecurity](../../models/operations/partiallyupdateorganizationsecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.PartiallyUpdateOrganizationResponse](../../models/operations/partiallyupdateorganizationresponse.md)**


## post_monitor_config_validation_job

Create a monitor config validation job for all configs

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()


res = s.internal.post_monitor_config_validation_job(operations.PostMonitorConfigValidationJobSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                             | [operations.PostMonitorConfigValidationJobSecurity](../../models/operations/postmonitorconfigvalidationjobsecurity.md) | :heavy_check_mark:                                                                                                     | The security requirements to use for the request.                                                                      |


### Response

**[operations.PostMonitorConfigValidationJobResponse](../../models/operations/postmonitorconfigvalidationjobresponse.md)**


## provision_aws_marketplace_new_user

Create resources for a new user coming from AWS Marketplace

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.ProvisionNewMarketplaceUserRequest(
    customer_id_token='mollitia',
    email='Lorine_Crooks58@gmail.com',
    expect_existing=False,
    model_name='numquam',
    org_name='commodi',
)

res = s.internal.provision_aws_marketplace_new_user(req, operations.ProvisionAWSMarketplaceNewUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [shared.ProvisionNewMarketplaceUserRequest](../../models/shared/provisionnewmarketplaceuserrequest.md)                 | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `security`                                                                                                             | [operations.ProvisionAWSMarketplaceNewUserSecurity](../../models/operations/provisionawsmarketplacenewusersecurity.md) | :heavy_check_mark:                                                                                                     | The security requirements to use for the request.                                                                      |


### Response

**[operations.ProvisionAWSMarketplaceNewUserResponse](../../models/operations/provisionawsmarketplacenewuserresponse.md)**


## provision_databricks_connection

Create resources for a new user coming from Databricks

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.ProvisionDatabricksConnectionRequest(
    email='Jarred.Frami@yahoo.com',
    expect_existing_user=False,
    id='51aa52c3-f5ad-4019-9a1f-fe78f097b007',
)

res = s.internal.provision_databricks_connection(req, operations.ProvisionDatabricksConnectionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [shared.ProvisionDatabricksConnectionRequest](../../models/shared/provisiondatabricksconnectionrequest.md)           | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.ProvisionDatabricksConnectionSecurity](../../models/operations/provisiondatabricksconnectionsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.ProvisionDatabricksConnectionResponse](../../models/operations/provisiondatabricksconnectionresponse.md)**


## provision_new_user

Create the resources that a new user needs to use WhyLabs via the website.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.ProvisionNewUserRequest(
    email='Wilfrid.Carter@gmail.com',
    expect_existing=False,
    model_name='iusto',
    org_name='dicta',
    subscription_tier=shared.SubscriptionTier.AWS_MARKETPLACE,
)

res = s.internal.provision_new_user(req, operations.ProvisionNewUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.ProvisionNewUserRequest](../../models/shared/provisionnewuserrequest.md)           | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.ProvisionNewUserSecurity](../../models/operations/provisionnewusersecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.ProvisionNewUserResponse](../../models/operations/provisionnewuserresponse.md)**


## put_request_monitor_run_config

Put the RequestMonitorRun config into S3.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.PutRequestMonitorRunConfigRequest(
    request_body=operations.PutRequestMonitorRunConfigRequestBody(
        analyzer_ids=[
            'accusamus',
            'commodi',
        ],
        end_timestamp=1893456000000,
        overwrite=False,
        start_timestamp=1577836800000,
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.internal.put_request_monitor_run_config(req, operations.PutRequestMonitorRunConfigSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PutRequestMonitorRunConfigRequest](../../models/operations/putrequestmonitorrunconfigrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.PutRequestMonitorRunConfigSecurity](../../models/operations/putrequestmonitorrunconfigsecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.PutRequestMonitorRunConfigResponse](../../models/operations/putrequestmonitorrunconfigresponse.md)**


## refresh_connection

Refresh metadata for a workspace connection.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.RefreshConnectionRequest(
    org_id='repudiandae',
    workspace_id='quae',
)

res = s.internal.refresh_connection(req, operations.RefreshConnectionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.RefreshConnectionRequest](../../models/shared/refreshconnectionrequest.md)           | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.RefreshConnectionSecurity](../../models/operations/refreshconnectionsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.RefreshConnectionResponse](../../models/operations/refreshconnectionresponse.md)**


## register_databricks_connection

Register databricks metadata, temporarily storing it against a UUID so that it can be used to provision a databricks connection after email authentication

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.RegisterDatabricksConnectionRequest(
    access_token='ipsum',
    cloud_provider='quidem',
    connection_established=False,
    connection_id='molestias',
    demo=False,
    email='Samantha_Gleason@yahoo.com',
    free_trial=False,
    hostname='useful-bonnet.org',
    port=575947,
    workspace_id='veritatis',
    workspace_url='itaque',
)

res = s.internal.register_databricks_connection(req, operations.RegisterDatabricksConnectionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [shared.RegisterDatabricksConnectionRequest](../../models/shared/registerdatabricksconnectionrequest.md)           | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `security`                                                                                                         | [operations.RegisterDatabricksConnectionSecurity](../../models/operations/registerdatabricksconnectionsecurity.md) | :heavy_check_mark:                                                                                                 | The security requirements to use for the request.                                                                  |


### Response

**[operations.RegisterDatabricksConnectionResponse](../../models/operations/registerdatabricksconnectionresponse.md)**


## remove_membership_by_email

Removes membership in a given org from a user, using the user's email address.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.RemoveMembershipRequest(
    email='Emily_Altenwerth13@gmail.com',
    org_id='deserunt',
)

res = s.internal.remove_membership_by_email(req, operations.RemoveMembershipByEmailSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [shared.RemoveMembershipRequest](../../models/shared/removemembershiprequest.md)                         | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.RemoveMembershipByEmailSecurity](../../models/operations/removemembershipbyemailsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.RemoveMembershipByEmailResponse](../../models/operations/removemembershipbyemailresponse.md)**


## run_job

Run an existing job in a given databricks workspace.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.RunJobRequest(
    job_id=716327,
    org_id='quibusdam',
    workspace_id='labore',
)

res = s.internal.run_job(req, operations.RunJobSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.RunJobRequest](../../models/shared/runjobrequest.md)           | :heavy_check_mark:                                                     | The request object to use for the request.                             |
| `security`                                                             | [operations.RunJobSecurity](../../models/operations/runjobsecurity.md) | :heavy_check_mark:                                                     | The security requirements to use for the request.                      |


### Response

**[operations.RunJobResponse](../../models/operations/runjobresponse.md)**


## set_default_membership

Sets the organization that should be used when logging a user in

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.SetDefaultMembershipRequest(
    org_id='modi',
    user_id='qui',
)

res = s.internal.set_default_membership(req, operations.SetDefaultMembershipSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [shared.SetDefaultMembershipRequest](../../models/shared/setdefaultmembershiprequest.md)           | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.SetDefaultMembershipSecurity](../../models/operations/setdefaultmembershipsecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.SetDefaultMembershipResponse](../../models/operations/setdefaultmembershipresponse.md)**


## stripe_payment_endpoint

Endpoint for Stripe payment webhooks

### Example Usage

```python
import songbird


s = songbird.Songbird()

req = 'aliquid'

res = s.internal.stripe_payment_endpoint(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [str](../../models//.md)                   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.StripePaymentEndpointResponse](../../models/operations/stripepaymentendpointresponse.md)**


## update_connection

Update the connection metadata for a given org

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.UpdateConnectionRequest(
    changes=shared.UpdateConnectionChanges(
        connected=False,
        demo=False,
        org_id='cupiditate',
    ),
    org_id='quos',
    workspace_id='perferendis',
)

res = s.internal.update_connection(req, operations.UpdateConnectionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.UpdateConnectionRequest](../../models/shared/updateconnectionrequest.md)           | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.UpdateConnectionSecurity](../../models/operations/updateconnectionsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.UpdateConnectionResponse](../../models/operations/updateconnectionresponse.md)**


## update_membership_by_email

Updates the role in an membership, given the organization and the user's email address.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.UpdateMembershipRequest(
    email='Rhoda14@gmail.com',
    org_id='dolorum',
    role=shared.Role.MEMBER,
)

res = s.internal.update_membership_by_email(req, operations.UpdateMembershipByEmailSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [shared.UpdateMembershipRequest](../../models/shared/updatemembershiprequest.md)                         | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.UpdateMembershipByEmailSecurity](../../models/operations/updatemembershipbyemailsecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.UpdateMembershipByEmailResponse](../../models/operations/updatemembershipbyemailresponse.md)**


## update_notification_settings

Update notification settings for an org

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.UpdateNotificationSettingsRequest(
    notification_settings=shared.NotificationSettings(
        email_settings=shared.UberNotificationSchedule(
            cadence=shared.NotificationSqsMessageCadence.DAILY,
            day_of_week=shared.NotificationSettingsDay.THURSDAY,
            enabled=False,
            local24_hour_of_day=735194,
            local_minute_of_hour=288476,
            local_timezone='delectus',
        ),
        pager_duty_settings=shared.UberNotificationSchedule(
            cadence=shared.NotificationSqsMessageCadence.DAILY,
            day_of_week=shared.NotificationSettingsDay.MONDAY,
            enabled=False,
            local24_hour_of_day=756107,
            local_minute_of_hour=576157,
            local_timezone='aliquid',
        ),
        slack_settings=shared.UberNotificationSchedule(
            cadence=shared.NotificationSqsMessageCadence.WEEKLY,
            day_of_week=shared.NotificationSettingsDay.SATURDAY,
            enabled=False,
            local24_hour_of_day=572252,
            local_minute_of_hour=638921,
            local_timezone='dolor',
        ),
    ),
    org_id='debitis',
)

res = s.internal.update_notification_settings(req, operations.UpdateNotificationSettingsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.UpdateNotificationSettingsRequest](../../models/operations/updatenotificationsettingsrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.UpdateNotificationSettingsSecurity](../../models/operations/updatenotificationsettingssecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.UpdateNotificationSettingsResponse](../../models/operations/updatenotificationsettingsresponse.md)**


## ~~update_org~~

Update all fields of an existing organization

> :warning: **DEPRECATED**: this method will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.UpdateOrgRequest(
    request_body=operations.UpdateOrgRequestBody(
        org_id='a',
    ),
    domain='acme.ai',
    email_domains='acme.ai,acme.com',
    name='ACME, Inc',
    notification_email_address='notifications@acme.ai',
    observatory_url='https://hub.whylabsapp.com',
    pager_duty_key='abc-def-ghi-jkl',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.AWS_MARKETPLACE,
)

res = s.internal.update_org(req, operations.UpdateOrgSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.UpdateOrgRequest](../../models/operations/updateorgrequest.md)   | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `security`                                                                   | [operations.UpdateOrgSecurity](../../models/operations/updateorgsecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.UpdateOrgResponse](../../models/operations/updateorgresponse.md)**


## update_organization

Update all fields of an existing organization

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.UpdateOrganizationRequest(
    domain='acme.ai',
    email_domains='acme.ai,acme.com',
    name='ACME, Inc',
    notification_email_address='notifications@acme.ai',
    observatory_url='https://hub.whylabsapp.com',
    org_id='in',
    pager_duty_key='abc-def-ghi-jkl',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.PAID,
)

res = s.internal.update_organization(req, operations.UpdateOrganizationSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.UpdateOrganizationRequest](../../models/operations/updateorganizationrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.UpdateOrganizationSecurity](../../models/operations/updateorganizationsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.UpdateOrganizationResponse](../../models/operations/updateorganizationresponse.md)**


## update_user

Update a user.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.User(
    email='Wilford29@hotmail.com',
    preferences='cumque',
    user_id='facere',
)

res = s.internal.update_user(req, operations.UpdateUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.User](../../models/shared/user.md)                                     | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.UpdateUserSecurity](../../models/operations/updateusersecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.UpdateUserResponse](../../models/operations/updateuserresponse.md)**


## why_labs_search

WhyLabs Search

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.WhyLabsSearchRequest(
    query='ea',
)

res = s.internal.why_labs_search(req, operations.WhyLabsSearchSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.WhyLabsSearchRequest](../../models/operations/whylabssearchrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.WhyLabsSearchSecurity](../../models/operations/whylabssearchsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.WhyLabsSearchResponse](../../models/operations/whylabssearchresponse.md)**


## why_labs_search_indexing

WhyLabs Search Indexing

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.SearchIndexRequest(
    org_id='aliquid',
    type=shared.SearchIndexType.ENTITY_SCHEMA,
)

res = s.internal.why_labs_search_indexing(req, operations.WhyLabsSearchIndexingSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [shared.SearchIndexRequest](../../models/shared/searchindexrequest.md)                               | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.WhyLabsSearchIndexingSecurity](../../models/operations/whylabssearchindexingsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.WhyLabsSearchIndexingResponse](../../models/operations/whylabssearchindexingresponse.md)**

