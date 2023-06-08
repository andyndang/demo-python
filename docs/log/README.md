# log

### Available Operations

* [log_async](#log_async) - Like /log, except this api doesn't take the actual profile content. It returns an upload link that can be used to upload the profile to.
* [log_reference](#log_reference) - Returns a presigned URL for uploading the reference profile to.

## log_async

Like /log, except this api doesn't take the actual profile content. It returns an upload link that can be used to upload the profile to.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.LogAsyncRequest(
    log_async_request=shared.LogAsyncRequest(
        dataset_timestamp=978571,
        segment_tags=[
            shared.SegmentTag(
                key='dicta',
                value='magnam',
            ),
            shared.SegmentTag(
                key='cumque',
                value='facere',
            ),
            shared.SegmentTag(
                key='ea',
                value='aliquid',
            ),
        ],
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.log.log_async(req, operations.LogAsyncSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

## log_reference

Reference profiles can be used for.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.LogReferenceRequest(
    log_reference_request=shared.LogReferenceRequest(
        alias='laborum',
        dataset_timestamp=881104,
    ),
    model_id='model-123',
    org_id='org-123',
)

res = s.log.log_reference(req, operations.LogReferenceSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```
