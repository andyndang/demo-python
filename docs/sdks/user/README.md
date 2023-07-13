# user

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
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.CreateUserRequest(
    email='Savion42@gmail.com',
)

res = s.user.create_user(req, operations.CreateUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.CreateUserRequest](../../models/shared/createuserrequest.md)           | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.CreateUserSecurity](../../models/operations/createusersecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.CreateUserResponse](../../models/operations/createuserresponse.md)**


## get_user

Get a user by their id.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetUserRequest(
    user_id='quod',
)

res = s.user.get_user(req, operations.GetUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetUserRequest](../../models/operations/getuserrequest.md)   | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `security`                                                               | [operations.GetUserSecurity](../../models/operations/getusersecurity.md) | :heavy_check_mark:                                                       | The security requirements to use for the request.                        |


### Response

**[operations.GetUserResponse](../../models/operations/getuserresponse.md)**


## get_user_by_email

Get a user by their email.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetUserByEmailRequest(
    email='Christophe.Parisian68@hotmail.com',
)

res = s.user.get_user_by_email(req, operations.GetUserByEmailSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetUserByEmailRequest](../../models/operations/getuserbyemailrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GetUserByEmailSecurity](../../models/operations/getuserbyemailsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GetUserByEmailResponse](../../models/operations/getuserbyemailresponse.md)**


## update_user

Update a user.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.User(
    email='Cruz.Schamberger73@yahoo.com',
    preferences='accusamus',
    user_id='numquam',
)

res = s.user.update_user(req, operations.UpdateUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.User](../../models/shared/user.md)                                     | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.UpdateUserSecurity](../../models/operations/updateusersecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.UpdateUserResponse](../../models/operations/updateuserresponse.md)**

