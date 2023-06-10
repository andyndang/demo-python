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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.DeleteAnalyzerRequest](../../models/operations/deleteanalyzerrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.DeleteAnalyzerSecurity](../../models/operations/deleteanalyzersecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.DeleteAnalyzerResponse](../../models/operations/deleteanalyzerresponse.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteMonitorRequest](../../models/operations/deletemonitorrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.DeleteMonitorSecurity](../../models/operations/deletemonitorsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.DeleteMonitorResponse](../../models/operations/deletemonitorresponse.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetAnalyzerRequest](../../models/operations/getanalyzerrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.GetAnalyzerSecurity](../../models/operations/getanalyzersecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.GetAnalyzerResponse](../../models/operations/getanalyzerresponse.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetMonitorRequest](../../models/operations/getmonitorrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.GetMonitorSecurity](../../models/operations/getmonitorsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.GetMonitorResponse](../../models/operations/getmonitorresponse.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetMonitorConfigV3Request](../../models/operations/getmonitorconfigv3request.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.GetMonitorConfigV3Security](../../models/operations/getmonitorconfigv3security.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.GetMonitorConfigV3Response](../../models/operations/getmonitorconfigv3response.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetMonitorConfigV3VersionRequest](../../models/operations/getmonitorconfigv3versionrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.GetMonitorConfigV3VersionSecurity](../../models/operations/getmonitorconfigv3versionsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.GetMonitorConfigV3VersionResponse](../../models/operations/getmonitorconfigv3versionresponse.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.ListMonitorConfigV3VersionsRequest](../../models/operations/listmonitorconfigv3versionsrequest.md)   | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `security`                                                                                                       | [operations.ListMonitorConfigV3VersionsSecurity](../../models/operations/listmonitorconfigv3versionssecurity.md) | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |


### Response

**[operations.ListMonitorConfigV3VersionsResponse](../../models/operations/listmonitorconfigv3versionsresponse.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PatchMonitorConfigV3Request](../../models/operations/patchmonitorconfigv3request.md)   | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [operations.PatchMonitorConfigV3Security](../../models/operations/patchmonitorconfigv3security.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |


### Response

**[operations.PatchMonitorConfigV3Response](../../models/operations/patchmonitorconfigv3response.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PutAnalyzerRequest](../../models/operations/putanalyzerrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.PutAnalyzerSecurity](../../models/operations/putanalyzersecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.PutAnalyzerResponse](../../models/operations/putanalyzerresponse.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.PutMonitorRequest](../../models/operations/putmonitorrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.PutMonitorSecurity](../../models/operations/putmonitorsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.PutMonitorResponse](../../models/operations/putmonitorresponse.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PutMonitorConfigV3Request](../../models/operations/putmonitorconfigv3request.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.PutMonitorConfigV3Security](../../models/operations/putmonitorconfigv3security.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.PutMonitorConfigV3Response](../../models/operations/putmonitorconfigv3response.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PutRequestMonitorRunConfigRequest](../../models/operations/putrequestmonitorrunconfigrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.PutRequestMonitorRunConfigSecurity](../../models/operations/putrequestmonitorrunconfigsecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.PutRequestMonitorRunConfigResponse](../../models/operations/putrequestmonitorrunconfigresponse.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ValidateMonitorConfigV3Request](../../models/operations/validatemonitorconfigv3request.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.ValidateMonitorConfigV3Security](../../models/operations/validatemonitorconfigv3security.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.ValidateMonitorConfigV3Response](../../models/operations/validatemonitorconfigv3response.md)**

