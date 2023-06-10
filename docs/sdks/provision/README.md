# provision

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
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.ProvisionNewMarketplaceUserRequest(
    customer_id_token='nemo',
    email='Agnes1@hotmail.com',
    expect_existing=False,
    model_name='cumque',
    org_name='corporis',
)

res = s.provision.provision_aws_marketplace_new_user(req, operations.ProvisionAWSMarketplaceNewUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [shared.ProvisionNewMarketplaceUserRequest](../../models/shared/provisionnewmarketplaceuserrequest.md)                 | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `security`                                                                                                             | [operations.ProvisionAWSMarketplaceNewUserSecurity](../../models/operations/provisionawsmarketplacenewusersecurity.md) | :heavy_check_mark:                                                                                                     | The security requirements to use for the request.                                                                      |


### Response

**[operations.ProvisionAWSMarketplaceNewUserResponse](../../models/operations/provisionawsmarketplacenewuserresponse.md)**


## provision_databricks_connection

Create resources for a new user coming from Databricks

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.ProvisionDatabricksConnectionRequest(
    email='Morgan33@hotmail.com',
    expect_existing_user=False,
    id='87053202-c73d-45fe-9b90-c28909b3fe49',
)

res = s.provision.provision_databricks_connection(req, operations.ProvisionDatabricksConnectionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [shared.ProvisionDatabricksConnectionRequest](../../models/shared/provisiondatabricksconnectionrequest.md)           | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |
| `security`                                                                                                           | [operations.ProvisionDatabricksConnectionSecurity](../../models/operations/provisiondatabricksconnectionsecurity.md) | :heavy_check_mark:                                                                                                   | The security requirements to use for the request.                                                                    |


### Response

**[operations.ProvisionDatabricksConnectionResponse](../../models/operations/provisiondatabricksconnectionresponse.md)**


## provision_new_user

Create the resources that a new user needs to use WhyLabs via the website.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.ProvisionNewUserRequest(
    email='Kailee_Stracke@hotmail.com',
    expect_existing=False,
    model_name='libero',
    org_name='delectus',
    subscription_tier=shared.SubscriptionTier.PAID,
)

res = s.provision.provision_new_user(req, operations.ProvisionNewUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.ProvisionNewUserRequest](../../models/shared/provisionnewuserrequest.md)           | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.ProvisionNewUserSecurity](../../models/operations/provisionnewusersecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.ProvisionNewUserResponse](../../models/operations/provisionnewuserresponse.md)**


## register_databricks_connection

Register databricks metadata, temporarily storing it against a UUID so that it can be used to provision a databricks connection after email authentication

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.RegisterDatabricksConnectionRequest(
    access_token='quos',
    cloud_provider='aliquid',
    connection_established=False,
    connection_id='dolorem',
    demo=False,
    email='Dameon94@gmail.com',
    free_trial=False,
    hostname='nimble-reporter.info',
    port=490459,
    workspace_id='reiciendis',
    workspace_url='amet',
)

res = s.provision.register_databricks_connection(req, operations.RegisterDatabricksConnectionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [shared.RegisterDatabricksConnectionRequest](../../models/shared/registerdatabricksconnectionrequest.md)           | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `security`                                                                                                         | [operations.RegisterDatabricksConnectionSecurity](../../models/operations/registerdatabricksconnectionsecurity.md) | :heavy_check_mark:                                                                                                 | The security requirements to use for the request.                                                                  |


### Response

**[operations.RegisterDatabricksConnectionResponse](../../models/operations/registerdatabricksconnectionresponse.md)**

