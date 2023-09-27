# FeatureWeights
(*feature_weights*)

### Available Operations

* [get_column_weights](#get_column_weights) - Get column weights for the specified dataset
* [put_column_weights](#put_column_weights) - Put column weights for the specified dataset

## get_column_weights

Get column weights for the specified dataset

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.GetColumnWeightsRequest(
    dataset_id='model-123',
    org_id='org-123',
)

res = s.feature_weights.get_column_weights(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetColumnWeightsRequest](../../models/operations/getcolumnweightsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetColumnWeightsResponse](../../models/operations/getcolumnweightsresponse.md)**


## put_column_weights

Put column weights for the specified dataset

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.PutColumnWeightsRequest(
    request_body='beatae',
    dataset_id='model-123',
    org_id='org-123',
)

res = s.feature_weights.put_column_weights(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PutColumnWeightsRequest](../../models/operations/putcolumnweightsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PutColumnWeightsResponse](../../models/operations/putcolumnweightsresponse.md)**

