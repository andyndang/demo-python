# Tracing
(*tracing*)

### Available Operations

* [post_spans_json](#post_spans_json) - Publish Spans into WhyLabs
* [post_spans_raw](#post_spans_raw) - Publish Spans into WhyLabs

## post_spans_json

API to publish Spans into WhyLabs

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="",
)

req = operations.PostSpansJSONRequest(
    request_body=[
        'string',
    ],
    x_whylabs_resource='resource-1',
)

res = s.tracing.post_spans_json(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PostSpansJSONRequest](../../models/operations/postspansjsonrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.PostSpansJSONResponse](../../models/operations/postspansjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## post_spans_raw

API to publish Spans into WhyLabs

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="",
)

req = operations.PostSpansRawRequest(
    request_body='0xacBf544EcA'.encode(),
    x_whylabs_resource='resource-1',
)

res = s.tracing.post_spans_raw(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PostSpansRawRequest](../../models/operations/postspansrawrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.PostSpansRawResponse](../../models/operations/postspansrawresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
