# Provision
(*provision*)

### Available Operations

* [provision_aws_marketplace_new_user](#provision_aws_marketplace_new_user) - Create resources for a new user coming from AWS Marketplace
* [provision_databricks_connection](#provision_databricks_connection) - Create resources for a new user coming from Databricks
* [provision_new_user](#provision_new_user) - Create the resources that a new user needs to use WhyLabs via the website.
* [register_databricks_connection](#register_databricks_connection) - Register databricks metadata, temporarily storing it against a UUID so that it can be used to provision a databricks connection after email authentication

## provision_aws_marketplace_new_user

Create resources for a new user coming from AWS Marketplace

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="",
)

req = shared.ProvisionNewMarketplaceUserRequest(
    customer_id_token='string',
    email='Karina72@yahoo.com',
    model_name='string',
    org_name='string',
)

res = s.provision.provision_aws_marketplace_new_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [shared.ProvisionNewMarketplaceUserRequest](../../models/shared/provisionnewmarketplaceuserrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.ProvisionAWSMarketplaceNewUserResponse](../../models/operations/provisionawsmarketplacenewuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## provision_databricks_connection

Create resources for a new user coming from Databricks

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="",
)

req = shared.ProvisionDatabricksConnectionRequest(
    email='Alexandria_Ernser@yahoo.com',
    expect_existing_user=False,
    id='<ID>',
)

res = s.provision.provision_databricks_connection(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [shared.ProvisionDatabricksConnectionRequest](../../models/shared/provisiondatabricksconnectionrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.ProvisionDatabricksConnectionResponse](../../models/operations/provisiondatabricksconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## provision_new_user

Create the resources that a new user needs to use WhyLabs via the website.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="",
)

req = shared.ProvisionNewUserRequest(
    email='Alec40@hotmail.com',
    model_name='string',
    org_name='string',
    subscription_tier=shared.SubscriptionTier.FREE,
)

res = s.provision.provision_new_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.ProvisionNewUserRequest](../../models/shared/provisionnewuserrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ProvisionNewUserResponse](../../models/operations/provisionnewuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## register_databricks_connection

Register databricks metadata, temporarily storing it against a UUID so that it can be used to provision a databricks connection after email authentication

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="",
)

req = shared.RegisterDatabricksConnectionRequest(
    access_token='string',
    cloud_provider='string',
    connection_id='string',
    demo=False,
    email='Kim53@yahoo.com',
    hostname='glistening-mobile.com',
    port=797817,
    workspace_id='string',
    workspace_url='string',
)

res = s.provision.register_databricks_connection(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [shared.RegisterDatabricksConnectionRequest](../../models/shared/registerdatabricksconnectionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.RegisterDatabricksConnectionResponse](../../models/operations/registerdatabricksconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
