<!-- Start SDK Example Usage -->
```python
import songbird
from songbird.models import operations

s = songbird.Songbird()


res = s.admin.post_monitor_config_validation_job(operations.PostMonitorConfigValidationJobSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->