# debug_events

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
        content='laboriosam',
        creation_timestamp=943749,
        dataset_timestamp=902599,
        segment=shared.Segment(
            tags=[
                shared.SegmentTag(
                    key='in',
                    value='corporis',
                ),
                shared.SegmentTag(
                    key='iste',
                    value='iure',
                ),
                shared.SegmentTag(
                    key='saepe',
                    value='quidem',
                ),
            ],
        ),
        tags=[
            'ipsa',
        ],
        trace_id='reiciendis',
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

