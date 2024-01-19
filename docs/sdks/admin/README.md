# Admin
(*admin*)

### Available Operations

* [activate_marketplace_subscription_internal](#activate_marketplace_subscription_internal) - Activate Azure Marketplace subscription to an existing organization.
* [generate_report](#generate_report) - Generate an admin report
* [list_azure_marketplace_subscriptions](#list_azure_marketplace_subscriptions) - List Azure Marketplace subscriptions
* [post_monitor_config_validation_job](#post_monitor_config_validation_job) - Create a monitor config validation job for all configs

## activate_marketplace_subscription_internal

Activate Azure Marketplace subscription to an existing organization.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.ActivateMarketplaceSubscriptionInternalRequest(
    org_id='string',
    subscription_id='string',
)

res = s.admin.activate_marketplace_subscription_internal(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.ActivateMarketplaceSubscriptionInternalRequest](../../models/operations/activatemarketplacesubscriptioninternalrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.ActivateMarketplaceSubscriptionInternalResponse](../../models/operations/activatemarketplacesubscriptioninternalresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## generate_report

Generate an admin report

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GenerateReportRequest(
    report_type=shared.AdminReportType.SESSIONS,
)

res = s.admin.generate_report(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GenerateReportRequest](../../models/operations/generatereportrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GenerateReportResponse](../../models/operations/generatereportresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_azure_marketplace_subscriptions

List Azure Marketplace subscriptions

### Example Usage

```python
import songbird

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.list_azure_marketplace_subscriptions()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.ListAzureMarketplaceSubscriptionsResponse](../../models/operations/listazuremarketplacesubscriptionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_monitor_config_validation_job

Create a monitor config validation job for all configs

### Example Usage

```python
import songbird

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.admin.post_monitor_config_validation_job()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.PostMonitorConfigValidationJobResponse](../../models/operations/postmonitorconfigvalidationjobresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
