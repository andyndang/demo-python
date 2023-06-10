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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateAPIKeyRequest](../../models/operations/createapikeyrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.CreateAPIKeySecurity](../../models/operations/createapikeysecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.CreateAPIKeyResponse](../../models/operations/createapikeyresponse.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetAPIKeyRequest](../../models/operations/getapikeyrequest.md)   | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `security`                                                                   | [operations.GetAPIKeySecurity](../../models/operations/getapikeysecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.GetAPIKeyResponse](../../models/operations/getapikeyresponse.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListAPIKeysRequest](../../models/operations/listapikeysrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.ListAPIKeysSecurity](../../models/operations/listapikeyssecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.ListAPIKeysResponse](../../models/operations/listapikeysresponse.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RevokeAPIKeyRequest](../../models/operations/revokeapikeyrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.RevokeAPIKeySecurity](../../models/operations/revokeapikeysecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.RevokeAPIKeyResponse](../../models/operations/revokeapikeyresponse.md)**

