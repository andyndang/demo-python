# Databricks

### Available Operations

* [get_connection](#get_connection) - Get the connection metadata for a given org
* [list_jobs](#list_jobs) - List all of the jobs in a workspace.
* [refresh_connection](#refresh_connection) - Refresh metadata for a workspace connection.
* [run_job](#run_job) - Run an existing job in a given databricks workspace.
* [update_connection](#update_connection) - Update the connection metadata for a given org

## get_connection

Get the connection metadata for a given org

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.GetConnectionRequest(
    org_id='veritatis',
    workspace_id='deserunt',
)

res = s.databricks.get_connection(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.GetConnectionRequest](../../models/shared/getconnectionrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetConnectionResponse](../../models/operations/getconnectionresponse.md)**


## list_jobs

List all of the jobs in a workspace.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.ListJobsRequest(
    org_id='perferendis',
    workspace_id='ipsam',
)

res = s.databricks.list_jobs(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [shared.ListJobsRequest](../../models/shared/listjobsrequest.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.ListJobsResponse](../../models/operations/listjobsresponse.md)**


## refresh_connection

Refresh metadata for a workspace connection.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.RefreshConnectionRequest(
    org_id='repellendus',
    workspace_id='sapiente',
)

res = s.databricks.refresh_connection(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.RefreshConnectionRequest](../../models/shared/refreshconnectionrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.RefreshConnectionResponse](../../models/operations/refreshconnectionresponse.md)**


## run_job

Run an existing job in a given databricks workspace.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.RunJobRequest(
    job_id=778157,
    org_id='odit',
    workspace_id='at',
)

res = s.databricks.run_job(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.RunJobRequest](../../models/shared/runjobrequest.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.RunJobResponse](../../models/operations/runjobresponse.md)**


## update_connection

Update the connection metadata for a given org

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.UpdateConnectionRequest(
    changes=shared.UpdateConnectionChanges(
        connected=False,
        demo=False,
        org_id='at',
    ),
    org_id='maiores',
    workspace_id='molestiae',
)

res = s.databricks.update_connection(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.UpdateConnectionRequest](../../models/shared/updateconnectionrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateConnectionResponse](../../models/operations/updateconnectionresponse.md)**

