# log

### Available Operations

* [get_profile_observatory_link](#get_profile_observatory_link) - Get observatory links for profiles in a given org/model. A max of 3 profiles can be viewed a a time.
* [log_async](#log_async) - Like /log, except this api doesn't take the actual profile content. It returns an upload link that can be used to upload the profile to.
* [log_reference](#log_reference) - Returns a presigned URL for uploading the reference profile to.

## get_profile_observatory_link

Get observatory links for profiles in a given org/model. A max of 3 profiles can be viewed a a time.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.GetProfileObservatoryLinkRequest(
    get_profile_observatory_link_request=shared.GetProfileObservatoryLinkRequest(
        batch_profile_timestamps=[
            367562,
        ],
        reference_profile_ids=[
            'iure',
        ],
    ),
    dataset_id='doloribus',
    org_id='debitis',
)

res = s.log.get_profile_observatory_link(req, operations.GetProfileObservatoryLinkSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetProfileObservatoryLinkRequest](../../models/operations/getprofileobservatorylinkrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.GetProfileObservatoryLinkSecurity](../../models/operations/getprofileobservatorylinksecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.GetProfileObservatoryLinkResponse](../../models/operations/getprofileobservatorylinkresponse.md)**


## log_async

Like /log, except this api doesn't take the actual profile content. It returns an upload link that can be used to upload the profile to.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.LogAsyncRequest(
    log_async_request=shared.LogAsyncRequest(
        dataset_timestamp=260341,
        segment_tags=[
            shared.SegmentTag(
                key='deleniti',
                value='facilis',
            ),
            shared.SegmentTag(
                key='in',
                value='architecto',
            ),
            shared.SegmentTag(
                key='architecto',
                value='repudiandae',
            ),
            shared.SegmentTag(
                key='ullam',
                value='expedita',
            ),
        ],
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.log.log_async(req, operations.LogAsyncSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.LogAsyncRequest](../../models/operations/logasyncrequest.md)   | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [operations.LogAsyncSecurity](../../models/operations/logasyncsecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |


### Response

**[operations.LogAsyncResponse](../../models/operations/logasyncresponse.md)**


## log_reference

Reference profiles can be used for.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.LogReferenceRequest(
    log_reference_request=shared.LogReferenceRequest(
        alias='nihil',
        dataset_timestamp=998848,
    ),
    model_id='model-123',
    org_id='org-123',
)

res = s.log.log_reference(req, operations.LogReferenceSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.LogReferenceRequest](../../models/operations/logreferencerequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.LogReferenceSecurity](../../models/operations/logreferencesecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.LogReferenceResponse](../../models/operations/logreferenceresponse.md)**

