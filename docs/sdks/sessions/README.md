# Sessions
(*sessions*)

### Available Operations

* [batch_create_reference_profile_upload](#batch_create_reference_profile_upload) - Create multiple reference profile uploads for a given session.
* [claim_guest_session](#claim_guest_session) - Claim a guest session, copying its model data into another org and expiring the session.
* [create_dataset_profile_upload](#create_dataset_profile_upload) - Create an upload for a given session.
* [create_reference_profile_upload](#create_reference_profile_upload) - Create a reference profile upload for a given session.
* [create_session](#create_session) - Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.
* [get_session](#get_session) - Get information about a session.
* [get_session_profile_observatory_link](#get_session_profile_observatory_link) - Get observatory links for profiles in a given session. A max of 3 profiles can be viewed a a time.

## batch_create_reference_profile_upload

Create multiple reference profile uploads for a given session.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.BatchCreateReferenceProfileUploadRequest(
    batch_log_reference_request=shared.BatchLogReferenceRequest(
        references=[
            shared.LogReferenceRequest(),
        ],
    ),
    session_id='string',
)

res = s.sessions.batch_create_reference_profile_upload(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.BatchCreateReferenceProfileUploadRequest](../../models/operations/batchcreatereferenceprofileuploadrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.BatchCreateReferenceProfileUploadResponse](../../models/operations/batchcreatereferenceprofileuploadresponse.md)**


## claim_guest_session

Claim a guest session, copying its model data into another org and expiring the session.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.ClaimGuestSessionRequest(
    org_id='string',
    session_id='string',
)

res = s.sessions.claim_guest_session(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ClaimGuestSessionRequest](../../models/operations/claimguestsessionrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.ClaimGuestSessionResponse](../../models/operations/claimguestsessionresponse.md)**


## create_dataset_profile_upload

Create an upload for a given session.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.CreateDatasetProfileUploadRequest(
    log_async_request=shared.LogAsyncRequest(
        segment_tags=[
            shared.SegmentTag(),
        ],
    ),
    session_id='string',
)

res = s.sessions.create_dataset_profile_upload(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.CreateDatasetProfileUploadRequest](../../models/operations/createdatasetprofileuploadrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.CreateDatasetProfileUploadResponse](../../models/operations/createdatasetprofileuploadresponse.md)**


## create_reference_profile_upload

Create a reference profile upload for a given session.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.CreateReferenceProfileUploadRequest(
    log_reference_request=shared.LogReferenceRequest(),
    session_id='string',
)

res = s.sessions.create_reference_profile_upload(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.CreateReferenceProfileUploadRequest](../../models/operations/createreferenceprofileuploadrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.CreateReferenceProfileUploadResponse](../../models/operations/createreferenceprofileuploadresponse.md)**


## create_session

Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.CreateSessionRequest(
    user_id='string',
)

res = s.sessions.create_session(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.CreateSessionRequest](../../models/shared/createsessionrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CreateSessionResponse](../../models/operations/createsessionresponse.md)**


## get_session

Get information about a session.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.GetSessionRequest(
    session_id='string',
)

res = s.sessions.get_session(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetSessionRequest](../../models/operations/getsessionrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetSessionResponse](../../models/operations/getsessionresponse.md)**


## get_session_profile_observatory_link

Get observatory links for profiles in a given session. A max of 3 profiles can be viewed a a time.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.GetSessionProfileObservatoryLinkRequest(
    get_profile_observatory_link_request=shared.GetProfileObservatoryLinkRequest(
        batch_profile_timestamps=[
            495187,
        ],
        reference_profile_ids=[
            'string',
        ],
    ),
    session_id='string',
)

res = s.sessions.get_session_profile_observatory_link(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetSessionProfileObservatoryLinkRequest](../../models/operations/getsessionprofileobservatorylinkrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.GetSessionProfileObservatoryLinkResponse](../../models/operations/getsessionprofileobservatorylinkresponse.md)**

