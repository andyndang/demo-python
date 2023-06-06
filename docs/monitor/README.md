# monitor

### Available Operations

* [delete_analyzer](#delete_analyzer) - Delete the analyzer config for a given dataset.
* [delete_monitor](#delete_monitor) - Delete the monitor for a given dataset.
* [get_analyzer](#get_analyzer) - Get the analyzer config for a given dataset.
* [get_monitor](#get_monitor) - Get the monitor config for a given dataset.
* [get_monitor_config_v3](#get_monitor_config_v3) - Get the monitor config document for a given dataset.
* [get_monitor_config_v3_version](#get_monitor_config_v3_version) - Get the monitor config document version for a given dataset.
* [list_monitor_config_v3_versions](#list_monitor_config_v3_versions) - List the monitor config document versions for a given dataset.
* [patch_monitor_config_v3](#patch_monitor_config_v3) - Patch an updated monitor config document for a given dataset.
* [put_analyzer](#put_analyzer) - Save the analyzer config for a given dataset.
* [put_monitor](#put_monitor) - Save the monitor for a given dataset.
* [put_monitor_config_v3](#put_monitor_config_v3) - Save the monitor config document for a given dataset.
* [put_request_monitor_run_config](#put_request_monitor_run_config) - Put the RequestMonitorRun config into S3.
* [validate_monitor_config_v3](#validate_monitor_config_v3) - Validate the monitor config document for a given dataset.

## delete_analyzer

Delete the analyzer config for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.DeleteAnalyzerRequest(
    analyzer_id='drift-analyzer',
    dataset_id='model-123',
    org_id='org-123',
)

res = s.monitor.delete_analyzer(req, operations.DeleteAnalyzerSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## delete_monitor

Delete the monitor for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.DeleteMonitorRequest(
    dataset_id='model-123',
    monitor_id='drift-monitor-123',
    org_id='org-123',
)

res = s.monitor.delete_monitor(req, operations.DeleteMonitorSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## get_analyzer

Get the analyzer config for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetAnalyzerRequest(
    analyzer_id='drift-analyzer',
    dataset_id='model-123',
    org_id='org-123',
)

res = s.monitor.get_analyzer(req, operations.GetAnalyzerSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## get_monitor

Get the monitor config for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetMonitorRequest(
    dataset_id='model-123',
    monitor_id='drift-monitor-123',
    org_id='org-123',
)

res = s.monitor.get_monitor(req, operations.GetMonitorSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## get_monitor_config_v3

Get the monitor config document for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetMonitorConfigV3Request(
    dataset_id='model-123',
    include_entity_schema=False,
    include_entity_weights=False,
    org_id='org-123',
)

res = s.monitor.get_monitor_config_v3(req, operations.GetMonitorConfigV3Security(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## get_monitor_config_v3_version

Get the monitor config document version for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetMonitorConfigV3VersionRequest(
    dataset_id='model-123',
    org_id='org-123',
    version_id='4920545486e2a4cdf0f770c09748e663',
)

res = s.monitor.get_monitor_config_v3_version(req, operations.GetMonitorConfigV3VersionSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## list_monitor_config_v3_versions

List the monitor config document versions for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.ListMonitorConfigV3VersionsRequest(
    dataset_id='model-123',
    org_id='org-123',
)

res = s.monitor.list_monitor_config_v3_versions(req, operations.ListMonitorConfigV3VersionsSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## patch_monitor_config_v3

Save an updated monitor config document for a given dataset.  Monitors and analyzers matching an existing ID are replaced.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.PatchMonitorConfigV3Request(
    request_body='odit',
    dataset_id='model-123',
    org_id='org-123',
)

res = s.monitor.patch_monitor_config_v3(req, operations.PatchMonitorConfigV3Security(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## put_analyzer

Save the analyzer config for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.PutAnalyzerRequest(
    request_body='nemo',
    analyzer_id='drift-analyzer',
    dataset_id='model-123',
    org_id='org-123',
)

res = s.monitor.put_analyzer(req, operations.PutAnalyzerSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## put_monitor

Save the monitor for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.PutMonitorRequest(
    request_body='quasi',
    dataset_id='model-123',
    monitor_id='drift-monitor-123',
    org_id='org-123',
)

res = s.monitor.put_monitor(req, operations.PutMonitorSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## put_monitor_config_v3

Save the monitor config document for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.PutMonitorConfigV3Request(
    request_body='iure',
    dataset_id='model-123',
    org_id='org-123',
)

res = s.monitor.put_monitor_config_v3(req, operations.PutMonitorConfigV3Security(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## put_request_monitor_run_config

Put the RequestMonitorRun config into S3.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.PutRequestMonitorRunConfigRequest(
    request_body=operations.PutRequestMonitorRunConfigRequestBody(
        analyzer_ids=[
            'debitis',
            'eius',
            'maxime',
            'deleniti',
        ],
        end_timestamp=1893456000000,
        overwrite=False,
        start_timestamp=1577836800000,
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.monitor.put_request_monitor_run_config(req, operations.PutRequestMonitorRunConfigSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## validate_monitor_config_v3

Validate the monitor config document for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.ValidateMonitorConfigV3Request(
    request_body='facilis',
    dataset_id='model-123',
    org_id='org-123',
    verbose=False,
)

res = s.monitor.validate_monitor_config_v3(req, operations.ValidateMonitorConfigV3Security(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```
