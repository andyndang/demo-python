# Payment
(*payment*)

### Available Operations

* [stripe_payment_endpoint](#stripe_payment_endpoint) - Endpoint for Stripe payment webhooks

## stripe_payment_endpoint

Endpoint for Stripe payment webhooks

### Example Usage

```python
import songbird

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = 'string'

res = s.payment.stripe_payment_endpoint(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [str](../../models/.md)                    | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.StripePaymentEndpointResponse](../../models/operations/stripepaymentendpointresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
