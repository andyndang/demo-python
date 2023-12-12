# User
(*user*)

### Available Operations

* [create_user](#create_user) - Create a user.
* [get_user](#get_user) - Get a user by their id.
* [get_user_by_email](#get_user_by_email) - Get a user by their email.
* [update_user](#update_user) - Update a user.

## create_user

Create a user.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.CreateUserRequest(
    email='Richie.Kuhic95@yahoo.com',
)

res = s.user.create_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.CreateUserRequest](../../models/shared/createuserrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateUserResponse](../../models/operations/createuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_user

Get a user by their id.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetUserRequest(
    user_id='string',
)

res = s.user.get_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetUserRequest](../../models/operations/getuserrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetUserResponse](../../models/operations/getuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_user_by_email

Get a user by their email.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetUserByEmailRequest(
    email='Chauncey12@yahoo.com',
)

res = s.user.get_user_by_email(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetUserByEmailRequest](../../models/operations/getuserbyemailrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetUserByEmailResponse](../../models/operations/getuserbyemailresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## update_user

Update a user.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.User(
    email='Madison.Jacobi47@yahoo.com',
    user_id='string',
)

res = s.user.update_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.User](../../models/shared/user.md) | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.UpdateUserResponse](../../models/operations/updateuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
