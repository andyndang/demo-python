# models

### Available Operations

* [create_model](#create_model) - Create a model with a given name and a time period
* [deactivate_model](#deactivate_model) - Mark a model as inactive
* [delete_entity_schema](#delete_entity_schema) - Delete the entity schema config for a given dataset.
* [delete_entity_schema_column](#delete_entity_schema_column) - Delete the entity schema of a single column for a given dataset.
* [delete_entity_schema_metric](#delete_entity_schema_metric) - Delete the schema of a single metric for a given dataset.
* [get_entity_schema](#get_entity_schema) - Get the entity schema config for a given dataset.
* [get_entity_schema_column](#get_entity_schema_column) - Get the entity schema of a single column for a given dataset.
* [get_model](#get_model) - Get a model metadata
* [list_models](#list_models) - Get a list of all of the model ids for an organization.
* [put_entity_schema](#put_entity_schema) - Save the entity schema config for a given dataset.
* [put_entity_schema_column](#put_entity_schema_column) - Save the entity schema of a single column for a given dataset.
* [put_entity_schema_metric](#put_entity_schema_metric) - Save the schema of a single metric for a given dataset.
* [update_model](#update_model) - Update a model's metadata

## create_model

Create a model

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.CreateModelRequest(
    model_id='model-123',
    model_name='Credit-Score-1',
    model_type=shared.ModelType.CLASSIFICATION,
    org_id='org-123',
    time_period=shared.TimePeriod.P1_D,
)

res = s.models.create_model(req, operations.CreateModelSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.CreateModelRequest](../../models/operations/createmodelrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.CreateModelSecurity](../../models/operations/createmodelsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.CreateModelResponse](../../models/operations/createmodelresponse.md)**


## deactivate_model

Mark a model as inactive

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.DeactivateModelRequest(
    model_id='model-123',
    org_id='org-123',
)

res = s.models.deactivate_model(req, operations.DeactivateModelSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.DeactivateModelRequest](../../models/operations/deactivatemodelrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.DeactivateModelSecurity](../../models/operations/deactivatemodelsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.DeactivateModelResponse](../../models/operations/deactivatemodelresponse.md)**


## delete_entity_schema

Delete the entity schema config for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.DeleteEntitySchemaRequest(
    dataset_id='model-123',
    org_id='org-123',
)

res = s.models.delete_entity_schema(req, operations.DeleteEntitySchemaSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.DeleteEntitySchemaRequest](../../models/operations/deleteentityschemarequest.md)   | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [operations.DeleteEntitySchemaSecurity](../../models/operations/deleteentityschemasecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |


### Response

**[operations.DeleteEntitySchemaResponse](../../models/operations/deleteentityschemaresponse.md)**


## delete_entity_schema_column

Delete the entity schema of a single column for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.DeleteEntitySchemaColumnRequest(
    column_id='feature-123',
    dataset_id='model-123',
    org_id='org-123',
)

res = s.models.delete_entity_schema_column(req, operations.DeleteEntitySchemaColumnSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.DeleteEntitySchemaColumnRequest](../../models/operations/deleteentityschemacolumnrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.DeleteEntitySchemaColumnSecurity](../../models/operations/deleteentityschemacolumnsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.DeleteEntitySchemaColumnResponse](../../models/operations/deleteentityschemacolumnresponse.md)**


## delete_entity_schema_metric

Delete the schema of a single metric for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.DeleteEntitySchemaMetricRequest(
    dataset_id='model-123',
    metric_label='feature-123',
    org_id='org-123',
)

res = s.models.delete_entity_schema_metric(req, operations.DeleteEntitySchemaMetricSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.DeleteEntitySchemaMetricRequest](../../models/operations/deleteentityschemametricrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.DeleteEntitySchemaMetricSecurity](../../models/operations/deleteentityschemametricsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.DeleteEntitySchemaMetricResponse](../../models/operations/deleteentityschemametricresponse.md)**


## get_entity_schema

Get the entity schema config for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetEntitySchemaRequest(
    dataset_id='model-123',
    org_id='org-123',
)

res = s.models.get_entity_schema(req, operations.GetEntitySchemaSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetEntitySchemaRequest](../../models/operations/getentityschemarequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.GetEntitySchemaSecurity](../../models/operations/getentityschemasecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.GetEntitySchemaResponse](../../models/operations/getentityschemaresponse.md)**


## get_entity_schema_column

Get the entity schema of a single column for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetEntitySchemaColumnRequest(
    column_id='feature-123',
    dataset_id='model-123',
    org_id='org-123',
)

res = s.models.get_entity_schema_column(req, operations.GetEntitySchemaColumnSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetEntitySchemaColumnRequest](../../models/operations/getentityschemacolumnrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.GetEntitySchemaColumnSecurity](../../models/operations/getentityschemacolumnsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.GetEntitySchemaColumnResponse](../../models/operations/getentityschemacolumnresponse.md)**


## get_model

Returns various metadata about a model

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetModelRequest(
    model_id='model-123',
    org_id='org-123',
)

res = s.models.get_model(req, operations.GetModelSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetModelRequest](../../models/operations/getmodelrequest.md)   | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [operations.GetModelSecurity](../../models/operations/getmodelsecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |


### Response

**[operations.GetModelResponse](../../models/operations/getmodelresponse.md)**


## list_models

Get a list of all of the model ids for an organization.

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.ListModelsRequest(
    org_id='org-123',
)

res = s.models.list_models(req, operations.ListModelsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListModelsRequest](../../models/operations/listmodelsrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.ListModelsSecurity](../../models/operations/listmodelssecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.ListModelsResponse](../../models/operations/listmodelsresponse.md)**


## put_entity_schema

Save the entity schema config for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.PutEntitySchemaRequest(
    entity_schema=shared.EntitySchema(
        columns={
            "voluptas": shared.ColumnSchema(
                classifier='input',
                data_type='fractional',
                discreteness='discrete',
            ),
            "natus": shared.ColumnSchema(
                classifier='input',
                data_type='fractional',
                discreteness='discrete',
            ),
            "eos": shared.ColumnSchema(
                classifier='input',
                data_type='fractional',
                discreteness='discrete',
            ),
            "atque": shared.ColumnSchema(
                classifier='input',
                data_type='fractional',
                discreteness='discrete',
            ),
        },
        metadata=shared.SchemaMetadata(
            author='sit',
            updated_timestamp=854614,
            version=67249,
        ),
        metrics={
            "dolorum": shared.MetricSchema(
                column='estimated_prediction',
                default_metric='median',
                label='estimated_prediction.median',
            ),
            "iusto": shared.MetricSchema(
                column='estimated_prediction',
                default_metric='median',
                label='estimated_prediction.median',
            ),
            "voluptate": shared.MetricSchema(
                column='estimated_prediction',
                default_metric='median',
                label='estimated_prediction.median',
            ),
        },
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.models.put_entity_schema(req, operations.PutEntitySchemaSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PutEntitySchemaRequest](../../models/operations/putentityschemarequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.PutEntitySchemaSecurity](../../models/operations/putentityschemasecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.PutEntitySchemaResponse](../../models/operations/putentityschemaresponse.md)**


## put_entity_schema_column

Save the entity schema of a single column for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.PutEntitySchemaColumnRequest(
    column_schema=shared.ColumnSchema(
        classifier='input',
        data_type='fractional',
        discreteness='discrete',
    ),
    column_id='feature-123',
    dataset_id='model-123',
    org_id='org-123',
)

res = s.models.put_entity_schema_column(req, operations.PutEntitySchemaColumnSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PutEntitySchemaColumnRequest](../../models/operations/putentityschemacolumnrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.PutEntitySchemaColumnSecurity](../../models/operations/putentityschemacolumnsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.PutEntitySchemaColumnResponse](../../models/operations/putentityschemacolumnresponse.md)**


## put_entity_schema_metric

Save the schema of a single metric for a given dataset.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.PutEntitySchemaMetricRequest(
    metric_schema=shared.MetricSchema(
        column='estimated_prediction',
        default_metric='median',
        label='estimated_prediction.median',
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.models.put_entity_schema_metric(req, operations.PutEntitySchemaMetricSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PutEntitySchemaMetricRequest](../../models/operations/putentityschemametricrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.PutEntitySchemaMetricSecurity](../../models/operations/putentityschemametricsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.PutEntitySchemaMetricResponse](../../models/operations/putentityschemametricresponse.md)**


## update_model

Update a model's metadata

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.UpdateModelRequest(
    model_id='model-123',
    model_name='Credit-Score-1',
    model_type=shared.ModelType.CLASSIFICATION,
    org_id='org-123',
    time_period=shared.TimePeriod.P1_D,
)

res = s.models.update_model(req, operations.UpdateModelSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateModelRequest](../../models/operations/updatemodelrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.UpdateModelSecurity](../../models/operations/updatemodelsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.UpdateModelResponse](../../models/operations/updatemodelresponse.md)**

