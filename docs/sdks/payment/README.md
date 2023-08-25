# payment

### Available Operations

* [stripe_payment_endpoint](#stripe_payment_endpoint) - Endpoint for Stripe payment webhooks

## stripe_payment_endpoint

Endpoint for Stripe payment webhooks

### Example Usage

```python
import songbird


s = songbird.Songbird()

req = 'fugiat'

res = s.payment.stripe_payment_endpoint(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [str](../../models//.md)                   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.StripePaymentEndpointResponse](../../models/operations/stripepaymentendpointresponse.md)**

