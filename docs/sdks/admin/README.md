# Admin
(*admin*)

### Available Operations

* [generate_report](#generate_report) - Generate an admin report
* [post_monitor_config_validation_job](#post_monitor_config_validation_job) - Create a monitor config validation job for all configs

## generate_report

Generate an admin report

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.GenerateReportRequest(
    report_type=shared.AdminReportType.SESSIONS,
)

res = s.admin.generate_report(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GenerateReportRequest](../../models/operations/generatereportrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GenerateReportResponse](../../models/operations/generatereportresponse.md)**


## post_monitor_config_validation_job

Create a monitor config validation job for all configs

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.admin.post_monitor_config_validation_job()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.PostMonitorConfigValidationJobResponse](../../models/operations/postmonitorconfigvalidationjobresponse.md)**

