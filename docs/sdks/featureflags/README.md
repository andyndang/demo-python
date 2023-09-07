# feature_flags

### Available Operations

* [get_feature_flags](#get_feature_flags) - Get feature flags for the specified user/org

## get_feature_flags

Get feature flags for the specified user/org

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetFeatureFlagsRequest(
    org_id='occaecati',
    user_id='fugit',
)

res = s.feature_flags.get_feature_flags(req, operations.GetFeatureFlagsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetFeatureFlagsRequest](../../models/operations/getfeatureflagsrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.GetFeatureFlagsSecurity](../../models/operations/getfeatureflagssecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.GetFeatureFlagsResponse](../../models/operations/getfeatureflagsresponse.md)**

