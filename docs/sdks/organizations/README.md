# Organizations
(*organizations*)

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

res = s.organizations.create_organization(req)

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
| errors.SDKError | 400-600         | */*             |

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

res = s.organizations.delete_organization(req)

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
| errors.SDKError | 400-600         | */*             |

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

res = s.organizations.get_aws_marketplace_metadata(req)

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
| errors.SDKError | 400-600         | */*             |

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

res = s.organizations.get_organization(req)

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
| errors.SDKError | 400-600         | */*             |

## list_organizations

Get a list of all of the organization ids.

### Example Usage

```python
import songbird

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.organizations.list_organizations()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.ListOrganizationsResponse](../../models/operations/listorganizationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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

res = s.organizations.partially_update_org(req)

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
| errors.SDKError | 400-600         | */*             |

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

res = s.organizations.partially_update_organization(req)

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
| errors.SDKError | 400-600         | */*             |

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

res = s.organizations.update_org(req)

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
| errors.SDKError | 400-600         | */*             |

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

res = s.organizations.update_organization(req)

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
| errors.SDKError | 400-600         | */*             |
