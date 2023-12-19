# Account
(*account*)

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

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
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

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateAccountUserRequest](../../models/operations/createaccountuserrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateAccountUserResponse](../../models/operations/createaccountuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_account_user

Delete an account user's details

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.DeleteAccountUserRequest(
    org_id='org-123',
    user_id='user-123',
)

res = s.account.delete_account_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteAccountUserRequest](../../models/operations/deleteaccountuserrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.DeleteAccountUserResponse](../../models/operations/deleteaccountuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_account_memberships

Get memberships in the account organization and any managed organizations

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetAccountMembershipsRequest(
    managed_org_id='org-123',
    org_id='org-123',
    user_id='user-123',
)

res = s.account.get_account_memberships(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAccountMembershipsRequest](../../models/operations/getaccountmembershipsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetAccountMembershipsResponse](../../models/operations/getaccountmembershipsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_account_user_by_email

Get account user by email

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetAccountUserByEmailRequest(
    email='user@whylabs.ai',
    org_id='org-123',
)

res = s.account.get_account_user_by_email(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetAccountUserByEmailRequest](../../models/operations/getaccountuserbyemailrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetAccountUserByEmailResponse](../../models/operations/getaccountuserbyemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_account_user_by_id

Get account user by user_id

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetAccountUserByIDRequest(
    org_id='org-123',
    user_id='user-123',
)

res = s.account.get_account_user_by_id(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAccountUserByIDRequest](../../models/operations/getaccountuserbyidrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetAccountUserByIDResponse](../../models/operations/getaccountuserbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_account_users

List users in the account organization and any managed organizations

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.ListAccountUsersRequest(
    org_id='org-123',
)

res = s.account.list_account_users(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListAccountUsersRequest](../../models/operations/listaccountusersrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListAccountUsersResponse](../../models/operations/listaccountusersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_managed_organizations

List managed organizations for a parent organization

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.ListManagedOrganizationsRequest(
    org_id='org-123',
)

res = s.account.list_managed_organizations(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListManagedOrganizationsRequest](../../models/operations/listmanagedorganizationsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.ListManagedOrganizationsResponse](../../models/operations/listmanagedorganizationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_organization_memberships

Add or delete all of the memberships in a specific role and managed organization

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.PatchOrganizationMembershipsRequest(
    patch_account_memberships_request=shared.PatchAccountMembershipsRequest(
        user_ids_to_add=[
            'string',
        ],
        user_ids_to_delete=[
            'string',
        ],
    ),
    managed_org_id='org-123',
    org_id='org-123',
    role=shared.Role.VIEWER,
)

res = s.account.patch_organization_memberships(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PatchOrganizationMembershipsRequest](../../models/operations/patchorganizationmembershipsrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PatchOrganizationMembershipsResponse](../../models/operations/patchorganizationmembershipsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_organization_memberships

Replace all of the memberships in a specific role and managed organization

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.PutOrganizationMembershipsRequest(
    put_account_memberships_request=shared.PutAccountMembershipsRequest(
        user_ids=[
            'string',
        ],
    ),
    managed_org_id='org-123',
    org_id='org-123',
    role=shared.Role.VIEWER,
)

res = s.account.put_organization_memberships(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.PutOrganizationMembershipsRequest](../../models/operations/putorganizationmembershipsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.PutOrganizationMembershipsResponse](../../models/operations/putorganizationmembershipsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_account_user

Update an account user's details

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.UpdateAccountUserRequest(
    update_account_user_request=shared.UpdateAccountUserRequest(),
    org_id='org-123',
    user_id='user-123',
)

res = s.account.update_account_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateAccountUserRequest](../../models/operations/updateaccountuserrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpdateAccountUserResponse](../../models/operations/updateaccountuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
