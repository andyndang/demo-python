# FeatureFlags
(*.feature_flags*)

### Available Operations

* [get_feature_flags](#get_feature_flags) - Get feature flags for the specified user/org

## get_feature_flags

Get feature flags for the specified user/org

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="",
)

req = operations.GetFeatureFlagsRequest(
    org_id='string',
    user_id='string',
)

res = s.feature_flags.get_feature_flags(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetFeatureFlagsRequest](../../models/operations/getfeatureflagsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetFeatureFlagsResponse](../../models/operations/getfeatureflagsresponse.md)**

