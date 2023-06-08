# schema

### Available Operations

* [get_monitor_config_schema](#get_monitor_config_schema) - Get the current supported schema of the monitor configuration

## get_monitor_config_schema

Get the current supported schema of the  monitor configuration

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetMonitorConfigSchemaRequest(
    org_id='org-123',
)

res = s.schema.get_monitor_config_schema(req, operations.GetMonitorConfigSchemaSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```
