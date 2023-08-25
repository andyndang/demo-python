# sessions

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

s = songbird.Songbird()

req = operations.BatchCreateReferenceProfileUploadRequest(
    batch_log_reference_request=shared.BatchLogReferenceRequest(
        references=[
            shared.LogReferenceRequest(
                alias='pariatur',
                dataset_timestamp=747080,
            ),
            shared.LogReferenceRequest(
                alias='dicta',
                dataset_timestamp=674848,
            ),
            shared.LogReferenceRequest(
                alias='totam',
                dataset_timestamp=276894,
            ),
            shared.LogReferenceRequest(
                alias='aspernatur',
                dataset_timestamp=174909,
            ),
        ],
    ),
    session_id='distinctio',
)

res = s.sessions.batch_create_reference_profile_upload(req)

if res.status_code == 200:
    # handle response
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
from songbird.models import operations

s = songbird.Songbird()

req = operations.ClaimGuestSessionRequest(
    org_id='facilis',
    session_id='aliquid',
)

res = s.sessions.claim_guest_session(req, operations.ClaimGuestSessionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ClaimGuestSessionRequest](../../models/operations/claimguestsessionrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.ClaimGuestSessionSecurity](../../models/operations/claimguestsessionsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.ClaimGuestSessionResponse](../../models/operations/claimguestsessionresponse.md)**


## create_dataset_profile_upload

Create an upload for a given session.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.CreateDatasetProfileUploadRequest(
    log_async_request=shared.LogAsyncRequest(
        dataset_timestamp=463150,
        segment_tags=[
            shared.SegmentTag(
                key='temporibus',
                value='qui',
            ),
            shared.SegmentTag(
                key='neque',
                value='fugit',
            ),
            shared.SegmentTag(
                key='magni',
                value='odio',
            ),
        ],
    ),
    session_id='sunt',
)

res = s.sessions.create_dataset_profile_upload(req)

if res.status_code == 200:
    # handle response
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

s = songbird.Songbird()

req = operations.CreateReferenceProfileUploadRequest(
    log_reference_request=shared.LogReferenceRequest(
        alias='ullam',
        dataset_timestamp=722081,
    ),
    session_id='hic',
)

res = s.sessions.create_reference_profile_upload(req)

if res.status_code == 200:
    # handle response
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

s = songbird.Songbird()

req = shared.CreateSessionRequest(
    user_id='voluptatem',
)

res = s.sessions.create_session(req)

if res.status_code == 200:
    # handle response
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
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetSessionRequest(
    session_id='cumque',
)

res = s.sessions.get_session(req, operations.GetSessionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetSessionRequest](../../models/operations/getsessionrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.GetSessionSecurity](../../models/operations/getsessionsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.GetSessionResponse](../../models/operations/getsessionresponse.md)**


## get_session_profile_observatory_link

Get observatory links for profiles in a given session. A max of 3 profiles can be viewed a a time.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.GetSessionProfileObservatoryLinkRequest(
    get_profile_observatory_link_request=shared.GetProfileObservatoryLinkRequest(
        batch_profile_timestamps=[
            748664,
            92596,
            903720,
        ],
        reference_profile_ids=[
            'veritatis',
        ],
    ),
    session_id='nobis',
)

res = s.sessions.get_session_profile_observatory_link(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetSessionProfileObservatoryLinkRequest](../../models/operations/getsessionprofileobservatorylinkrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.GetSessionProfileObservatoryLinkResponse](../../models/operations/getsessionprofileobservatorylinkresponse.md)**

