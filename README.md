# Songbird

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/andyndang/demo-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import songbird
from songbird.models import operations

s = songbird.Songbird()


res = s.admin.post_monitor_config_validation_job(operations.PostMonitorConfigValidationJobSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [admin](docs/admin/README.md)

* [post_monitor_config_validation_job](docs/admin/README.md#post_monitor_config_validation_job) - Create a monitor config validation job for all configs

### [api_key](docs/apikey/README.md)

* [create_api_key](docs/apikey/README.md#create_api_key) - Generate an API key for a user.
* [get_api_key](docs/apikey/README.md#get_api_key) - Get an api key by its id
* [list_api_keys](docs/apikey/README.md#list_api_keys) - List API key metadata for a given organization and user
* [revoke_api_key](docs/apikey/README.md#revoke_api_key) - Revoke the given API Key, removing its ability to access WhyLabs systems

### [databricks](docs/databricks/README.md)

* [get_connection](docs/databricks/README.md#get_connection) - Get the connection metadata for a given org
* [list_jobs](docs/databricks/README.md#list_jobs) - List all of the jobs in a workspace.
* [refresh_connection](docs/databricks/README.md#refresh_connection) - Refresh metadata for a workspace connection.
* [run_job](docs/databricks/README.md#run_job) - Run an existing job in a given databricks workspace.
* [update_connection](docs/databricks/README.md#update_connection) - Update the connection metadata for a given org

### [dataset_metadata](docs/datasetmetadata/README.md)

* [delete_dataset_metadata](docs/datasetmetadata/README.md#delete_dataset_metadata) - Delete dataset metadata for the specified dataset
* [get_dataset_metadata](docs/datasetmetadata/README.md#get_dataset_metadata) - Get dataset metadata for the specified dataset
* [put_dataset_metadata](docs/datasetmetadata/README.md#put_dataset_metadata) - Put dataset metadata for the specified dataset

### [dataset_profile](docs/datasetprofile/README.md)

* [create_reference_profile](docs/datasetprofile/README.md#create_reference_profile) - Returns data needed to uploading the reference profile
* [delete_analyzer_results](docs/datasetprofile/README.md#delete_analyzer_results) - Deletes a set of analyzer results
* [delete_dataset_profiles](docs/datasetprofile/README.md#delete_dataset_profiles) - Deletes a set of dataset profiles
* [delete_reference_profile](docs/datasetprofile/README.md#delete_reference_profile) - Delete a single reference profile
* [get_reference_profile](docs/datasetprofile/README.md#get_reference_profile) - Returns a single reference profile
* [list_reference_profiles](docs/datasetprofile/README.md#list_reference_profiles) - Returns a list for reference profiles
* [list_segments](docs/datasetprofile/README.md#list_segments) - Returns a list of segments

### [feature_weights](docs/featureweights/README.md)

* [get_column_weights](docs/featureweights/README.md#get_column_weights) - Get column weights for the specified dataset
* [put_column_weights](docs/featureweights/README.md#put_column_weights) - Put column weights for the specified dataset

### [feature_flags](docs/featureflags/README.md)

* [get_feature_flags](docs/featureflags/README.md#get_feature_flags) - Get feature flags for the specified user/org

### [internal](docs/internal/README.md)

* [create_membership](docs/internal/README.md#create_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [create_organization](docs/internal/README.md#create_organization) - Create an organization
* [create_user](docs/internal/README.md#create_user) - Create a user.
* [delete_organization](docs/internal/README.md#delete_organization) - Delete an org
* [get_aws_marketplace_metadata](docs/internal/README.md#get_aws_marketplace_metadata) - Get marketplace metadata for an org if any exists.
* [get_api_key](docs/internal/README.md#get_api_key) - Get an api key by its id
* [get_connection](docs/internal/README.md#get_connection) - Get the connection metadata for a given org
* [get_default_membership_for_email](docs/internal/README.md#get_default_membership_for_email) - Get the default membership for a user.
* [get_feature_flags](docs/internal/README.md#get_feature_flags) - Get feature flags for the specified user/org
* [get_memberships](docs/internal/README.md#get_memberships) - Get memberships for a user.
* [get_memberships_by_email](docs/internal/README.md#get_memberships_by_email) - Get memberships for a user given that user's email address.
* [get_memberships_by_org](docs/internal/README.md#get_memberships_by_org) - Get memberships for an org.
* [get_monitor_config_v3_version](docs/internal/README.md#get_monitor_config_v3_version) - Get the monitor config document version for a given dataset.
* [get_notification_settings](docs/internal/README.md#get_notification_settings) - Get notification settings for an org
* [get_organization](docs/internal/README.md#get_organization) - Get the metadata about an organization.
* [get_user](docs/internal/README.md#get_user) - Get a user by their id.
* [get_user_by_email](docs/internal/README.md#get_user_by_email) - Get a user by their email.
* [list_api_keys](docs/internal/README.md#list_api_keys) - List API key metadata for a given organization and user
* [list_jobs](docs/internal/README.md#list_jobs) - List all of the jobs in a workspace.
* [list_monitor_config_v3_versions](docs/internal/README.md#list_monitor_config_v3_versions) - List the monitor config document versions for a given dataset.
* [list_organizations](docs/internal/README.md#list_organizations) - Get a list of all of the organization ids.
* [list_segments](docs/internal/README.md#list_segments) - Returns a list of segments
* [~~partially_update_org~~](docs/internal/README.md#partially_update_org) - Update some fields of an organization to non-null values :warning: **Deprecated**
* [partially_update_organization](docs/internal/README.md#partially_update_organization) - Update some fields of an organization to non-null values
* [post_monitor_config_validation_job](docs/internal/README.md#post_monitor_config_validation_job) - Create a monitor config validation job for all configs
* [provision_aws_marketplace_new_user](docs/internal/README.md#provision_aws_marketplace_new_user) - Create resources for a new user coming from AWS Marketplace
* [provision_databricks_connection](docs/internal/README.md#provision_databricks_connection) - Create resources for a new user coming from Databricks
* [provision_new_user](docs/internal/README.md#provision_new_user) - Create the resources that a new user needs to use WhyLabs via the website.
* [put_request_monitor_run_config](docs/internal/README.md#put_request_monitor_run_config) - Put the RequestMonitorRun config into S3.
* [refresh_connection](docs/internal/README.md#refresh_connection) - Refresh metadata for a workspace connection.
* [register_databricks_connection](docs/internal/README.md#register_databricks_connection) - Register databricks metadata, temporarily storing it against a UUID so that it can be used to provision a databricks connection after email authentication
* [remove_membership_by_email](docs/internal/README.md#remove_membership_by_email) - Removes membership in a given org from a user, using the user's email address.
* [run_job](docs/internal/README.md#run_job) - Run an existing job in a given databricks workspace.
* [set_default_membership](docs/internal/README.md#set_default_membership) - Sets the organization that should be used when logging a user in
* [stripe_payment_endpoint](docs/internal/README.md#stripe_payment_endpoint) - Endpoint for Stripe payment webhooks
* [update_connection](docs/internal/README.md#update_connection) - Update the connection metadata for a given org
* [update_membership_by_email](docs/internal/README.md#update_membership_by_email) - Updates the role in an membership
* [update_notification_settings](docs/internal/README.md#update_notification_settings) - Update notification settings for an org
* [~~update_org~~](docs/internal/README.md#update_org) - Update an existing organization :warning: **Deprecated**
* [update_organization](docs/internal/README.md#update_organization) - Update an existing organization
* [update_user](docs/internal/README.md#update_user) - Update a user.
* [why_labs_search](docs/internal/README.md#why_labs_search) - WhyLabs Search
* [why_labs_search_indexing](docs/internal/README.md#why_labs_search_indexing) - WhyLabs Search Indexing

### [log](docs/log/README.md)

* [log_async](docs/log/README.md#log_async) - Like /log, except this api doesn't take the actual profile content. It returns an upload link that can be used to upload the profile to.
* [log_reference](docs/log/README.md#log_reference) - Returns a presigned URL for uploading the reference profile to.

### [membership](docs/membership/README.md)

* [create_membership](docs/membership/README.md#create_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [create_organization_membership](docs/membership/README.md#create_organization_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [get_default_membership_for_email](docs/membership/README.md#get_default_membership_for_email) - Get the default membership for a user.
* [get_memberships](docs/membership/README.md#get_memberships) - Get memberships for a user.
* [get_memberships_by_email](docs/membership/README.md#get_memberships_by_email) - Get memberships for a user given that user's email address.
* [get_memberships_by_org](docs/membership/README.md#get_memberships_by_org) - Get memberships for an org.
* [list_organization_memberships](docs/membership/README.md#list_organization_memberships) - List organization memberships
* [remove_membership_by_email](docs/membership/README.md#remove_membership_by_email) - Removes membership in a given org from a user, using the user's email address.
* [remove_organization_membership](docs/membership/README.md#remove_organization_membership) - Removes membership in a given org from a user, using the user's email address.
* [set_default_membership](docs/membership/README.md#set_default_membership) - Sets the organization that should be used when logging a user in
* [update_membership_by_email](docs/membership/README.md#update_membership_by_email) - Updates the role in an membership
* [update_organization_membership](docs/membership/README.md#update_organization_membership) - Updates the role in an membership

### [models](docs/models/README.md)

* [create_model](docs/models/README.md#create_model) - Create a model with a given name and a time period
* [deactivate_model](docs/models/README.md#deactivate_model) - Mark a model as inactive
* [delete_entity_schema](docs/models/README.md#delete_entity_schema) - Delete the entity schema config for a given dataset.
* [delete_entity_schema_column](docs/models/README.md#delete_entity_schema_column) - Delete the entity schema of a single column for a given dataset.
* [delete_entity_schema_metric](docs/models/README.md#delete_entity_schema_metric) - Delete the schema of a single metric for a given dataset.
* [get_entity_schema](docs/models/README.md#get_entity_schema) - Get the entity schema config for a given dataset.
* [get_entity_schema_column](docs/models/README.md#get_entity_schema_column) - Get the entity schema of a single column for a given dataset.
* [get_model](docs/models/README.md#get_model) - Get a model metadata
* [list_models](docs/models/README.md#list_models) - Get a list of all of the model ids for an organization.
* [put_entity_schema](docs/models/README.md#put_entity_schema) - Save the entity schema config for a given dataset.
* [put_entity_schema_column](docs/models/README.md#put_entity_schema_column) - Save the entity schema of a single column for a given dataset.
* [put_entity_schema_metric](docs/models/README.md#put_entity_schema_metric) - Save the schema of a single metric for a given dataset.
* [update_model](docs/models/README.md#update_model) - Update a model's metadata

### [monitor](docs/monitor/README.md)

* [delete_analyzer](docs/monitor/README.md#delete_analyzer) - Delete the analyzer config for a given dataset.
* [delete_monitor](docs/monitor/README.md#delete_monitor) - Delete the monitor for a given dataset.
* [get_analyzer](docs/monitor/README.md#get_analyzer) - Get the analyzer config for a given dataset.
* [get_monitor](docs/monitor/README.md#get_monitor) - Get the monitor config for a given dataset.
* [get_monitor_config_v3](docs/monitor/README.md#get_monitor_config_v3) - Get the monitor config document for a given dataset.
* [get_monitor_config_v3_version](docs/monitor/README.md#get_monitor_config_v3_version) - Get the monitor config document version for a given dataset.
* [list_monitor_config_v3_versions](docs/monitor/README.md#list_monitor_config_v3_versions) - List the monitor config document versions for a given dataset.
* [patch_monitor_config_v3](docs/monitor/README.md#patch_monitor_config_v3) - Patch an updated monitor config document for a given dataset.
* [put_analyzer](docs/monitor/README.md#put_analyzer) - Save the analyzer config for a given dataset.
* [put_monitor](docs/monitor/README.md#put_monitor) - Save the monitor for a given dataset.
* [put_monitor_config_v3](docs/monitor/README.md#put_monitor_config_v3) - Save the monitor config document for a given dataset.
* [put_request_monitor_run_config](docs/monitor/README.md#put_request_monitor_run_config) - Put the RequestMonitorRun config into S3.
* [validate_monitor_config_v3](docs/monitor/README.md#validate_monitor_config_v3) - Validate the monitor config document for a given dataset.

### [notification_settings](docs/notificationsettings/README.md)

* [add_notification_action](docs/notificationsettings/README.md#add_notification_action) - Add new notification action
* [delete_notification_action](docs/notificationsettings/README.md#delete_notification_action) - Delete notification action
* [disable_notification_action](docs/notificationsettings/README.md#disable_notification_action) - Disable notification action
* [enable_notification_action](docs/notificationsettings/README.md#enable_notification_action) - Enable notification action
* [get_notification_action](docs/notificationsettings/README.md#get_notification_action) - Get notification action for id
* [get_notification_settings](docs/notificationsettings/README.md#get_notification_settings) - Get notification settings for an org
* [list_notification_actions](docs/notificationsettings/README.md#list_notification_actions) - List notification actions for an org
* [put_notification_action](docs/notificationsettings/README.md#put_notification_action) - Add new notification action
* [test_notification_action](docs/notificationsettings/README.md#test_notification_action) - Test a notification action
* [update_notification_action](docs/notificationsettings/README.md#update_notification_action) - Update notification action
* [update_notification_settings](docs/notificationsettings/README.md#update_notification_settings) - Update notification settings for an org
* [get_email_notification_action_payload](docs/notificationsettings/README.md#get_email_notification_action_payload) - Get dummy notification action payload
* [get_pager_duty_notification_action_payload](docs/notificationsettings/README.md#get_pager_duty_notification_action_payload) - Get dummy notification action payload
* [get_slack_notification_action_payload](docs/notificationsettings/README.md#get_slack_notification_action_payload) - Get dummy notification action payload

### [organizations](docs/organizations/README.md)

* [create_organization](docs/organizations/README.md#create_organization) - Create an organization
* [delete_organization](docs/organizations/README.md#delete_organization) - Delete an org
* [get_aws_marketplace_metadata](docs/organizations/README.md#get_aws_marketplace_metadata) - Get marketplace metadata for an org if any exists.
* [get_organization](docs/organizations/README.md#get_organization) - Get the metadata about an organization.
* [list_organizations](docs/organizations/README.md#list_organizations) - Get a list of all of the organization ids.
* [~~partially_update_org~~](docs/organizations/README.md#partially_update_org) - Update some fields of an organization to non-null values :warning: **Deprecated**
* [partially_update_organization](docs/organizations/README.md#partially_update_organization) - Update some fields of an organization to non-null values
* [~~update_org~~](docs/organizations/README.md#update_org) - Update an existing organization :warning: **Deprecated**
* [update_organization](docs/organizations/README.md#update_organization) - Update an existing organization

### [payment](docs/payment/README.md)

* [stripe_payment_endpoint](docs/payment/README.md#stripe_payment_endpoint) - Endpoint for Stripe payment webhooks

### [provision](docs/provision/README.md)

* [provision_aws_marketplace_new_user](docs/provision/README.md#provision_aws_marketplace_new_user) - Create resources for a new user coming from AWS Marketplace
* [provision_databricks_connection](docs/provision/README.md#provision_databricks_connection) - Create resources for a new user coming from Databricks
* [provision_new_user](docs/provision/README.md#provision_new_user) - Create the resources that a new user needs to use WhyLabs via the website.
* [register_databricks_connection](docs/provision/README.md#register_databricks_connection) - Register databricks metadata, temporarily storing it against a UUID so that it can be used to provision a databricks connection after email authentication

### [schema](docs/schema/README.md)

* [get_monitor_config_schema](docs/schema/README.md#get_monitor_config_schema) - Get the current supported schema of the monitor configuration

### [search](docs/search/README.md)

* [why_labs_search](docs/search/README.md#why_labs_search) - WhyLabs Search
* [why_labs_search_indexing](docs/search/README.md#why_labs_search_indexing) - WhyLabs Search Indexing

### [sessions](docs/sessions/README.md)

* [batch_create_reference_profile_upload](docs/sessions/README.md#batch_create_reference_profile_upload) - Create multiple reference profile uploads for a given session.
* [claim_guest_session](docs/sessions/README.md#claim_guest_session) - Claim a guest session, copying its model data into another org and expiring the session.
* [create_dataset_profile_upload](docs/sessions/README.md#create_dataset_profile_upload) - Create an upload for a given session.
* [create_reference_profile_upload](docs/sessions/README.md#create_reference_profile_upload) - Create a reference profile upload for a given session.
* [create_session](docs/sessions/README.md#create_session) - Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.
* [get_session](docs/sessions/README.md#get_session) - Get information about a session.

### [user](docs/user/README.md)

* [create_user](docs/user/README.md#create_user) - Create a user.
* [get_user](docs/user/README.md#get_user) - Get a user by their id.
* [get_user_by_email](docs/user/README.md#get_user_by_email) - Get a user by their email.
* [update_user](docs/user/README.md#update_user) - Update a user.
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
