# Schema
(*schema*)

### Available Operations

* [get_monitor_config_schema](#get_monitor_config_schema) - Get the current supported schema of the monitor configuration

## get_monitor_config_schema

Get the current supported schema of the  monitor configuration

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetMonitorConfigSchemaRequest(
    org_id='org-123',
)

res = s.schema.get_monitor_config_schema(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetMonitorConfigSchemaRequest](../../models/operations/getmonitorconfigschemarequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetMonitorConfigSchemaResponse](../../models/operations/getmonitorconfigschemaresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
