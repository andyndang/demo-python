<!-- Start SDK Example Usage -->
```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.GenerateReportRequest(
    report_type=shared.AdminReportType.SESSIONS,
    time_period=shared.AdminReportTimePeriod.MONTH,
)

res = s.admin.generate_report(req, operations.GenerateReportSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->