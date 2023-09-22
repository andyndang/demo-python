# Provision

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
    customer_id_token='quis',
    email='Jenifer.Becker@yahoo.com',
    expect_existing=False,
    model_name='eos',
    org_name='perferendis',
)

res = s.provision.provision_aws_marketplace_new_user(req)

if res.status_code == 200:
    # handle response
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
    email='Peggie87@gmail.com',
    expect_existing_user=False,
    id='5fe9b90c-2890-49b3-be49-a8d9cbf48633',
)

res = s.provision.provision_databricks_connection(req)

if res.status_code == 200:
    # handle response
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
    email='Christy_Erdman73@gmail.com',
    expect_existing=False,
    model_name='voluptate',
    org_name='dignissimos',
    subscription_tier=shared.SubscriptionTier.SUBSCRIPTION,
)

res = s.provision.provision_new_user(req)

if res.status_code == 200:
    # handle response
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
    access_token='amet',
    cloud_provider='dolorum',
    connection_established=False,
    connection_id='numquam',
    demo=False,
    email='Anderson.Bednar@gmail.com',
    free_trial=False,
    hostname='frightening-synergy.net',
    port=976405,
    workspace_id='voluptas',
    workspace_url='natus',
)

res = s.provision.register_databricks_connection(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [shared.RegisterDatabricksConnectionRequest](../../models/shared/registerdatabricksconnectionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.RegisterDatabricksConnectionResponse](../../models/operations/registerdatabricksconnectionresponse.md)**

