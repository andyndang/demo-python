# dataset_metadata

### Available Operations

* [delete_dataset_metadata](#delete_dataset_metadata) - Delete dataset metadata for the specified dataset
* [get_dataset_metadata](#get_dataset_metadata) - Get dataset metadata for the specified dataset
* [put_dataset_metadata](#put_dataset_metadata) - Put dataset metadata for the specified dataset

## delete_dataset_metadata

Delete dataset metadata for the specified dataset

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.DeleteDatasetMetadataRequest(
    dataset_id='model-123',
    org_id='org-123',
)

res = s.dataset_metadata.delete_dataset_metadata(req, operations.DeleteDatasetMetadataSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## get_dataset_metadata

Get dataset metadata for the specified dataset

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetDatasetMetadataRequest(
    dataset_id='model-123',
    org_id='org-123',
)

res = s.dataset_metadata.get_dataset_metadata(req, operations.GetDatasetMetadataSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## put_dataset_metadata

Put dataset metadata for the specified dataset

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.PutDatasetMetadataRequest(
    request_body='magnam',
    dataset_id='model-123',
    org_id='org-123',
)

res = s.dataset_metadata.put_dataset_metadata(req, operations.PutDatasetMetadataSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```
