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
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.ProvisionNewMarketplaceUserRequest(
    customer_id_token='Infrastructure',
    email='Emery.Rempel@gmail.com',
    model_name='Maserati',
    org_name='woman',
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


## provision_databricks_connection

Create resources for a new user coming from Databricks

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
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


## provision_new_user

Create the resources that a new user needs to use WhyLabs via the website.

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.ProvisionNewUserRequest(
    email='Alec40@hotmail.com',
    model_name='Ergonomic',
    org_name='Northwest',
    subscription_tier=shared.SubscriptionTier.PAID,
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


## register_databricks_connection

Register databricks metadata, temporarily storing it against a UUID so that it can be used to provision a databricks connection after email authentication

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = shared.RegisterDatabricksConnectionRequest(
    access_token='logistical',
    cloud_provider='Operations',
    connection_id='Carolina',
    demo=False,
    email='Christophe81@yahoo.com',
    hostname='far-flung-mushroom.org',
    port=610134,
    workspace_id='Account',
    workspace_url='Oganesson',
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

