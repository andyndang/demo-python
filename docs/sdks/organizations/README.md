# organizations

### Available Operations

* [create_organization](#create_organization) - Create an organization
* [delete_organization](#delete_organization) - Delete an org
* [get_aws_marketplace_metadata](#get_aws_marketplace_metadata) - Get marketplace metadata for an org if any exists.
* [get_organization](#get_organization) - Get the metadata about an organization.
* [list_organizations](#list_organizations) - Get a list of all of the organization ids.
* [~~partially_update_org~~](#partially_update_org) - Update some fields of an organization to non-null values :warning: **Deprecated**
* [partially_update_organization](#partially_update_organization) - Update some fields of an organization to non-null values
* [~~update_org~~](#update_org) - Update an existing organization :warning: **Deprecated**
* [update_organization](#update_organization) - Update an existing organization

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
    parent_org_id='org-123',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.FREE,
)

res = s.organizations.create_organization(req, operations.CreateOrganizationSecurity(
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


## delete_organization

Delete an org

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.DeleteOrganizationRequest(
    org_id='iure',
)

res = s.organizations.delete_organization(req, operations.DeleteOrganizationSecurity(
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


## get_aws_marketplace_metadata

Get marketplace metadata for an org if any exists.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetAWSMarketplaceMetadataRequest(
    org_id='odio',
)

res = s.organizations.get_aws_marketplace_metadata(req, operations.GetAWSMarketplaceMetadataSecurity(
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


## get_organization

Returns various metadata about an organization

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetOrganizationRequest(
    org_id='quaerat',
)

res = s.organizations.get_organization(req, operations.GetOrganizationSecurity(
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


## list_organizations

Get a list of all of the organization ids.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()


res = s.organizations.list_organizations(operations.ListOrganizationsSecurity(
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


## ~~partially_update_org~~

Update some fields of an organization to non-null values, leaving all other existing values the same

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.PartiallyUpdateOrgRequest(
    request_body=operations.PartiallyUpdateOrgRequestBody(
        org_id='accusamus',
    ),
    domain='acme.ai',
    name='ACME, Inc',
    notification_email_address='notifications@acme.ai',
    observatory_url='https://hub.whylabsapp.com',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.AWS_MARKETPLACE,
)

res = s.organizations.partially_update_org(req, operations.PartiallyUpdateOrgSecurity(
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
    org_id='voluptatibus',
    pager_duty_key='abc-def-ghi-jkl',
    parent_org_id='abc-def-ghi-jkl',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.PAID,
)

res = s.organizations.partially_update_organization(req, operations.PartiallyUpdateOrganizationSecurity(
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


## ~~update_org~~

Update all fields of an existing organization

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.UpdateOrgRequest(
    request_body=operations.UpdateOrgRequestBody(
        org_id='natus',
    ),
    domain='acme.ai',
    email_domains='acme.ai,acme.com',
    name='ACME, Inc',
    notification_email_address='notifications@acme.ai',
    observatory_url='https://hub.whylabsapp.com',
    pager_duty_key='abc-def-ghi-jkl',
    parent_org_id='org-123',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.FREE,
)

res = s.organizations.update_org(req, operations.UpdateOrgSecurity(
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
    org_id='atque',
    pager_duty_key='abc-def-ghi-jkl',
    parent_org_id='org-123',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.FREE,
)

res = s.organizations.update_organization(req, operations.UpdateOrganizationSecurity(
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

