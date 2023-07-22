# admin

### Available Operations

* [generate_report](#generate_report) - Generate an admin report
* [post_monitor_config_validation_job](#post_monitor_config_validation_job) - Create a monitor config validation job for all configs

## generate_report

Generate an admin report

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.GenerateReportRequest(
    report_type=shared.AdminReportType.SESSIONS,
)

res = s.admin.generate_report(req, operations.GenerateReportSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GenerateReportRequest](../../models/operations/generatereportrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GenerateReportSecurity](../../models/operations/generatereportsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GenerateReportResponse](../../models/operations/generatereportresponse.md)**


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

