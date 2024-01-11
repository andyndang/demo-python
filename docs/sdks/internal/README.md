# Internal
(*internal*)

### Available Operations

* [activate_azure_subscription](#activate_azure_subscription) - Endpoint to activate Azure Marketplace subscriptions
* [azure_marketplace_webhook](#azure_marketplace_webhook) - Endpoint for Azure Marketplace webhooks
* [create_account_user](#create_account_user) - Create an account user
* [create_membership](#create_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [create_organization](#create_organization) - Create an organization
* [create_user](#create_user) - Create a user.
* [delete_account_user](#delete_account_user) - Delete account user
* [delete_organization](#delete_organization) - Delete an org
* [generate_report](#generate_report) - Generate an admin report
* [get_aws_marketplace_metadata](#get_aws_marketplace_metadata) - Get marketplace metadata for an org if any exists.
* [get_account_memberships](#get_account_memberships) - Get memberships in an account
* [get_account_user_by_email](#get_account_user_by_email) - Get account user by email
* [get_account_user_by_id](#get_account_user_by_id) - Get account user by user_id
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
* [get_organization_subscriptions](#get_organization_subscriptions) - Get organization subscription details
* [get_user](#get_user) - Get a user by their id.
* [get_user_by_email](#get_user_by_email) - Get a user by their email.
* [hide_segments](#hide_segments) - Hides a list of segments
* [list_account_users](#list_account_users) - List users in an account
* [list_api_keys](#list_api_keys) - List API key metadata for a given organization and user
* [list_jobs](#list_jobs) - List all of the jobs in a workspace.
* [list_managed_organizations](#list_managed_organizations) - List managed organizations for a parent organization
* [list_monitor_config_v3_versions](#list_monitor_config_v3_versions) - List the monitor config document versions for a given dataset.
* [list_organizations](#list_organizations) - Get a list of all of the organization ids.
* [~~partially_update_org~~](#partially_update_org) - Update some fields of an organization to non-null values :warning: **Deprecated**
* [partially_update_organization](#partially_update_organization) - Update some fields of an organization to non-null values
* [patch_organization_memberships](#patch_organization_memberships) - Add or delete memberships in a specific role and managed organization
* [post_monitor_config_validation_job](#post_monitor_config_validation_job) - Create a monitor config validation job for all configs
* [provision_aws_marketplace_new_user](#provision_aws_marketplace_new_user) - Create resources for a new user coming from AWS Marketplace
* [provision_databricks_connection](#provision_databricks_connection) - Create resources for a new user coming from Databricks
* [provision_new_user](#provision_new_user) - Create the resources that a new user needs to use WhyLabs via the website.
* [put_organization_memberships](#put_organization_memberships) - Replace the memberships in a specific role and managed organization
* [put_request_monitor_run_config](#put_request_monitor_run_config) - Put the RequestMonitorRun config into S3.
* [refresh_connection](#refresh_connection) - Refresh metadata for a workspace connection.
* [register_databricks_connection](#register_databricks_connection) - Register databricks metadata, temporarily storing it against a UUID so that it can be used to provision a databricks connection after email authentication
* [remove_membership_by_email](#remove_membership_by_email) - Removes membership in a given org from a user, using the user's email address.
* [run_job](#run_job) - Run an existing job in a given databricks workspace.
* [set_default_membership](#set_default_membership) - Sets the organization that should be used when logging a user in
* [stripe_payment_endpoint](#stripe_payment_endpoint) - Endpoint for Stripe payment webhooks
* [update_account_user](#update_account_user) - Update account user
* [update_connection](#update_connection) - Update the connection metadata for a given org
* [update_membership_by_email](#update_membership_by_email) - Updates the role in an membership
* [update_notification_settings](#update_notification_settings) - Update notification settings for an org
* [~~update_org~~](#update_org) - Update an existing organization :warning: **Deprecated**
* [update_organization](#update_organization) - Update an existing organization
* [update_user](#update_user) - Update a user.
* [why_labs_search](#why_labs_search) - WhyLabs Search
* [why_labs_search_indexing](#why_labs_search_indexing) - WhyLabs Search Indexing

## activate_azure_subscription

Endpoint to activate Azure Marketplace subscriptions

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.ActivateAzureSubscriptionRequest(
    email='Travis_Cummings7@gmail.com',
    marketplace_token='string',
    org_name='string',
)

res = s.internal.activate_azure_subscription(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [shared.ActivateAzureSubscriptionRequest](../../models/shared/activateazuresubscriptionrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.ActivateAzureSubscriptionResponse](../../models/operations/activateazuresubscriptionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## azure_marketplace_webhook

Endpoint for Azure Marketplace webhooks

### Example Usage

```python
import songbird

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = 'string'

res = s.internal.azure_marketplace_webhook(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [str](../../models/.md)                    | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.AzureMarketplaceWebhookResponse](../../models/operations/azuremarketplacewebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_account_user

Create an account user

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.CreateAccountUserRequest(
    create_account_user_request=shared.CreateAccountUserRequest(
        email='Jason_Skiles63@yahoo.com',
    ),
    org_id='org-123',
)

res = s.internal.create_account_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateAccountUserRequest](../../models/operations/createaccountuserrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateAccountUserResponse](../../models/operations/createaccountuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_membership

Create a membership for a user, making them apart of an organization. Uses the user's current email address.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.AddMembershipRequest(
    email='Willie1@gmail.com',
    org_id='string',
    role=shared.Role.ADMIN,
)

res = s.internal.create_membership(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.AddMembershipRequest](../../models/shared/addmembershiprequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CreateMembershipResponse](../../models/operations/createmembershipresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_organization

Create an organization

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.CreateOrganizationRequest(
    domain='acme.ai',
    email_domains='acme.ai,acme.com',
    name='ACME, Inc',
    notification_email_address='notifications@acme.ai',
    observatory_url='https://hub.whylabsapp.com',
    override_id='org-123',
    pager_duty_key='abc-def-ghi-jkl',
    parent_org_id='org-123',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    storage_bucket_override='https://s3.us-west-2.amazonaws.com/whylabs-public/',
)

res = s.internal.create_organization(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateOrganizationRequest](../../models/operations/createorganizationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateOrganizationResponse](../../models/operations/createorganizationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_user

Create a user.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.CreateUserRequest(
    email='Richie.Kuhic95@yahoo.com',
)

res = s.internal.create_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.CreateUserRequest](../../models/shared/createuserrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateUserResponse](../../models/operations/createuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_account_user

Delete an account user's details

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.DeleteAccountUserRequest(
    org_id='org-123',
    user_id='user-123',
)

res = s.internal.delete_account_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteAccountUserRequest](../../models/operations/deleteaccountuserrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.DeleteAccountUserResponse](../../models/operations/deleteaccountuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_organization

Delete an org

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.DeleteOrganizationRequest(
    org_id='string',
)

res = s.internal.delete_organization(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.DeleteOrganizationRequest](../../models/operations/deleteorganizationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.DeleteOrganizationResponse](../../models/operations/deleteorganizationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## generate_report

Generate an admin report

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GenerateReportRequest(
    report_type=shared.AdminReportType.SESSIONS,
)

res = s.internal.generate_report(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GenerateReportRequest](../../models/operations/generatereportrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GenerateReportResponse](../../models/operations/generatereportresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_aws_marketplace_metadata

Get marketplace metadata for an org if any exists.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetAWSMarketplaceMetadataRequest(
    org_id='string',
)

res = s.internal.get_aws_marketplace_metadata(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetAWSMarketplaceMetadataRequest](../../models/operations/getawsmarketplacemetadatarequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetAWSMarketplaceMetadataResponse](../../models/operations/getawsmarketplacemetadataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_account_memberships

Get memberships in the account organization and any managed organizations

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetAccountMembershipsRequest(
    managed_org_id='org-123',
    org_id='org-123',
    user_id='user-123',
)

res = s.internal.get_account_memberships(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAccountMembershipsRequest](../../models/operations/getaccountmembershipsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetAccountMembershipsResponse](../../models/operations/getaccountmembershipsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_account_user_by_email

Get account user by email

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetAccountUserByEmailRequest(
    email='user@whylabs.ai',
    org_id='org-123',
)

res = s.internal.get_account_user_by_email(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAccountUserByEmailRequest](../../models/operations/getaccountuserbyemailrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetAccountUserByEmailResponse](../../models/operations/getaccountuserbyemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_account_user_by_id

Get account user by user_id

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetAccountUserByIDRequest(
    org_id='org-123',
    user_id='user-123',
)

res = s.internal.get_account_user_by_id(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAccountUserByIDRequest](../../models/operations/getaccountuserbyidrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetAccountUserByIDResponse](../../models/operations/getaccountuserbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_key

Get an api key by its id

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetAPIKeyRequest(
    key_id='fh4dUNV3WQ',
    org_id='org-123',
)

res = s.internal.get_api_key(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetAPIKeyRequest](../../models/operations/getapikeyrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetAPIKeyResponse](../../models/operations/getapikeyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_connection

Get the connection metadata for a given org

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.GetConnectionRequest()

res = s.internal.get_connection(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.GetConnectionRequest](../../models/shared/getconnectionrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetConnectionResponse](../../models/operations/getconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_default_membership_for_email

Get the default membership for a user.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetDefaultMembershipForEmailRequest(
    email='Jake.Dibbert@hotmail.com',
)

res = s.internal.get_default_membership_for_email(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetDefaultMembershipForEmailRequest](../../models/operations/getdefaultmembershipforemailrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetDefaultMembershipForEmailResponse](../../models/operations/getdefaultmembershipforemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_feature_flags

Get feature flags for the specified user/org

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetFeatureFlagsRequest(
    org_id='string',
    user_id='string',
)

res = s.internal.get_feature_flags(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetFeatureFlagsRequest](../../models/operations/getfeatureflagsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetFeatureFlagsResponse](../../models/operations/getfeatureflagsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_memberships

Get memberships for a user.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetMembershipsRequest(
    user_id='string',
)

res = s.internal.get_memberships(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetMembershipsRequest](../../models/operations/getmembershipsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetMembershipsResponse](../../models/operations/getmembershipsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_memberships_by_email

Get memberships for a user given that user's email address.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetMembershipsByEmailRequest(
    email='Giles.Grady@gmail.com',
)

res = s.internal.get_memberships_by_email(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetMembershipsByEmailRequest](../../models/operations/getmembershipsbyemailrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetMembershipsByEmailResponse](../../models/operations/getmembershipsbyemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_memberships_by_org

Get memberships for an org.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetMembershipsByOrgRequest(
    org_id='string',
)

res = s.internal.get_memberships_by_org(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetMembershipsByOrgRequest](../../models/operations/getmembershipsbyorgrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetMembershipsByOrgResponse](../../models/operations/getmembershipsbyorgresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monitor_config_v3_version

Get the monitor config document version for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetMonitorConfigV3VersionRequest(
    dataset_id='model-123',
    org_id='org-123',
    version_id='4920545486e2a4cdf0f770c09748e663',
)

res = s.internal.get_monitor_config_v3_version(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetMonitorConfigV3VersionRequest](../../models/operations/getmonitorconfigv3versionrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetMonitorConfigV3VersionResponse](../../models/operations/getmonitorconfigv3versionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_notification_settings

Get notification settings for an org

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetNotificationSettingsRequest(
    org_id='string',
)

res = s.internal.get_notification_settings(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetNotificationSettingsRequest](../../models/operations/getnotificationsettingsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetNotificationSettingsResponse](../../models/operations/getnotificationsettingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_organization

Returns various metadata about an organization

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetOrganizationRequest(
    org_id='string',
)

res = s.internal.get_organization(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetOrganizationRequest](../../models/operations/getorganizationrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetOrganizationResponse](../../models/operations/getorganizationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_organization_subscriptions

Get organization subscription details

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetOrganizationSubscriptionsRequest(
    org_id='string',
)

res = s.internal.get_organization_subscriptions(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetOrganizationSubscriptionsRequest](../../models/operations/getorganizationsubscriptionsrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetOrganizationSubscriptionsResponse](../../models/operations/getorganizationsubscriptionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_user

Get a user by their id.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetUserRequest(
    user_id='string',
)

res = s.internal.get_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetUserRequest](../../models/operations/getuserrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetUserResponse](../../models/operations/getuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_user_by_email

Get a user by their email.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetUserByEmailRequest(
    email='Chauncey12@yahoo.com',
)

res = s.internal.get_user_by_email(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetUserByEmailRequest](../../models/operations/getuserbyemailrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetUserByEmailResponse](../../models/operations/getuserbyemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## hide_segments

Returns a list of segments that were hidden for a dataset.

        

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.HideSegmentsRequest(
    segments_list_request=shared.SegmentsListRequest(
        segments=[
            'string',
        ],
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.internal.hide_segments(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.HideSegmentsRequest](../../models/operations/hidesegmentsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.HideSegmentsResponse](../../models/operations/hidesegmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_account_users

List users in the account organization and any managed organizations

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.ListAccountUsersRequest(
    org_id='org-123',
)

res = s.internal.list_account_users(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListAccountUsersRequest](../../models/operations/listaccountusersrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListAccountUsersResponse](../../models/operations/listaccountusersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_api_keys

Returns the API key metadata for a given organization and user

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.ListAPIKeysRequest(
    org_id='org-123',
    user_id='user-123',
)

res = s.internal.list_api_keys(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListAPIKeysRequest](../../models/operations/listapikeysrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListAPIKeysResponse](../../models/operations/listapikeysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_jobs

List all of the jobs in a workspace.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.ListJobsRequest()

res = s.internal.list_jobs(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [shared.ListJobsRequest](../../models/shared/listjobsrequest.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.ListJobsResponse](../../models/operations/listjobsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_managed_organizations

List managed organizations for a parent organization

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.ListManagedOrganizationsRequest(
    org_id='org-123',
)

res = s.internal.list_managed_organizations(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListManagedOrganizationsRequest](../../models/operations/listmanagedorganizationsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.ListManagedOrganizationsResponse](../../models/operations/listmanagedorganizationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_monitor_config_v3_versions

List the monitor config document versions for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.ListMonitorConfigV3VersionsRequest(
    dataset_id='model-123',
    org_id='org-123',
)

res = s.internal.list_monitor_config_v3_versions(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.ListMonitorConfigV3VersionsRequest](../../models/operations/listmonitorconfigv3versionsrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.ListMonitorConfigV3VersionsResponse](../../models/operations/listmonitorconfigv3versionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_organizations

Get a list of all of the organization ids.

### Example Usage

```python
import songbird

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.list_organizations()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.ListOrganizationsResponse](../../models/operations/listorganizationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## ~~partially_update_org~~

Update some fields of an organization to non-null values, leaving all other existing values the same

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.PartiallyUpdateOrgRequest(
    request_body=operations.PartiallyUpdateOrgRequestBody(),
    domain='acme.ai',
    name='ACME, Inc',
    notification_email_address='notifications@acme.ai',
    observatory_url='https://hub.whylabsapp.com',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
)

res = s.internal.partially_update_org(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.PartiallyUpdateOrgRequest](../../models/operations/partiallyupdateorgrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.PartiallyUpdateOrgResponse](../../models/operations/partiallyupdateorgresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## partially_update_organization

Update some fields of an organization to non-null values, leaving all other existing values the same

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.PartiallyUpdateOrganizationRequest(
    domain='acme.ai',
    email_domains='acme.ai,acme.com',
    name='ACME, Inc',
    notification_email_address='notifications@acme.ai',
    observatory_url='https://hub.whylabsapp.com',
    org_id='string',
    pager_duty_key='abc-def-ghi-jkl',
    parent_org_id='abc-def-ghi-jkl',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    storage_bucket_override='https://s3.us-west-2.amazonaws.com/whylabs-public/',
)

res = s.internal.partially_update_organization(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PartiallyUpdateOrganizationRequest](../../models/operations/partiallyupdateorganizationrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PartiallyUpdateOrganizationResponse](../../models/operations/partiallyupdateorganizationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_organization_memberships

Add or delete all of the memberships in a specific role and managed organization

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.PatchOrganizationMembershipsRequest(
    patch_account_memberships_request=shared.PatchAccountMembershipsRequest(
        user_ids_to_add=[
            'string',
        ],
        user_ids_to_delete=[
            'string',
        ],
    ),
    managed_org_id='org-123',
    org_id='org-123',
    role=shared.Role.VIEWER,
)

res = s.internal.patch_organization_memberships(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PatchOrganizationMembershipsRequest](../../models/operations/patchorganizationmembershipsrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PatchOrganizationMembershipsResponse](../../models/operations/patchorganizationmembershipsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_monitor_config_validation_job

Create a monitor config validation job for all configs

### Example Usage

```python
import songbird

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.internal.post_monitor_config_validation_job()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.PostMonitorConfigValidationJobResponse](../../models/operations/postmonitorconfigvalidationjobresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## provision_aws_marketplace_new_user

Create resources for a new user coming from AWS Marketplace

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.ProvisionNewMarketplaceUserRequest(
    customer_id_token='string',
    email='Karina72@yahoo.com',
    model_name='string',
    org_name='string',
)

res = s.internal.provision_aws_marketplace_new_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [shared.ProvisionNewMarketplaceUserRequest](../../models/shared/provisionnewmarketplaceuserrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.ProvisionAWSMarketplaceNewUserResponse](../../models/operations/provisionawsmarketplacenewuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## provision_databricks_connection

Create resources for a new user coming from Databricks

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.ProvisionDatabricksConnectionRequest(
    email='Alexandria_Ernser@yahoo.com',
    expect_existing_user=False,
    id='<ID>',
)

res = s.internal.provision_databricks_connection(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [shared.ProvisionDatabricksConnectionRequest](../../models/shared/provisiondatabricksconnectionrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.ProvisionDatabricksConnectionResponse](../../models/operations/provisiondatabricksconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## provision_new_user

Create the resources that a new user needs to use WhyLabs via the website.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.ProvisionNewUserRequest(
    email='Alec40@hotmail.com',
    model_name='string',
    org_name='string',
    subscription_tier=shared.SubscriptionTier.PAID,
)

res = s.internal.provision_new_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.ProvisionNewUserRequest](../../models/shared/provisionnewuserrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ProvisionNewUserResponse](../../models/operations/provisionnewuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_organization_memberships

Replace all of the memberships in a specific role and managed organization

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.PutOrganizationMembershipsRequest(
    put_account_memberships_request=shared.PutAccountMembershipsRequest(
        user_ids=[
            'string',
        ],
    ),
    managed_org_id='org-123',
    org_id='org-123',
    role=shared.Role.VIEWER,
)

res = s.internal.put_organization_memberships(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PutOrganizationMembershipsRequest](../../models/operations/putorganizationmembershipsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PutOrganizationMembershipsResponse](../../models/operations/putorganizationmembershipsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_request_monitor_run_config

Put the RequestMonitorRun config into S3.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.PutRequestMonitorRunConfigRequest(
    request_body=operations.PutRequestMonitorRunConfigRequestBody(
        analyzer_ids=[
            'd',
            'r',
            'i',
            'f',
            't',
            '-',
            'a',
            'n',
            'a',
            'l',
            'y',
            'z',
            'e',
            'r',
        ],
        end_timestamp=1893456000000,
        start_timestamp=1577836800000,
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.internal.put_request_monitor_run_config(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PutRequestMonitorRunConfigRequest](../../models/operations/putrequestmonitorrunconfigrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PutRequestMonitorRunConfigResponse](../../models/operations/putrequestmonitorrunconfigresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## refresh_connection

Refresh metadata for a workspace connection.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.RefreshConnectionRequest()

res = s.internal.refresh_connection(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.RefreshConnectionRequest](../../models/shared/refreshconnectionrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.RefreshConnectionResponse](../../models/operations/refreshconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## register_databricks_connection

Register databricks metadata, temporarily storing it against a UUID so that it can be used to provision a databricks connection after email authentication

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.RegisterDatabricksConnectionRequest(
    access_token='string',
    cloud_provider='string',
    connection_id='string',
    demo=False,
    email='Kim53@yahoo.com',
    hostname='glistening-mobile.com',
    port=797817,
    workspace_id='string',
    workspace_url='string',
)

res = s.internal.register_databricks_connection(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [shared.RegisterDatabricksConnectionRequest](../../models/shared/registerdatabricksconnectionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.RegisterDatabricksConnectionResponse](../../models/operations/registerdatabricksconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## remove_membership_by_email

Removes membership in a given org from a user, using the user's email address.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.RemoveMembershipRequest(
    email='Shaun79@gmail.com',
    org_id='string',
)

res = s.internal.remove_membership_by_email(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.RemoveMembershipRequest](../../models/shared/removemembershiprequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.RemoveMembershipByEmailResponse](../../models/operations/removemembershipbyemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## run_job

Run an existing job in a given databricks workspace.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.RunJobRequest(
    job_id=353621,
)

res = s.internal.run_job(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.RunJobRequest](../../models/shared/runjobrequest.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.RunJobResponse](../../models/operations/runjobresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## set_default_membership

Sets the organization that should be used when logging a user in

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.SetDefaultMembershipRequest(
    org_id='string',
    user_id='string',
)

res = s.internal.set_default_membership(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.SetDefaultMembershipRequest](../../models/shared/setdefaultmembershiprequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.SetDefaultMembershipResponse](../../models/operations/setdefaultmembershipresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## stripe_payment_endpoint

Endpoint for Stripe payment webhooks

### Example Usage

```python
import songbird

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = 'string'

res = s.internal.stripe_payment_endpoint(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [str](../../models/.md)                    | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.StripePaymentEndpointResponse](../../models/operations/stripepaymentendpointresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_account_user

Update an account user's details

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.UpdateAccountUserRequest(
    update_account_user_request=shared.UpdateAccountUserRequest(),
    org_id='org-123',
    user_id='user-123',
)

res = s.internal.update_account_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateAccountUserRequest](../../models/operations/updateaccountuserrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpdateAccountUserResponse](../../models/operations/updateaccountuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_connection

Update the connection metadata for a given org

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.UpdateConnectionRequest(
    changes=shared.UpdateConnectionChanges(),
)

res = s.internal.update_connection(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.UpdateConnectionRequest](../../models/shared/updateconnectionrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateConnectionResponse](../../models/operations/updateconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_membership_by_email

Updates the role in an membership, given the organization and the user's email address.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.UpdateMembershipRequest(
    email='Minnie42@hotmail.com',
    org_id='string',
    role=shared.Role.VIEWER,
)

res = s.internal.update_membership_by_email(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.UpdateMembershipRequest](../../models/shared/updatemembershiprequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateMembershipByEmailResponse](../../models/operations/updatemembershipbyemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_notification_settings

Update notification settings for an org

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.UpdateNotificationSettingsRequest(
    notification_settings=shared.NotificationSettings(
        email_settings=shared.UberNotificationSchedule(
            cadence=shared.NotificationSqsMessageCadence.HOURLY,
            enabled=False,
        ),
        pager_duty_settings=shared.UberNotificationSchedule(
            cadence=shared.NotificationSqsMessageCadence.DAILY,
            enabled=False,
        ),
        slack_settings=shared.UberNotificationSchedule(
            cadence=shared.NotificationSqsMessageCadence.INDIVIDUAL,
            enabled=False,
        ),
    ),
    org_id='string',
)

res = s.internal.update_notification_settings(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.UpdateNotificationSettingsRequest](../../models/operations/updatenotificationsettingsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.UpdateNotificationSettingsResponse](../../models/operations/updatenotificationsettingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## ~~update_org~~

Update all fields of an existing organization

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.UpdateOrgRequest(
    request_body=operations.UpdateOrgRequestBody(),
    domain='acme.ai',
    email_domains='acme.ai,acme.com',
    name='ACME, Inc',
    notification_email_address='notifications@acme.ai',
    observatory_url='https://hub.whylabsapp.com',
    pager_duty_key='abc-def-ghi-jkl',
    parent_org_id='org-123',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
)

res = s.internal.update_org(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.UpdateOrgRequest](../../models/operations/updateorgrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.UpdateOrgResponse](../../models/operations/updateorgresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_organization

Update all fields of an existing organization

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.UpdateOrganizationRequest(
    domain='acme.ai',
    email_domains='acme.ai,acme.com',
    name='ACME, Inc',
    notification_email_address='notifications@acme.ai',
    observatory_url='https://hub.whylabsapp.com',
    org_id='string',
    pager_duty_key='abc-def-ghi-jkl',
    parent_org_id='org-123',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    storage_bucket_override='https://s3.us-west-2.amazonaws.com/whylabs-public/',
)

res = s.internal.update_organization(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateOrganizationRequest](../../models/operations/updateorganizationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UpdateOrganizationResponse](../../models/operations/updateorganizationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_user

Update a user.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.User(
    email='Madison.Jacobi47@yahoo.com',
    user_id='string',
)

res = s.internal.update_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.User](../../models/shared/user.md) | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.UpdateUserResponse](../../models/operations/updateuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## why_labs_search

WhyLabs Search

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.WhyLabsSearchRequest(
    query='string',
)

res = s.internal.why_labs_search(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.WhyLabsSearchRequest](../../models/operations/whylabssearchrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.WhyLabsSearchResponse](../../models/operations/whylabssearchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## why_labs_search_indexing

WhyLabs Search Indexing

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.SearchIndexRequest()

res = s.internal.why_labs_search_indexing(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.SearchIndexRequest](../../models/shared/searchindexrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.WhyLabsSearchIndexingResponse](../../models/operations/whylabssearchindexingresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
