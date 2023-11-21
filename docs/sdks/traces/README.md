# Traces
(*traces*)

### Available Operations

* [export_traces_json](#export_traces_json) - Export traces into WhyLabs
* [export_traces_raw](#export_traces_raw) - Export traces into WhyLabs

## export_traces_json

API to export traces into WhyLabs

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="",
)

req = operations.ExportTracesJSONRequest(
    request_body=[
        'string',
    ],
    x_whylabs_resource='resource-1',
)

res = s.traces.export_traces_json(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ExportTracesJSONRequest](../../models/operations/exporttracesjsonrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ExportTracesJSONResponse](../../models/operations/exporttracesjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## export_traces_raw

API to export traces into WhyLabs

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="",
)

req = operations.ExportTracesRawRequest(
    request_body='0x13AeB07844'.encode(),
    x_whylabs_resource='resource-1',
)

res = s.traces.export_traces_raw(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ExportTracesRawRequest](../../models/operations/exporttracesrawrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.ExportTracesRawResponse](../../models/operations/exporttracesrawresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
