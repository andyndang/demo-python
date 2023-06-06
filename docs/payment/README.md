# payment

### Available Operations

* [stripe_payment_endpoint](#stripe_payment_endpoint) - Endpoint for Stripe payment webhooks

## stripe_payment_endpoint

Endpoint for Stripe payment webhooks

### Example Usage

```python
import songbird


s = songbird.Songbird()

req = 'pariatur'

res = s.payment.stripe_payment_endpoint(req)

if res.status_code == 200:
    # handle response
```
