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
    org_id='provident',
    workspace_id='distinctio',
)

res = s.databricks.get_connection(req, operations.GetConnectionSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## list_jobs

List all of the jobs in a workspace.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.ListJobsRequest(
    org_id='quibusdam',
    workspace_id='unde',
)

res = s.databricks.list_jobs(req, operations.ListJobsSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## refresh_connection

Refresh metadata for a workspace connection.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.RefreshConnectionRequest(
    org_id='nulla',
    workspace_id='corrupti',
)

res = s.databricks.refresh_connection(req, operations.RefreshConnectionSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## run_job

Run an existing job in a given databricks workspace.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.RunJobRequest(
    job_id=847252,
    org_id='vel',
    workspace_id='error',
)

res = s.databricks.run_job(req, operations.RunJobSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

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
        org_id='deserunt',
    ),
    org_id='suscipit',
    workspace_id='iure',
)

res = s.databricks.update_connection(req, operations.UpdateConnectionSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```
