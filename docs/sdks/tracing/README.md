# Tracing
(*tracing*)

### Available Operations

* [post_traces_json](#post_traces_json) - Publish traces into WhyLabs
* [post_traces_raw](#post_traces_raw) - Publish traces into WhyLabs

## post_traces_json

API to publish traces into WhyLabs

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="",
)

req = operations.PostTracesJSONRequest(
    request_body=[
        'string',
    ],
    x_whylabs_resource='resource-1',
)

res = s.tracing.post_traces_json(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PostTracesJSONRequest](../../models/operations/posttracesjsonrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.PostTracesJSONResponse](../../models/operations/posttracesjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## post_traces_raw

API to publish traces into WhyLabs

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="",
)

req = operations.PostTracesRawRequest(
    request_body='0xBEA861Fc01'.encode(),
    x_whylabs_resource='resource-1',
)

res = s.tracing.post_traces_raw(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PostTracesRawRequest](../../models/operations/posttracesrawrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.PostTracesRawResponse](../../models/operations/posttracesrawresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
