# membership

### Available Operations

* [create_membership](#create_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [create_organization_membership](#create_organization_membership) - Create a membership for a user, making them apart of an organization. Uses the user's current email address.
* [get_default_membership_for_email](#get_default_membership_for_email) - Get the default membership for a user.
* [get_memberships](#get_memberships) - Get memberships for a user.
* [get_memberships_by_email](#get_memberships_by_email) - Get memberships for a user given that user's email address.
* [get_memberships_by_org](#get_memberships_by_org) - Get memberships for an org.
* [list_organization_memberships](#list_organization_memberships) - List organization memberships
* [remove_membership_by_email](#remove_membership_by_email) - Removes membership in a given org from a user, using the user's email address.
* [remove_organization_membership](#remove_organization_membership) - Removes membership in a given org from a user, using the user's email address.
* [set_default_membership](#set_default_membership) - Sets the organization that should be used when logging a user in
* [update_membership_by_email](#update_membership_by_email) - Updates the role in an membership
* [update_organization_membership](#update_organization_membership) - Updates the role in an membership

## create_membership

Create a membership for a user, making them apart of an organization. Uses the user's current email address.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.AddMembershipRequest(
    created_by='non',
    default=False,
    email='Elyssa_Tillman58@yahoo.com',
    org_id='nam',
    role=shared.Role.MEMBER,
)

res = s.membership.create_membership(req, operations.CreateMembershipSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## create_organization_membership

Create a membership for a user, making them apart of an organization. Uses the user's current email address.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.CreateOrganizationMembershipRequest(
    email='user@whylabs.ai',
    org_id='org-123',
    role=shared.Role.MEMBER,
    set_default=False,
)

res = s.membership.create_organization_membership(req, operations.CreateOrganizationMembershipSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
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
    email='Verlie.Feeney@yahoo.com',
)

res = s.membership.get_default_membership_for_email(req, operations.GetDefaultMembershipForEmailSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
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
    user_id='vel',
)

res = s.membership.get_memberships(req, operations.GetMembershipsSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
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
    email='Lenna47@yahoo.com',
)

res = s.membership.get_memberships_by_email(req, operations.GetMembershipsByEmailSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
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
    org_id='magnam',
)

res = s.membership.get_memberships_by_org(req, operations.GetMembershipsByOrgSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## list_organization_memberships

list memberships for an organization

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.ListOrganizationMembershipsRequest(
    org_id='org-123',
)

res = s.membership.list_organization_memberships(req, operations.ListOrganizationMembershipsSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
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
    email='Maggie38@hotmail.com',
    org_id='natus',
)

res = s.membership.remove_membership_by_email(req, operations.RemoveMembershipByEmailSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## remove_organization_membership

Removes membership in a given org from a user, using the user's email address.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.RemoveOrganizationMembershipRequest(
    email='user@whylabs.ai',
    org_id='org-123',
)

res = s.membership.remove_organization_membership(req, operations.RemoveOrganizationMembershipSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
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
    org_id='nobis',
    user_id='eum',
)

res = s.membership.set_default_membership(req, operations.SetDefaultMembershipSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
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
    email='Brice9@hotmail.com',
    org_id='excepturi',
    role=shared.Role.MEMBER,
)

res = s.membership.update_membership_by_email(req, operations.UpdateMembershipByEmailSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## update_organization_membership

Updates the role in an membership, given the organization and the user's email address.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.UpdateOrganizationMembershipRequest(
    email='user@whylabs.ai',
    org_id='org-123',
    role=shared.Role.MEMBER,
)

res = s.membership.update_organization_membership(req, operations.UpdateOrganizationMembershipSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```
