# feature_weights

### Available Operations

* [get_column_weights](#get_column_weights) - Get column weights for the specified dataset
* [put_column_weights](#put_column_weights) - Put column weights for the specified dataset

## get_column_weights

Get column weights for the specified dataset

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetColumnWeightsRequest(
    dataset_id='model-123',
    org_id='org-123',
)

res = s.feature_weights.get_column_weights(req, operations.GetColumnWeightsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetColumnWeightsRequest](../../models/operations/getcolumnweightsrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.GetColumnWeightsSecurity](../../models/operations/getcolumnweightssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.GetColumnWeightsResponse](../../models/operations/getcolumnweightsresponse.md)**


## put_column_weights

Put column weights for the specified dataset

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.PutColumnWeightsRequest(
    request_body='fuga',
    dataset_id='model-123',
    org_id='org-123',
)

res = s.feature_weights.put_column_weights(req, operations.PutColumnWeightsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PutColumnWeightsRequest](../../models/operations/putcolumnweightsrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.PutColumnWeightsSecurity](../../models/operations/putcolumnweightssecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.PutColumnWeightsResponse](../../models/operations/putcolumnweightsresponse.md)**

