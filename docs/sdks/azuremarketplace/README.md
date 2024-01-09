# AzureMarketplace
(*azure_marketplace*)

### Available Operations

* [azure_marketplace_webhook](#azure_marketplace_webhook) - Endpoint for Azure Marketplace webhooks

## azure_marketplace_webhook

Endpoint for Azure Marketplace webhooks

### Example Usage

```python
import songbird

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = 'string'

res = s.azure_marketplace.azure_marketplace_webhook(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [str](../../models/.md)                    | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.AzureMarketplaceWebhookResponse](../../models/operations/azuremarketplacewebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
