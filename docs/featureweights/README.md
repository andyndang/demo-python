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
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

## put_column_weights

Put column weights for the specified dataset

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.PutColumnWeightsRequest(
    request_body='nam',
    dataset_id='model-123',
    org_id='org-123',
)

res = s.feature_weights.put_column_weights(req, operations.PutColumnWeightsSecurity(
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```
