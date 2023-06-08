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
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.AWS_MARKETPLACE,
)

res = s.organizations.create_organization(req, operations.CreateOrganizationSecurity(
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
    org_id='odit',
)

res = s.organizations.delete_organization(req, operations.DeleteOrganizationSecurity(
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
    org_id='ea',
)

res = s.organizations.get_aws_marketplace_metadata(req, operations.GetAWSMarketplaceMetadataSecurity(
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
    org_id='accusantium',
)

res = s.organizations.get_organization(req, operations.GetOrganizationSecurity(
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


res = s.organizations.list_organizations(operations.ListOrganizationsSecurity(
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
        org_id='ab',
    ),
    domain='acme.ai',
    name='ACME, Inc',
    notification_email_address='notifications@acme.ai',
    observatory_url='https://hub.whylabsapp.com',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.SUBSCRIPTION,
)

res = s.organizations.partially_update_org(req, operations.PartiallyUpdateOrgSecurity(
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
    org_id='quidem',
    pager_duty_key='abc-def-ghi-jkl',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.PAID,
)

res = s.organizations.partially_update_organization(req, operations.PartiallyUpdateOrganizationSecurity(
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
        org_id='voluptate',
    ),
    domain='acme.ai',
    email_domains='acme.ai,acme.com',
    name='ACME, Inc',
    notification_email_address='notifications@acme.ai',
    observatory_url='https://hub.whylabsapp.com',
    pager_duty_key='abc-def-ghi-jkl',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.PAID,
)

res = s.organizations.update_org(req, operations.UpdateOrgSecurity(
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
    org_id='nam',
    pager_duty_key='abc-def-ghi-jkl',
    slack_webhook='https://hooks.slack.com/services/foo/bar',
    subscription_tier=shared.SubscriptionTier.FREE,
)

res = s.organizations.update_organization(req, operations.UpdateOrganizationSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```
