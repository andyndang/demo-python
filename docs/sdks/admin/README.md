# admin

### Available Operations

* [post_monitor_config_validation_job](#post_monitor_config_validation_job) - Create a monitor config validation job for all configs

## post_monitor_config_validation_job

Create a monitor config validation job for all configs

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()


res = s.admin.post_monitor_config_validation_job(operations.PostMonitorConfigValidationJobSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                             | [operations.PostMonitorConfigValidationJobSecurity](../../models/operations/postmonitorconfigvalidationjobsecurity.md) | :heavy_check_mark:                                                                                                     | The security requirements to use for the request.                                                                      |


### Response

**[operations.PostMonitorConfigValidationJobResponse](../../models/operations/postmonitorconfigvalidationjobresponse.md)**

