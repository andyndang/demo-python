# DebugEvents

### Available Operations

* [log_debug_event](#log_debug_event) - Log a debug event

## log_debug_event

Create a debug event.
        

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.LogDebugEventRequest(
    debug_event=shared.DebugEvent(
        content='quod',
        creation_timestamp=461479,
        dataset_timestamp=520478,
        segment=shared.Segment(
            tags=[
                shared.SegmentTag(
                    key='porro',
                    value='dolorum',
                ),
            ],
        ),
        tags=[
            'dicta',
        ],
        trace_id='nam',
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.debug_events.log_debug_event(req, operations.LogDebugEventSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.LogDebugEventRequest](../../models/operations/logdebugeventrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.LogDebugEventSecurity](../../models/operations/logdebugeventsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.LogDebugEventResponse](../../models/operations/logdebugeventresponse.md)**

