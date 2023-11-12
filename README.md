# Songbird

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/andyndang/demo-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
### Example

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="",
)

req = operations.CreateAccountUserRequest(
    create_account_user_request=shared.CreateAccountUserRequest(
        email='Jason_Skiles63@yahoo.com',
    ),
    org_id='org-123',
)

res = s.account.create_account_user(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [account](docs/sdks/account/README.md)

* [create_account_user](docs/sdks/account/README.md#create_account_user) - Create an account user
* [delete_account_user](docs/sdks/account/README.md#delete_account_user) - Delete account user
* [get_account_memberships](docs/sdks/account/README.md#get_account_memberships) - Get memberships in an account
* [get_account_user_by_email](docs/sdks/account/README.md#get_account_user_by_email) - Get account user by email
* [get_account_user_by_id](docs/sdks/account/README.md#get_account_user_by_id) - Get account user by user_id
* [list_account_users](docs/sdks/account/README.md#list_account_users) - List users in an account
* [list_managed_organizations](docs/sdks/account/README.md#list_managed_organizations) - List managed organizations for a parent organization
* [patch_organization_memberships](docs/sdks/account/README.md#patch_organization_memberships) - Add or delete memberships in a specific role and managed organization
* [put_organization_memberships](docs/sdks/account/README.md#put_organization_memberships) - Replace the memberships in a specific role and managed organization
* [update_account_user](docs/sdks/account/README.md#update_account_user) - Update account user

### [internal](docs/sdks/internal/README.md)

* [create_account_user](docs/sdks/internal/README.md#create_account_user) - Create an account user
* [create_membership](docs/sdks/internal/README.md#create_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [create_organization](docs/sdks/internal/README.md#create_organization) - Create an organization
* [create_user](docs/sdks/internal/README.md#create_user) - Create a user.
* [delete_account_user](docs/sdks/internal/README.md#delete_account_user) - Delete account user
* [delete_organization](docs/sdks/internal/README.md#delete_organization) - Delete an org
* [generate_report](docs/sdks/internal/README.md#generate_report) - Generate an admin report
* [get_aws_marketplace_metadata](docs/sdks/internal/README.md#get_aws_marketplace_metadata) - Get marketplace metadata for an org if any exists.
* [get_account_memberships](docs/sdks/internal/README.md#get_account_memberships) - Get memberships in an account
* [get_account_user_by_email](docs/sdks/internal/README.md#get_account_user_by_email) - Get account user by email
* [get_account_user_by_id](docs/sdks/internal/README.md#get_account_user_by_id) - Get account user by user_id
* [get_api_key](docs/sdks/internal/README.md#get_api_key) - Get an api key by its id
* [get_connection](docs/sdks/internal/README.md#get_connection) - Get the connection metadata for a given org
* [get_default_membership_for_email](docs/sdks/internal/README.md#get_default_membership_for_email) - Get the default membership for a user.
* [get_feature_flags](docs/sdks/internal/README.md#get_feature_flags) - Get feature flags for the specified user/org
* [get_memberships](docs/sdks/internal/README.md#get_memberships) - Get memberships for a user.
* [get_memberships_by_email](docs/sdks/internal/README.md#get_memberships_by_email) - Get memberships for a user given that user's email address.
* [get_memberships_by_org](docs/sdks/internal/README.md#get_memberships_by_org) - Get memberships for an org.
* [get_monitor_config_v3_version](docs/sdks/internal/README.md#get_monitor_config_v3_version) - Get the monitor config document version for a given dataset.
* [get_notification_settings](docs/sdks/internal/README.md#get_notification_settings) - Get notification settings for an org
* [get_organization](docs/sdks/internal/README.md#get_organization) - Get the metadata about an organization.
* [get_organization_subscriptions](docs/sdks/internal/README.md#get_organization_subscriptions) - Get organization subscription details
* [get_user](docs/sdks/internal/README.md#get_user) - Get a user by their id.
* [get_user_by_email](docs/sdks/internal/README.md#get_user_by_email) - Get a user by their email.
* [hide_segments](docs/sdks/internal/README.md#hide_segments) - Hides a list of segments
* [list_account_users](docs/sdks/internal/README.md#list_account_users) - List users in an account
* [list_api_keys](docs/sdks/internal/README.md#list_api_keys) - List API key metadata for a given organization and user
* [list_jobs](docs/sdks/internal/README.md#list_jobs) - List all of the jobs in a workspace.
* [list_managed_organizations](docs/sdks/internal/README.md#list_managed_organizations) - List managed organizations for a parent organization
* [list_monitor_config_v3_versions](docs/sdks/internal/README.md#list_monitor_config_v3_versions) - List the monitor config document versions for a given dataset.
* [list_organizations](docs/sdks/internal/README.md#list_organizations) - Get a list of all of the organization ids.
* [~~partially_update_org~~](docs/sdks/internal/README.md#partially_update_org) - Update some fields of an organization to non-null values :warning: **Deprecated**
* [partially_update_organization](docs/sdks/internal/README.md#partially_update_organization) - Update some fields of an organization to non-null values
* [patch_organization_memberships](docs/sdks/internal/README.md#patch_organization_memberships) - Add or delete memberships in a specific role and managed organization
* [post_monitor_config_validation_job](docs/sdks/internal/README.md#post_monitor_config_validation_job) - Create a monitor config validation job for all configs
* [provision_aws_marketplace_new_user](docs/sdks/internal/README.md#provision_aws_marketplace_new_user) - Create resources for a new user coming from AWS Marketplace
* [provision_databricks_connection](docs/sdks/internal/README.md#provision_databricks_connection) - Create resources for a new user coming from Databricks
* [provision_new_user](docs/sdks/internal/README.md#provision_new_user) - Create the resources that a new user needs to use WhyLabs via the website.
* [put_organization_memberships](docs/sdks/internal/README.md#put_organization_memberships) - Replace the memberships in a specific role and managed organization
* [put_request_monitor_run_config](docs/sdks/internal/README.md#put_request_monitor_run_config) - Put the RequestMonitorRun config into S3.
* [refresh_connection](docs/sdks/internal/README.md#refresh_connection) - Refresh metadata for a workspace connection.
* [register_databricks_connection](docs/sdks/internal/README.md#register_databricks_connection) - Register databricks metadata, temporarily storing it against a UUID so that it can be used to provision a databricks connection after email authentication
* [remove_membership_by_email](docs/sdks/internal/README.md#remove_membership_by_email) - Removes membership in a given org from a user, using the user's email address.
* [run_job](docs/sdks/internal/README.md#run_job) - Run an existing job in a given databricks workspace.
* [set_default_membership](docs/sdks/internal/README.md#set_default_membership) - Sets the organization that should be used when logging a user in
* [stripe_payment_endpoint](docs/sdks/internal/README.md#stripe_payment_endpoint) - Endpoint for Stripe payment webhooks
* [update_account_user](docs/sdks/internal/README.md#update_account_user) - Update account user
* [update_connection](docs/sdks/internal/README.md#update_connection) - Update the connection metadata for a given org
* [update_membership_by_email](docs/sdks/internal/README.md#update_membership_by_email) - Updates the role in an membership
* [update_notification_settings](docs/sdks/internal/README.md#update_notification_settings) - Update notification settings for an org
* [~~update_org~~](docs/sdks/internal/README.md#update_org) - Update an existing organization :warning: **Deprecated**
* [update_organization](docs/sdks/internal/README.md#update_organization) - Update an existing organization
* [update_user](docs/sdks/internal/README.md#update_user) - Update a user.
* [why_labs_search](docs/sdks/internal/README.md#why_labs_search) - WhyLabs Search
* [why_labs_search_indexing](docs/sdks/internal/README.md#why_labs_search_indexing) - WhyLabs Search Indexing

### [admin](docs/sdks/admin/README.md)

* [generate_report](docs/sdks/admin/README.md#generate_report) - Generate an admin report
* [post_monitor_config_validation_job](docs/sdks/admin/README.md#post_monitor_config_validation_job) - Create a monitor config validation job for all configs

### [databricks](docs/sdks/databricks/README.md)

* [get_connection](docs/sdks/databricks/README.md#get_connection) - Get the connection metadata for a given org
* [list_jobs](docs/sdks/databricks/README.md#list_jobs) - List all of the jobs in a workspace.
* [refresh_connection](docs/sdks/databricks/README.md#refresh_connection) - Refresh metadata for a workspace connection.
* [run_job](docs/sdks/databricks/README.md#run_job) - Run an existing job in a given databricks workspace.
* [update_connection](docs/sdks/databricks/README.md#update_connection) - Update the connection metadata for a given org

### [feature_flags](docs/sdks/featureflags/README.md)

* [get_feature_flags](docs/sdks/featureflags/README.md#get_feature_flags) - Get feature flags for the specified user/org

### [membership](docs/sdks/membership/README.md)

* [create_membership](docs/sdks/membership/README.md#create_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [create_organization_membership](docs/sdks/membership/README.md#create_organization_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [get_default_membership_for_email](docs/sdks/membership/README.md#get_default_membership_for_email) - Get the default membership for a user.
* [get_memberships](docs/sdks/membership/README.md#get_memberships) - Get memberships for a user.
* [get_memberships_by_email](docs/sdks/membership/README.md#get_memberships_by_email) - Get memberships for a user given that user's email address.
* [get_memberships_by_org](docs/sdks/membership/README.md#get_memberships_by_org) - Get memberships for an org.
* [list_organization_memberships](docs/sdks/membership/README.md#list_organization_memberships) - List organization memberships
* [remove_membership_by_email](docs/sdks/membership/README.md#remove_membership_by_email) - Removes membership in a given org from a user, using the user's email address.
* [remove_organization_membership](docs/sdks/membership/README.md#remove_organization_membership) - Removes membership in a given org from a user, using the user's email address.
* [set_default_membership](docs/sdks/membership/README.md#set_default_membership) - Sets the organization that should be used when logging a user in
* [update_membership_by_email](docs/sdks/membership/README.md#update_membership_by_email) - Updates the role in an membership
* [update_organization_membership](docs/sdks/membership/README.md#update_organization_membership) - Updates the role in an membership

### [notification_settings](docs/sdks/notificationsettings/README.md)

* [add_notification_action](docs/sdks/notificationsettings/README.md#add_notification_action) - Add new notification action
* [delete_notification_action](docs/sdks/notificationsettings/README.md#delete_notification_action) - Delete notification action
* [disable_notification_action](docs/sdks/notificationsettings/README.md#disable_notification_action) - Disable notification action
* [enable_notification_action](docs/sdks/notificationsettings/README.md#enable_notification_action) - Enable notification action
* [get_notification_action](docs/sdks/notificationsettings/README.md#get_notification_action) - Get notification action for id
* [get_notification_settings](docs/sdks/notificationsettings/README.md#get_notification_settings) - Get notification settings for an org
* [list_notification_actions](docs/sdks/notificationsettings/README.md#list_notification_actions) - List notification actions for an org
* [put_notification_action](docs/sdks/notificationsettings/README.md#put_notification_action) - Add new notification action
* [test_notification_action](docs/sdks/notificationsettings/README.md#test_notification_action) - Test a notification action
* [update_notification_action](docs/sdks/notificationsettings/README.md#update_notification_action) - Update notification action
* [update_notification_settings](docs/sdks/notificationsettings/README.md#update_notification_settings) - Update notification settings for an org
* [get_email_notification_action_payload](docs/sdks/notificationsettings/README.md#get_email_notification_action_payload) - Get dummy notification action payload
* [get_pager_duty_notification_action_payload](docs/sdks/notificationsettings/README.md#get_pager_duty_notification_action_payload) - Get dummy notification action payload
* [get_slack_notification_action_payload](docs/sdks/notificationsettings/README.md#get_slack_notification_action_payload) - Get dummy notification action payload

### [organizations](docs/sdks/organizations/README.md)

* [create_organization](docs/sdks/organizations/README.md#create_organization) - Create an organization
* [delete_organization](docs/sdks/organizations/README.md#delete_organization) - Delete an org
* [get_aws_marketplace_metadata](docs/sdks/organizations/README.md#get_aws_marketplace_metadata) - Get marketplace metadata for an org if any exists.
* [get_organization](docs/sdks/organizations/README.md#get_organization) - Get the metadata about an organization.
* [list_organizations](docs/sdks/organizations/README.md#list_organizations) - Get a list of all of the organization ids.
* [~~partially_update_org~~](docs/sdks/organizations/README.md#partially_update_org) - Update some fields of an organization to non-null values :warning: **Deprecated**
* [partially_update_organization](docs/sdks/organizations/README.md#partially_update_organization) - Update some fields of an organization to non-null values
* [~~update_org~~](docs/sdks/organizations/README.md#update_org) - Update an existing organization :warning: **Deprecated**
* [update_organization](docs/sdks/organizations/README.md#update_organization) - Update an existing organization

### [api_key](docs/sdks/apikey/README.md)

* [create_api_key](docs/sdks/apikey/README.md#create_api_key) - Generate an API key for a user.
* [get_api_key](docs/sdks/apikey/README.md#get_api_key) - Get an api key by its id
* [list_api_keys](docs/sdks/apikey/README.md#list_api_keys) - List API key metadata for a given organization and user
* [revoke_api_key](docs/sdks/apikey/README.md#revoke_api_key) - Revoke the given API Key, removing its ability to access WhyLabs systems

### [dataset_profile](docs/sdks/datasetprofile/README.md)

* [create_reference_profile](docs/sdks/datasetprofile/README.md#create_reference_profile) - Returns data needed to uploading the reference profile
* [delete_analyzer_results](docs/sdks/datasetprofile/README.md#delete_analyzer_results) - Deletes a set of analyzer results
* [delete_dataset_profiles](docs/sdks/datasetprofile/README.md#delete_dataset_profiles) - Deletes a set of dataset profiles
* [delete_reference_profile](docs/sdks/datasetprofile/README.md#delete_reference_profile) - Delete a single reference profile
* [get_profile_traces](docs/sdks/datasetprofile/README.md#get_profile_traces) - Returns a list for profile traces matching a trace id
* [get_reference_profile](docs/sdks/datasetprofile/README.md#get_reference_profile) - Returns a single reference profile
* [hide_segments](docs/sdks/datasetprofile/README.md#hide_segments) - Hides a list of segments
* [list_reference_profiles](docs/sdks/datasetprofile/README.md#list_reference_profiles) - Returns a list for reference profiles between the given time range filtered on the upload timestamp
* [list_segments](docs/sdks/datasetprofile/README.md#list_segments) - Returns a list of segments

### [dataset_metadata](docs/sdks/datasetmetadata/README.md)

* [delete_dataset_metadata](docs/sdks/datasetmetadata/README.md#delete_dataset_metadata) - Delete dataset metadata for the specified dataset
* [get_dataset_metadata](docs/sdks/datasetmetadata/README.md#get_dataset_metadata) - Get dataset metadata for the specified dataset
* [put_dataset_metadata](docs/sdks/datasetmetadata/README.md#put_dataset_metadata) - Put dataset metadata for the specified dataset

### [feature_weights](docs/sdks/featureweights/README.md)

* [get_column_weights](docs/sdks/featureweights/README.md#get_column_weights) - Get column weights for the specified dataset
* [put_column_weights](docs/sdks/featureweights/README.md#put_column_weights) - Put column weights for the specified dataset

### [debug_events](docs/sdks/debugevents/README.md)

* [log_debug_event](docs/sdks/debugevents/README.md#log_debug_event) - Log a debug event

### [log](docs/sdks/log/README.md)

* [get_profile_observatory_link](docs/sdks/log/README.md#get_profile_observatory_link) - Get observatory links for profiles in a given org/model. A max of 3 profiles can be viewed a a time.
* [log_async](docs/sdks/log/README.md#log_async) - Like /log, except this api doesn't take the actual profile content. It returns an upload link that can be used to upload the profile to.
* [log_reference](docs/sdks/log/README.md#log_reference) - Returns a presigned URL for uploading the reference profile to.

### [models](docs/sdks/models/README.md)

* [create_model](docs/sdks/models/README.md#create_model) - Create a model with a given name and a time period
* [deactivate_model](docs/sdks/models/README.md#deactivate_model) - Mark a model as inactive
* [delete_entity_schema](docs/sdks/models/README.md#delete_entity_schema) - Delete the entity schema config for a given dataset.
* [delete_entity_schema_column](docs/sdks/models/README.md#delete_entity_schema_column) - Delete the entity schema of a single column for a given dataset.
* [delete_entity_schema_metric](docs/sdks/models/README.md#delete_entity_schema_metric) - Delete the schema of a single metric for a given dataset.
* [get_entity_schema](docs/sdks/models/README.md#get_entity_schema) - Get the entity schema config for a given dataset.
* [get_entity_schema_column](docs/sdks/models/README.md#get_entity_schema_column) - Get the entity schema of a single column for a given dataset.
* [get_model](docs/sdks/models/README.md#get_model) - Get a model metadata
* [list_models](docs/sdks/models/README.md#list_models) - Get a list of all of the model ids for an organization.
* [put_entity_schema](docs/sdks/models/README.md#put_entity_schema) - Save the entity schema config for a given dataset.
* [put_entity_schema_column](docs/sdks/models/README.md#put_entity_schema_column) - Save the entity schema of a single column for a given dataset.
* [put_entity_schema_metric](docs/sdks/models/README.md#put_entity_schema_metric) - Save the schema of a single metric for a given dataset.
* [update_model](docs/sdks/models/README.md#update_model) - Update a model's metadata

### [monitor](docs/sdks/monitor/README.md)

* [delete_analyzer](docs/sdks/monitor/README.md#delete_analyzer) - Delete the analyzer config for a given dataset.
* [delete_monitor](docs/sdks/monitor/README.md#delete_monitor) - Delete the monitor for a given dataset.
* [get_analyzer](docs/sdks/monitor/README.md#get_analyzer) - Get the analyzer config for a given dataset.
* [get_monitor](docs/sdks/monitor/README.md#get_monitor) - Get the monitor config for a given dataset.
* [get_monitor_config_v3](docs/sdks/monitor/README.md#get_monitor_config_v3) - Get the monitor config document for a given dataset.
* [get_monitor_config_v3_version](docs/sdks/monitor/README.md#get_monitor_config_v3_version) - Get the monitor config document version for a given dataset.
* [list_constraints](docs/sdks/monitor/README.md#list_constraints) - List the constraints for a given dataset.
* [list_monitor_config_v3_versions](docs/sdks/monitor/README.md#list_monitor_config_v3_versions) - List the monitor config document versions for a given dataset.
* [patch_monitor_config_v3](docs/sdks/monitor/README.md#patch_monitor_config_v3) - Patch an updated monitor config document for a given dataset.
* [put_analyzer](docs/sdks/monitor/README.md#put_analyzer) - Save the analyzer config for a given dataset.
* [put_monitor](docs/sdks/monitor/README.md#put_monitor) - Save the monitor for a given dataset.
* [put_monitor_config_v3](docs/sdks/monitor/README.md#put_monitor_config_v3) - Save the monitor config document for a given dataset.
* [put_request_monitor_run_config](docs/sdks/monitor/README.md#put_request_monitor_run_config) - Put the RequestMonitorRun config into S3.
* [validate_monitor_config_v3](docs/sdks/monitor/README.md#validate_monitor_config_v3) - Validate the monitor config document for a given dataset.

### [schema](docs/sdks/schema/README.md)

* [get_monitor_config_schema](docs/sdks/schema/README.md#get_monitor_config_schema) - Get the current supported schema of the monitor configuration

### [payment](docs/sdks/payment/README.md)

* [stripe_payment_endpoint](docs/sdks/payment/README.md#stripe_payment_endpoint) - Endpoint for Stripe payment webhooks

### [provision](docs/sdks/provision/README.md)

* [provision_aws_marketplace_new_user](docs/sdks/provision/README.md#provision_aws_marketplace_new_user) - Create resources for a new user coming from AWS Marketplace
* [provision_databricks_connection](docs/sdks/provision/README.md#provision_databricks_connection) - Create resources for a new user coming from Databricks
* [provision_new_user](docs/sdks/provision/README.md#provision_new_user) - Create the resources that a new user needs to use WhyLabs via the website.
* [register_databricks_connection](docs/sdks/provision/README.md#register_databricks_connection) - Register databricks metadata, temporarily storing it against a UUID so that it can be used to provision a databricks connection after email authentication

### [search](docs/sdks/search/README.md)

* [why_labs_search](docs/sdks/search/README.md#why_labs_search) - WhyLabs Search
* [why_labs_search_indexing](docs/sdks/search/README.md#why_labs_search_indexing) - WhyLabs Search Indexing

### [sessions](docs/sdks/sessions/README.md)

* [batch_create_reference_profile_upload](docs/sdks/sessions/README.md#batch_create_reference_profile_upload) - Create multiple reference profile uploads for a given session.
* [claim_guest_session](docs/sdks/sessions/README.md#claim_guest_session) - Claim a guest session, copying its model data into another org and expiring the session.
* [create_dataset_profile_upload](docs/sdks/sessions/README.md#create_dataset_profile_upload) - Create an upload for a given session.
* [create_reference_profile_upload](docs/sdks/sessions/README.md#create_reference_profile_upload) - Create a reference profile upload for a given session.
* [create_session](docs/sdks/sessions/README.md#create_session) - Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.
* [get_session](docs/sdks/sessions/README.md#get_session) - Get information about a session.
* [get_session_profile_observatory_link](docs/sdks/sessions/README.md#get_session_profile_observatory_link) - Get observatory links for profiles in a given session. A max of 3 profiles can be viewed a a time.

### [subscription](docs/sdks/subscription/README.md)

* [get_organization_subscriptions](docs/sdks/subscription/README.md#get_organization_subscriptions) - Get organization subscription details

### [user](docs/sdks/user/README.md)

* [create_user](docs/sdks/user/README.md#create_user) - Create a user.
* [get_user](docs/sdks/user/README.md#get_user) - Get a user by their id.
* [get_user_by_email](docs/sdks/user/README.md#get_user_by_email) - Get a user by their email.
* [update_user](docs/sdks/user/README.md#update_user) - Update a user.
<!-- End SDK Available Operations -->



<!-- Start Dev Containers -->

<!-- End Dev Containers -->



<!-- Start Error Handling -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

### Example

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="",
)

req = operations.CreateAccountUserRequest(
    create_account_user_request=shared.CreateAccountUserRequest(
        email='Jason_Skiles63@yahoo.com',
    ),
    org_id='org-123',
)

res = None
try:
    res = s.account.create_account_user(req)

except (errors.SDKError) as e:
    print(e) # handle exception


if res.status_code == 200:
    # handle response
    pass
```
<!-- End Error Handling -->



<!-- Start Server Selection -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.whylabsapp.com` | None |

#### Example

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    server_idx=0,
    api_key_auth="",
)

req = operations.CreateAccountUserRequest(
    create_account_user_request=shared.CreateAccountUserRequest(
        email='Jason_Skiles63@yahoo.com',
    ),
    org_id='org-123',
)

res = s.account.create_account_user(req)

if res.status_code == 200:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    server_url="https://api.whylabsapp.com",
    api_key_auth="",
)

req = operations.CreateAccountUserRequest(
    create_account_user_request=shared.CreateAccountUserRequest(
        email='Jason_Skiles63@yahoo.com',
    ),
    org_id='org-123',
)

res = s.account.create_account_user(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End Server Selection -->



<!-- Start Custom HTTP Client -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import songbird
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = songbird.Songbird(client: http_client)
```
<!-- End Custom HTTP Client -->



<!-- Start Authentication -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name           | Type           | Scheme         |
| -------------- | -------------- | -------------- |
| `api_key_auth` | apiKey         | API key        |

To authenticate with the API the `api_key_auth` parameter must be set when initializing the SDK client instance. For example:
```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="",
)

req = operations.CreateAccountUserRequest(
    create_account_user_request=shared.CreateAccountUserRequest(
        email='Jason_Skiles63@yahoo.com',
    ),
    org_id='org-123',
)

res = s.account.create_account_user(req)

if res.status_code == 200:
    # handle response
    pass
```
<!-- End Authentication -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
