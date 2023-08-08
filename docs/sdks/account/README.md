# account

### Available Operations

* [create_account_user](#create_account_user) - Create an account user
* [delete_account_user](#delete_account_user) - Delete account user
* [get_account_memberships](#get_account_memberships) - Get memberships in an account
* [get_account_users](#get_account_users) - Get users in an account
* [get_org_role_memberships](#get_org_role_memberships) - Get memberships for a specific org and role
* [patch_org_role_memberships](#patch_org_role_memberships) - Add or delete memberships in a specific role and managed organization
* [put_org_role_memberships](#put_org_role_memberships) - Replace the memberships in a specific role and managed organization
* [update_account_user](#update_account_user) - Update account user

## create_account_user

Create an account user

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.CreateAccountUserRequest(
    request_body=operations.CreateAccountUserRequestBody(
        user=shared.AccountUser(
            active=False,
            email='Linda.Oberbrunner@yahoo.com',
            external_id='magnam',
            user_id='debitis',
        ),
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
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetAccountMembershipsRequest(
    org_id='org-123',
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


## get_account_users

Get users in the account organization and any managed organizations

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetAccountUsersRequest(
    email='user@whylabs.ai',
    org_id='org-123',
    user_id='user-123',
)

res = s.account.get_account_users(req, operations.GetAccountUsersSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetAccountUsersRequest](../../models/operations/getaccountusersrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.GetAccountUsersSecurity](../../models/operations/getaccountuserssecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.GetAccountUsersResponse](../../models/operations/getaccountusersresponse.md)**


## get_org_role_memberships

Get memberships in a specific organization and role within the account

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetOrgRoleMembershipsRequest(
    managed_org_id='org-123',
    org_id='org-123',
    role='admin',
)

res = s.account.get_org_role_memberships(req, operations.GetOrgRoleMembershipsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetOrgRoleMembershipsRequest](../../models/operations/getorgrolemembershipsrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.GetOrgRoleMembershipsSecurity](../../models/operations/getorgrolemembershipssecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.GetOrgRoleMembershipsResponse](../../models/operations/getorgrolemembershipsresponse.md)**


## patch_org_role_memberships

Add or delete all of the memberships in a specific role and managed organization

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.PatchOrgRoleMembershipsRequest(
    request_body=operations.PatchOrgRoleMembershipsRequestBody(
        request=shared.PatchAccountMembershipsRequest(
            user_ids_to_add=[
                'delectus',
            ],
            user_ids_to_delete=[
                'suscipit',
                'molestiae',
            ],
        ),
    ),
    managed_org_id='org-123',
    org_id='org-123',
    role='admin',
)

res = s.account.patch_org_role_memberships(req, operations.PatchOrgRoleMembershipsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.PatchOrgRoleMembershipsRequest](../../models/operations/patchorgrolemembershipsrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.PatchOrgRoleMembershipsSecurity](../../models/operations/patchorgrolemembershipssecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.PatchOrgRoleMembershipsResponse](../../models/operations/patchorgrolemembershipsresponse.md)**


## put_org_role_memberships

Replace all of the memberships in a specific role and managed organization

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.PutOrgRoleMembershipsRequest(
    request_body=operations.PutOrgRoleMembershipsRequestBody(
        request=shared.PutAccountMembershipsRequest(
            user_ids=[
                'placeat',
                'voluptatum',
                'iusto',
                'excepturi',
            ],
        ),
    ),
    managed_org_id='org-123',
    org_id='org-123',
    role='admin',
)

res = s.account.put_org_role_memberships(req, operations.PutOrgRoleMembershipsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PutOrgRoleMembershipsRequest](../../models/operations/putorgrolemembershipsrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.PutOrgRoleMembershipsSecurity](../../models/operations/putorgrolemembershipssecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.PutOrgRoleMembershipsResponse](../../models/operations/putorgrolemembershipsresponse.md)**


## update_account_user

Update an account user's details

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.UpdateAccountUserRequest(
    request_body=operations.UpdateAccountUserRequestBody(
        user=shared.AccountUser(
            active=False,
            email='Tianna33@yahoo.com',
            external_id='veritatis',
            user_id='deserunt',
        ),
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

