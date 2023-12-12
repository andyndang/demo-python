# Log
(*log*)

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

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetProfileObservatoryLinkRequest(
    get_profile_observatory_link_request=shared.GetProfileObservatoryLinkRequest(
        batch_profile_timestamps=[
            926863,
        ],
        reference_profile_ids=[
            'string',
        ],
    ),
    dataset_id='string',
    org_id='string',
)

res = s.log.get_profile_observatory_link(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetProfileObservatoryLinkRequest](../../models/operations/getprofileobservatorylinkrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetProfileObservatoryLinkResponse](../../models/operations/getprofileobservatorylinkresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## log_async

Like /log, except this api doesn't take the actual profile content. It returns an upload link that can be used to upload the profile to.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.LogAsyncRequest(
    log_async_request=shared.LogAsyncRequest(
        segment_tags=[
            shared.SegmentTag(
                key='<key>',
                value='string',
            ),
        ],
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.log.log_async(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.LogAsyncRequest](../../models/operations/logasyncrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.LogAsyncResponse](../../models/operations/logasyncresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## log_reference

Reference profiles can be used for.

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.LogReferenceRequest(
    log_reference_request=shared.LogReferenceRequest(),
    model_id='model-123',
    org_id='org-123',
)

res = s.log.log_reference(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.LogReferenceRequest](../../models/operations/logreferencerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.LogReferenceResponse](../../models/operations/logreferenceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
