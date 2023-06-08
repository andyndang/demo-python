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
    org_id='officia',
    user_id='occaecati',
)

res = s.feature_flags.get_feature_flags(req, operations.GetFeatureFlagsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```
