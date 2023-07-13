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
    created_by='omnis',
    default=False,
    email='Aileen71@yahoo.com',
    org_id='id',
    role=shared.Role.ADMIN,
)

res = s.membership.create_membership(req, operations.CreateMembershipSecurity(
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
    role=shared.Role.ADMIN,
    set_default=False,
)

res = s.membership.create_organization_membership(req, operations.CreateOrganizationMembershipSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.CreateOrganizationMembershipRequest](../../models/operations/createorganizationmembershiprequest.md)   | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `security`                                                                                                         | [operations.CreateOrganizationMembershipSecurity](../../models/operations/createorganizationmembershipsecurity.md) | :heavy_check_mark:                                                                                                 | The security requirements to use for the request.                                                                  |


### Response

**[operations.CreateOrganizationMembershipResponse](../../models/operations/createorganizationmembershipresponse.md)**


## get_default_membership_for_email

Get the default membership for a user.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetDefaultMembershipForEmailRequest(
    email='Liana_Rohan@yahoo.com',
)

res = s.membership.get_default_membership_for_email(req, operations.GetDefaultMembershipForEmailSecurity(
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


## get_memberships

Get memberships for a user.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetMembershipsRequest(
    user_id='aspernatur',
)

res = s.membership.get_memberships(req, operations.GetMembershipsSecurity(
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
    email='Eliane.Bosco@gmail.com',
)

res = s.membership.get_memberships_by_email(req, operations.GetMembershipsByEmailSecurity(
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
    org_id='provident',
)

res = s.membership.get_memberships_by_org(req, operations.GetMembershipsByOrgSecurity(
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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.ListOrganizationMembershipsRequest](../../models/operations/listorganizationmembershipsrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.ListOrganizationMembershipsSecurity](../../models/operations/listorganizationmembershipssecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.ListOrganizationMembershipsResponse](../../models/operations/listorganizationmembershipsresponse.md)**


## remove_membership_by_email

Removes membership in a given org from a user, using the user's email address.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.RemoveMembershipRequest(
    email='Kiley_Bartoletti@yahoo.com',
    org_id='mollitia',
)

res = s.membership.remove_membership_by_email(req, operations.RemoveMembershipByEmailSecurity(
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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.RemoveOrganizationMembershipRequest](../../models/operations/removeorganizationmembershiprequest.md)   | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `security`                                                                                                         | [operations.RemoveOrganizationMembershipSecurity](../../models/operations/removeorganizationmembershipsecurity.md) | :heavy_check_mark:                                                                                                 | The security requirements to use for the request.                                                                  |


### Response

**[operations.RemoveOrganizationMembershipResponse](../../models/operations/removeorganizationmembershipresponse.md)**


## set_default_membership

Sets the organization that should be used when logging a user in

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.SetDefaultMembershipRequest(
    org_id='ad',
    user_id='eum',
)

res = s.membership.set_default_membership(req, operations.SetDefaultMembershipSecurity(
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


## update_membership_by_email

Updates the role in an membership, given the organization and the user's email address.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.UpdateMembershipRequest(
    email='Sophie.Connelly@gmail.com',
    org_id='iure',
    role=shared.Role.VIEWER,
)

res = s.membership.update_membership_by_email(req, operations.UpdateMembershipByEmailSecurity(
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
    role=shared.Role.VIEWER,
)

res = s.membership.update_organization_membership(req, operations.UpdateOrganizationMembershipSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.UpdateOrganizationMembershipRequest](../../models/operations/updateorganizationmembershiprequest.md)   | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `security`                                                                                                         | [operations.UpdateOrganizationMembershipSecurity](../../models/operations/updateorganizationmembershipsecurity.md) | :heavy_check_mark:                                                                                                 | The security requirements to use for the request.                                                                  |


### Response

**[operations.UpdateOrganizationMembershipResponse](../../models/operations/updateorganizationmembershipresponse.md)**

