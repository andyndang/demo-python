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
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.LogDebugEventRequest(
    debug_event=shared.DebugEvent(
        segment=shared.Segment(
            tags=[
                shared.SegmentTag(
                    key='<key>',
                    value='string',
                ),
            ],
        ),
        tags=[
            'string',
        ],
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.debug_events.log_debug_event(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.LogDebugEventRequest](../../models/operations/logdebugeventrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.LogDebugEventResponse](../../models/operations/logdebugeventresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
