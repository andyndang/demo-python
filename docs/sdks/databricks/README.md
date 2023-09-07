# databricks

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
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.GetConnectionRequest(
    org_id='iusto',
    workspace_id='excepturi',
)

res = s.databricks.get_connection(req, operations.GetConnectionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.GetConnectionRequest](../../models/shared/getconnectionrequest.md)           | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.GetConnectionSecurity](../../models/operations/getconnectionsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.GetConnectionResponse](../../models/operations/getconnectionresponse.md)**


## list_jobs

List all of the jobs in a workspace.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.ListJobsRequest(
    org_id='nisi',
    workspace_id='recusandae',
)

res = s.databricks.list_jobs(req, operations.ListJobsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.ListJobsRequest](../../models/shared/listjobsrequest.md)           | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [operations.ListJobsSecurity](../../models/operations/listjobssecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |


### Response

**[operations.ListJobsResponse](../../models/operations/listjobsresponse.md)**


## refresh_connection

Refresh metadata for a workspace connection.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.RefreshConnectionRequest(
    org_id='temporibus',
    workspace_id='ab',
)

res = s.databricks.refresh_connection(req, operations.RefreshConnectionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.RefreshConnectionRequest](../../models/shared/refreshconnectionrequest.md)           | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.RefreshConnectionSecurity](../../models/operations/refreshconnectionsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.RefreshConnectionResponse](../../models/operations/refreshconnectionresponse.md)**


## run_job

Run an existing job in a given databricks workspace.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.RunJobRequest(
    job_id=337396,
    org_id='veritatis',
    workspace_id='deserunt',
)

res = s.databricks.run_job(req, operations.RunJobSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.RunJobRequest](../../models/shared/runjobrequest.md)           | :heavy_check_mark:                                                     | The request object to use for the request.                             |
| `security`                                                             | [operations.RunJobSecurity](../../models/operations/runjobsecurity.md) | :heavy_check_mark:                                                     | The security requirements to use for the request.                      |


### Response

**[operations.RunJobResponse](../../models/operations/runjobresponse.md)**


## update_connection

Update the connection metadata for a given org

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.UpdateConnectionRequest(
    changes=shared.UpdateConnectionChanges(
        connected=False,
        demo=False,
        org_id='perferendis',
    ),
    org_id='ipsam',
    workspace_id='repellendus',
)

res = s.databricks.update_connection(req, operations.UpdateConnectionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.UpdateConnectionRequest](../../models/shared/updateconnectionrequest.md)           | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.UpdateConnectionSecurity](../../models/operations/updateconnectionsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.UpdateConnectionResponse](../../models/operations/updateconnectionresponse.md)**

