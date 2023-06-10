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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.DeleteDatasetMetadataRequest](../../models/operations/deletedatasetmetadatarequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.DeleteDatasetMetadataSecurity](../../models/operations/deletedatasetmetadatasecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.DeleteDatasetMetadataResponse](../../models/operations/deletedatasetmetadataresponse.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetDatasetMetadataRequest](../../models/operations/getdatasetmetadatarequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.GetDatasetMetadataSecurity](../../models/operations/getdatasetmetadatasecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.GetDatasetMetadataResponse](../../models/operations/getdatasetmetadataresponse.md)**


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
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PutDatasetMetadataRequest](../../models/operations/putdatasetmetadatarequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.PutDatasetMetadataSecurity](../../models/operations/putdatasetmetadatasecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.PutDatasetMetadataResponse](../../models/operations/putdatasetmetadataresponse.md)**

