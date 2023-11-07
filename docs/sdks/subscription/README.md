# Subscription
(*.subscription*)

### Available Operations

* [get_organization_subscriptions](#get_organization_subscriptions) - Get organization subscription details

## get_organization_subscriptions

Get organization subscription details

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="",
)

req = operations.GetOrganizationSubscriptionsRequest(
    org_id='string',
)

res = s.subscription.get_organization_subscriptions(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetOrganizationSubscriptionsRequest](../../models/operations/getorganizationsubscriptionsrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetOrganizationSubscriptionsResponse](../../models/operations/getorganizationsubscriptionsresponse.md)**

