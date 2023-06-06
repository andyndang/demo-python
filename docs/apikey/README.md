# api_key

### Available Operations

* [create_api_key](#create_api_key) - Generate an API key for a user.
* [get_api_key](#get_api_key) - Get an api key by its id
* [list_api_keys](#list_api_keys) - List API key metadata for a given organization and user
* [revoke_api_key](#revoke_api_key) - Revoke the given API Key, removing its ability to access WhyLabs systems

## create_api_key

Generates an API key for a given user. Must be called either by system administrator or by the user themselves

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.CreateAPIKeyRequest(
    alias='MLApplicationName',
    expiration_time=1577836800000,
    org_id='org-123',
    scopes=[
        ':user',
        ':user',
        ':user',
    ],
    user_id='user-123',
)

res = s.api_key.create_api_key(req, operations.CreateAPIKeySecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## get_api_key

Get an api key by its id

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetAPIKeyRequest(
    key_id='fh4dUNV3WQ',
    org_id='org-123',
)

res = s.api_key.get_api_key(req, operations.GetAPIKeySecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## list_api_keys

Returns the API key metadata for a given organization and user

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.ListAPIKeysRequest(
    org_id='org-123',
    user_id='user-123',
)

res = s.api_key.list_api_keys(req, operations.ListAPIKeysSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## revoke_api_key

Revokes the given API Key

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.RevokeAPIKeyRequest(
    key_id='HMiFAgQeNb',
    org_id='org-123',
    user_id='user-123',
)

res = s.api_key.revoke_api_key(req, operations.RevokeAPIKeySecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```
