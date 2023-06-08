# internal

### Available Operations

* [create_membership](#create_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [create_organization](#create_organization) - Create an organization
* [create_user](#create_user) - Create a user.
* [delete_organization](#delete_organization) - Delete an org
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
    created_by='fugit',
    default=False,
    email='Tyrel.Rosenbaum@yahoo.com',
    org_id='commodi',
    role=shared.Role.MEMBER,
)

res = s.internal.create_membership(req, operations.CreateMembershipSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

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

## create_user

Create a user.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.CreateUserRequest(
    email='Ona.Rippin@gmail.com',
)

res = s.internal.create_user(req, operations.CreateUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## delete_organization

Delete an org

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.DeleteOrganizationRequest(
    org_id='excepturi',
)

res = s.internal.delete_organization(req, operations.DeleteOrganizationSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## get_aws_marketplace_metadata

Get marketplace metadata for an org if any exists.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetAWSMarketplaceMetadataRequest(
    org_id='aspernatur',
)

res = s.internal.get_aws_marketplace_metadata(req, operations.GetAWSMarketplaceMetadataSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

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

## get_connection

Get the connection metadata for a given org

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.GetConnectionRequest(
    org_id='perferendis',
    workspace_id='ad',
)

res = s.internal.get_connection(req, operations.GetConnectionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## get_default_membership_for_email

Get the default membership for a user.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetDefaultMembershipForEmailRequest(
    email='Camden61@yahoo.com',
)

res = s.internal.get_default_membership_for_email(req, operations.GetDefaultMembershipForEmailSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## get_feature_flags

Get feature flags for the specified user/org

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetFeatureFlagsRequest(
    org_id='laboriosam',
    user_id='hic',
)

res = s.internal.get_feature_flags(req, operations.GetFeatureFlagsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## get_memberships

Get memberships for a user.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetMembershipsRequest(
    user_id='saepe',
)

res = s.internal.get_memberships(req, operations.GetMembershipsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## get_memberships_by_email

Get memberships for a user given that user's email address.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetMembershipsByEmailRequest(
    email='Issac.Hessel@hotmail.com',
)

res = s.internal.get_memberships_by_email(req, operations.GetMembershipsByEmailSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## get_memberships_by_org

Get memberships for an org.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetMembershipsByOrgRequest(
    org_id='saepe',
)

res = s.internal.get_memberships_by_org(req, operations.GetMembershipsByOrgSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

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

## get_notification_settings

Get notification settings for an org

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetNotificationSettingsRequest(
    org_id='quidem',
)

res = s.internal.get_notification_settings(req, operations.GetNotificationSettingsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## get_organization

Returns various metadata about an organization

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetOrganizationRequest(
    org_id='architecto',
)

res = s.internal.get_organization(req, operations.GetOrganizationSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## get_user

Get a user by their id.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetUserRequest(
    user_id='ipsa',
)

res = s.internal.get_user(req, operations.GetUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## get_user_by_email

Get a user by their email.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetUserByEmailRequest(
    email='Manuela.OHara21@hotmail.com',
)

res = s.internal.get_user_by_email(req, operations.GetUserByEmailSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

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

## list_jobs

List all of the jobs in a workspace.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.ListJobsRequest(
    org_id='corporis',
    workspace_id='explicabo',
)

res = s.internal.list_jobs(req, operations.ListJobsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

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
        org_id='nobis',
    ),
    domain='acme.ai',
    name='ACME, Inc',
    notification_email_address='notifications@acme.ai',
    observatory_url='https://hub.whylabsapp.com',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.PAID,
)

res = s.internal.partially_update_org(req, operations.PartiallyUpdateOrgSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

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
    org_id='omnis',
    pager_duty_key='abc-def-ghi-jkl',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.PAID,
)

res = s.internal.partially_update_organization(req, operations.PartiallyUpdateOrganizationSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

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

## provision_aws_marketplace_new_user

Create resources for a new user coming from AWS Marketplace

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.ProvisionNewMarketplaceUserRequest(
    customer_id_token='minima',
    email='Alisa_Kessler@yahoo.com',
    expect_existing=False,
    model_name='sapiente',
    org_name='architecto',
)

res = s.internal.provision_aws_marketplace_new_user(req, operations.ProvisionAWSMarketplaceNewUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## provision_databricks_connection

Create resources for a new user coming from Databricks

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.ProvisionDatabricksConnectionRequest(
    email='Cordie99@yahoo.com',
    expect_existing_user=False,
    id='a9467739-251a-4a52-83f5-ad019da1ffe7',
)

res = s.internal.provision_databricks_connection(req, operations.ProvisionDatabricksConnectionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## provision_new_user

Create the resources that a new user needs to use WhyLabs via the website.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.ProvisionNewUserRequest(
    email='Whitney.Bednar@yahoo.com',
    expect_existing=False,
    model_name='cum',
    org_name='perferendis',
    subscription_tier=shared.SubscriptionTier.FREE,
)

res = s.internal.provision_new_user(req, operations.ProvisionNewUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

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
            'ut',
            'maiores',
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

## refresh_connection

Refresh metadata for a workspace connection.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.RefreshConnectionRequest(
    org_id='dicta',
    workspace_id='corporis',
)

res = s.internal.refresh_connection(req, operations.RefreshConnectionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## register_databricks_connection

Register databricks metadata, temporarily storing it against a UUID so that it can be used to provision a databricks connection after email authentication

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.RegisterDatabricksConnectionRequest(
    access_token='dolore',
    cloud_provider='iusto',
    connection_established=False,
    connection_id='dicta',
    demo=False,
    email='Emilie_Thompson@hotmail.com',
    free_trial=False,
    hostname='beautiful-crab.net',
    port=565189,
    workspace_id='excepturi',
    workspace_url='pariatur',
)

res = s.internal.register_databricks_connection(req, operations.RegisterDatabricksConnectionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## remove_membership_by_email

Removes membership in a given org from a user, using the user's email address.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.RemoveMembershipRequest(
    email='Johanna.Ledner92@gmail.com',
    org_id='sint',
)

res = s.internal.remove_membership_by_email(req, operations.RemoveMembershipByEmailSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## run_job

Run an existing job in a given databricks workspace.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.RunJobRequest(
    job_id=83112,
    org_id='itaque',
    workspace_id='incidunt',
)

res = s.internal.run_job(req, operations.RunJobSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## set_default_membership

Sets the organization that should be used when logging a user in

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.SetDefaultMembershipRequest(
    org_id='enim',
    user_id='consequatur',
)

res = s.internal.set_default_membership(req, operations.SetDefaultMembershipSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## stripe_payment_endpoint

Endpoint for Stripe payment webhooks

### Example Usage

```python
import songbird


s = songbird.Songbird()

req = 'est'

res = s.internal.stripe_payment_endpoint(req)

if res.status_code == 200:
    # handle response
```

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
        org_id='quibusdam',
    ),
    org_id='explicabo',
    workspace_id='deserunt',
)

res = s.internal.update_connection(req, operations.UpdateConnectionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## update_membership_by_email

Updates the role in an membership, given the organization and the user's email address.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.UpdateMembershipRequest(
    email='Ron18@hotmail.com',
    org_id='aliquid',
    role=shared.Role.MEMBER,
)

res = s.internal.update_membership_by_email(req, operations.UpdateMembershipByEmailSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

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
            cadence=shared.NotificationSqsMessageCadence.WEEKLY,
            day_of_week=shared.NotificationSettingsDay.SUNDAY,
            enabled=False,
            local24_hour_of_day=164940,
            local_minute_of_hour=828940,
            local_timezone='ipsam',
        ),
        pager_duty_settings=shared.UberNotificationSchedule(
            cadence=shared.NotificationSqsMessageCadence.HOURLY,
            day_of_week=shared.NotificationSettingsDay.MONDAY,
            enabled=False,
            local24_hour_of_day=677817,
            local_minute_of_hour=569618,
            local_timezone='tempora',
        ),
        slack_settings=shared.UberNotificationSchedule(
            cadence=shared.NotificationSqsMessageCadence.WEEKLY,
            day_of_week=shared.NotificationSettingsDay.FRIDAY,
            enabled=False,
            local24_hour_of_day=288476,
            local_minute_of_hour=962189,
            local_timezone='eum',
        ),
    ),
    org_id='non',
)

res = s.internal.update_notification_settings(req, operations.UpdateNotificationSettingsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

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
        org_id='eligendi',
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
    org_id='aliquid',
    pager_duty_key='abc-def-ghi-jkl',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.AWS_MARKETPLACE,
)

res = s.internal.update_organization(req, operations.UpdateOrganizationSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## update_user

Update a user.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.User(
    email='Kianna89@hotmail.com',
    preferences='a',
    user_id='dolorum',
)

res = s.internal.update_user(req, operations.UpdateUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## why_labs_search

WhyLabs Search

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.WhyLabsSearchRequest(
    query='in',
)

res = s.internal.why_labs_search(req, operations.WhyLabsSearchSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## why_labs_search_indexing

WhyLabs Search Indexing

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.SearchIndexRequest(
    org_id='in',
    type=shared.SearchIndexType.MONITOR_CONFIG,
)

res = s.internal.why_labs_search_indexing(req, operations.WhyLabsSearchIndexingSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```
