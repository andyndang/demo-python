# account

### Available Operations

* [create_account_user](#create_account_user) - Create an account user
* [delete_account_user](#delete_account_user) - Delete account user
* [get_account_memberships](#get_account_memberships) - Get memberships in an account
* [get_account_user_by_email](#get_account_user_by_email) - Get account user by email
* [get_account_user_by_id](#get_account_user_by_id) - Get account user by user_id
* [list_account_users](#list_account_users) - List users in an account
* [list_managed_organizations](#list_managed_organizations) - List managed organizations for a parent organization
* [patch_organization_memberships](#patch_organization_memberships) - Add or delete memberships in a specific role and managed organization
* [put_organization_memberships](#put_organization_memberships) - Replace the memberships in a specific role and managed organization
* [update_account_user](#update_account_user) - Update account user

## create_account_user

Create an account user

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.CreateAccountUserRequest(
    create_account_user_request=shared.CreateAccountUserRequest(
        active=False,
        email='Linda.Oberbrunner@yahoo.com',
        external_id='magnam',
        user_schema='debitis',
    ),
    org_id='org-123',
)

res = s.account.create_account_user(req, operations.CreateAccountUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateAccountUserRequest](../../models/operations/createaccountuserrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.CreateAccountUserSecurity](../../models/operations/createaccountusersecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.CreateAccountUserResponse](../../models/operations/createaccountuserresponse.md)**


## delete_account_user

Delete an account user's details

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.DeleteAccountUserRequest(
    org_id='org-123',
    user_id='user-123',
)

res = s.account.delete_account_user(req, operations.DeleteAccountUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.DeleteAccountUserRequest](../../models/operations/deleteaccountuserrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.DeleteAccountUserSecurity](../../models/operations/deleteaccountusersecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.DeleteAccountUserResponse](../../models/operations/deleteaccountuserresponse.md)**


## get_account_memberships

Get memberships in the account organization and any managed organizations

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.GetAccountMembershipsRequest(
    managed_org_id='org-123',
    org_id='org-123',
    role=shared.Role.ADMIN,
    user_id='user-123',
)

res = s.account.get_account_memberships(req, operations.GetAccountMembershipsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetAccountMembershipsRequest](../../models/operations/getaccountmembershipsrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.GetAccountMembershipsSecurity](../../models/operations/getaccountmembershipssecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.GetAccountMembershipsResponse](../../models/operations/getaccountmembershipsresponse.md)**


## get_account_user_by_email

Get account user by email

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetAccountUserByEmailRequest(
    email='user@whylabs.ai',
    org_id='org-123',
)

res = s.account.get_account_user_by_email(req, operations.GetAccountUserByEmailSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetAccountUserByEmailRequest](../../models/operations/getaccountuserbyemailrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.GetAccountUserByEmailSecurity](../../models/operations/getaccountuserbyemailsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.GetAccountUserByEmailResponse](../../models/operations/getaccountuserbyemailresponse.md)**


## get_account_user_by_id

Get account user by user_id

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetAccountUserByIDRequest(
    org_id='org-123',
    user_id='user-123',
)

res = s.account.get_account_user_by_id(req, operations.GetAccountUserByIDSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetAccountUserByIDRequest](../../models/operations/getaccountuserbyidrequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.GetAccountUserByIDSecurity](../../models/operations/getaccountuserbyidsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.GetAccountUserByIDResponse](../../models/operations/getaccountuserbyidresponse.md)**


## list_account_users

List users in the account organization and any managed organizations

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.ListAccountUsersRequest(
    org_id='org-123',
)

res = s.account.list_account_users(req, operations.ListAccountUsersSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ListAccountUsersRequest](../../models/operations/listaccountusersrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.ListAccountUsersSecurity](../../models/operations/listaccountuserssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.ListAccountUsersResponse](../../models/operations/listaccountusersresponse.md)**


## list_managed_organizations

List managed organizations for a parent organization

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.ListManagedOrganizationsRequest(
    org_id='org-123',
)

res = s.account.list_managed_organizations(req, operations.ListManagedOrganizationsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.ListManagedOrganizationsRequest](../../models/operations/listmanagedorganizationsrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.ListManagedOrganizationsSecurity](../../models/operations/listmanagedorganizationssecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.ListManagedOrganizationsResponse](../../models/operations/listmanagedorganizationsresponse.md)**


## patch_organization_memberships

Add or delete all of the memberships in a specific role and managed organization

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.PatchOrganizationMembershipsRequest(
    patch_account_memberships_request=shared.PatchAccountMembershipsRequest(
        user_ids_to_add=[
            'delectus',
        ],
        user_ids_to_delete=[
            'tempora',
        ],
    ),
    managed_org_id='org-123',
    org_id='org-123',
    role=shared.Role.MEMBER,
)

res = s.account.patch_organization_memberships(req, operations.PatchOrganizationMembershipsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.PatchOrganizationMembershipsRequest](../../models/operations/patchorganizationmembershipsrequest.md)   | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `security`                                                                                                         | [operations.PatchOrganizationMembershipsSecurity](../../models/operations/patchorganizationmembershipssecurity.md) | :heavy_check_mark:                                                                                                 | The security requirements to use for the request.                                                                  |


### Response

**[operations.PatchOrganizationMembershipsResponse](../../models/operations/patchorganizationmembershipsresponse.md)**


## put_organization_memberships

Replace all of the memberships in a specific role and managed organization

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.PutOrganizationMembershipsRequest(
    put_account_memberships_request=shared.PutAccountMembershipsRequest(
        user_ids=[
            'molestiae',
        ],
    ),
    managed_org_id='org-123',
    org_id='org-123',
    role=shared.Role.VIEWER,
)

res = s.account.put_organization_memberships(req, operations.PutOrganizationMembershipsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PutOrganizationMembershipsRequest](../../models/operations/putorganizationmembershipsrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.PutOrganizationMembershipsSecurity](../../models/operations/putorganizationmembershipssecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.PutOrganizationMembershipsResponse](../../models/operations/putorganizationmembershipsresponse.md)**


## update_account_user

Update an account user's details

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.UpdateAccountUserRequest(
    update_account_user_request=shared.UpdateAccountUserRequest(
        active=False,
        external_id='placeat',
        user_schema='voluptatum',
    ),
    org_id='org-123',
    user_id='user-123',
)

res = s.account.update_account_user(req, operations.UpdateAccountUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateAccountUserRequest](../../models/operations/updateaccountuserrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.UpdateAccountUserSecurity](../../models/operations/updateaccountusersecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.UpdateAccountUserResponse](../../models/operations/updateaccountuserresponse.md)**

