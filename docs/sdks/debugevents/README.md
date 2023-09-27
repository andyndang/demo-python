# DebugEvents
(*debug_events*)

### Available Operations

* [log_debug_event](#log_debug_event) - Log a debug event

## log_debug_event

Create a debug event.
        

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.LogDebugEventRequest(
    debug_event=shared.DebugEvent(
        content='officia',
        creation_timestamp=582020,
        dataset_timestamp=143353,
        segment=shared.Segment(
            tags=[
                shared.SegmentTag(
                    key='deleniti',
                    value='hic',
                ),
            ],
        ),
        tags=[
            'optio',
        ],
        trace_id='totam',
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.debug_events.log_debug_event(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.LogDebugEventRequest](../../models/operations/logdebugeventrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.LogDebugEventResponse](../../models/operations/logdebugeventresponse.md)**

