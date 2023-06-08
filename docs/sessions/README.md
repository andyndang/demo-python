# sessions

### Available Operations

* [batch_create_reference_profile_upload](#batch_create_reference_profile_upload) - Create multiple reference profile uploads for a given session.
* [claim_guest_session](#claim_guest_session) - Claim a guest session, copying its model data into another org and expiring the session.
* [create_dataset_profile_upload](#create_dataset_profile_upload) - Create an upload for a given session.
* [create_reference_profile_upload](#create_reference_profile_upload) - Create a reference profile upload for a given session.
* [create_session](#create_session) - Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.
* [get_session](#get_session) - Get information about a session.

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
                alias='ipsa',
                dataset_timestamp=434417,
            ),
        ],
    ),
    session_id='odio',
)

res = s.sessions.batch_create_reference_profile_upload(req)

if res.status_code == 200:
    # handle response
```

## claim_guest_session

Claim a guest session, copying its model data into another org and expiring the session.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.ClaimGuestSessionRequest(
    org_id='quaerat',
    session_id='accusamus',
)

res = s.sessions.claim_guest_session(req, operations.ClaimGuestSessionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## create_dataset_profile_upload

Create an upload for a given session.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.CreateDatasetProfileUploadRequest(
    log_async_request=shared.LogAsyncRequest(
        dataset_timestamp=696344,
        segment_tags=[
            shared.SegmentTag(
                key='voluptas',
                value='natus',
            ),
            shared.SegmentTag(
                key='eos',
                value='atque',
            ),
            shared.SegmentTag(
                key='sit',
                value='fugiat',
            ),
            shared.SegmentTag(
                key='ab',
                value='soluta',
            ),
        ],
    ),
    session_id='dolorum',
)

res = s.sessions.create_dataset_profile_upload(req)

if res.status_code == 200:
    # handle response
```

## create_reference_profile_upload

Create a reference profile upload for a given session.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.CreateReferenceProfileUploadRequest(
    log_reference_request=shared.LogReferenceRequest(
        alias='iusto',
        dataset_timestamp=453697,
    ),
    session_id='dolorum',
)

res = s.sessions.create_reference_profile_upload(req)

if res.status_code == 200:
    # handle response
```

## create_session

Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird()

req = shared.CreateSessionRequest(
    user_id='deleniti',
)

res = s.sessions.create_session(req)

if res.status_code == 200:
    # handle response
```

## get_session

Get information about a session.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetSessionRequest(
    session_id='omnis',
)

res = s.sessions.get_session(req, operations.GetSessionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```
