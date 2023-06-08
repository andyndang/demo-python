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
    email='Michaela.Zboncak@hotmail.com',
)

res = s.user.create_user(req, operations.CreateUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## get_user

Get a user by their id.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetUserRequest(
    user_id='voluptate',
)

res = s.user.get_user(req, operations.GetUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## get_user_by_email

Get a user by their email.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetUserByEmailRequest(
    email='Suzanne2@yahoo.com',
)

res = s.user.get_user_by_email(req, operations.GetUserByEmailSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## update_user

Update a user.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.User(
    email='Nils90@gmail.com',
    preferences='suscipit',
    user_id='deserunt',
)

res = s.user.update_user(req, operations.UpdateUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```
