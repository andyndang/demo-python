# DatasetProfile
(*dataset_profile*)

### Available Operations

* [create_reference_profile](#create_reference_profile) - Returns data needed to uploading the reference profile
* [delete_analyzer_results](#delete_analyzer_results) - Deletes a set of analyzer results
* [delete_dataset_profiles](#delete_dataset_profiles) - Deletes a set of dataset profiles
* [delete_reference_profile](#delete_reference_profile) - Delete a single reference profile
* [get_profile_traces](#get_profile_traces) - Returns a list for profile traces matching a trace id
* [get_reference_profile](#get_reference_profile) - Returns a single reference profile
* [hide_segments](#hide_segments) - Hides a list of segments
* [list_delete_analyzer_results_requests](#list_delete_analyzer_results_requests) - List requests to delete analyzer results
* [list_delete_dataset_profiles_requests](#list_delete_dataset_profiles_requests) - List requests to delete dataset profiles
* [list_reference_profiles](#list_reference_profiles) - Returns a list for reference profiles between the given time range filtered on the upload timestamp
* [list_segments](#list_segments) - Returns a list of segments

## create_reference_profile

Returns data needed to upload the reference profile. Supports uploading segmented reference profiles. 
            If segments are omitted, provides data needed to upload a single reference profile. 
            This replaces the deprecated LogReference operation.
        

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.CreateReferenceProfileRequest(
    create_reference_profile_request=shared.CreateReferenceProfileRequest(
        segments=[
            shared.Segment(
                tags=[
                    shared.SegmentTag(
                        key='<key>',
                        value='string',
                    ),
                ],
            ),
        ],
        tags=[
            'string',
        ],
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.dataset_profile.create_reference_profile(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.CreateReferenceProfileRequest](../../models/operations/createreferenceprofilerequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.CreateReferenceProfileResponse](../../models/operations/createreferenceprofileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_analyzer_results

Deletes a set of analyzer results. Returns false if scheduling deletion encountered some error.

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.DeleteAnalyzerResultsRequest(
    dataset_id='model-123',
    end_timestamp=1893456000000,
    org_id='org-123',
    start_timestamp=1577836800000,
)

res = s.dataset_profile.delete_analyzer_results(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.DeleteAnalyzerResultsRequest](../../models/operations/deleteanalyzerresultsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.DeleteAnalyzerResultsResponse](../../models/operations/deleteanalyzerresultsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_dataset_profiles

Deletes a set of dataset profiles. Returns false if scheduling deletion encountered some error.

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.DeleteDatasetProfilesRequest(
    before_upload_timestamp=1577836800000,
    dataset_id='model-123',
    org_id='org-123',
    profile_end_timestamp=1893456000000,
    profile_start_timestamp=1577836800000,
)

res = s.dataset_profile.delete_dataset_profiles(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.DeleteDatasetProfilesRequest](../../models/operations/deletedatasetprofilesrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.DeleteDatasetProfilesResponse](../../models/operations/deletedatasetprofilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_reference_profile

Delete a a Reference Profile. Returns false if the deletion encountered some error.

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.DeleteReferenceProfileRequest(
    model_id='model-123',
    org_id='org-123',
    reference_id='ref-xxy',
)

res = s.dataset_profile.delete_reference_profile(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.DeleteReferenceProfileRequest](../../models/operations/deletereferenceprofilerequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.DeleteReferenceProfileResponse](../../models/operations/deletereferenceprofileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_profile_traces

Returns a list of profile traces matching a trace id

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetProfileTracesRequest(
    dataset_id='model-123',
    limit=50,
    offset=0,
    org_id='org-123',
    trace_id='a756f8bb-de30-48a2-be41-178ae6af7100',
)

res = s.dataset_profile.get_profile_traces(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetProfileTracesRequest](../../models/operations/getprofiletracesrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetProfileTracesResponse](../../models/operations/getprofiletracesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_reference_profile

Returns a Reference Profile.

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.GetReferenceProfileRequest(
    model_id='model-123',
    org_id='org-123',
    reference_id='ref-xxy',
)

res = s.dataset_profile.get_reference_profile(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetReferenceProfileRequest](../../models/operations/getreferenceprofilerequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetReferenceProfileResponse](../../models/operations/getreferenceprofileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## hide_segments

Returns a list of segments that were hidden for a dataset.

        

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.HideSegmentsRequest(
    segments_list_request=shared.SegmentsListRequest(
        segments=[
            'string',
        ],
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.dataset_profile.hide_segments(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.HideSegmentsRequest](../../models/operations/hidesegmentsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.HideSegmentsResponse](../../models/operations/hidesegmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_delete_analyzer_results_requests

List the requests to delete analyzer results.

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.ListDeleteAnalyzerResultsRequestsRequest(
    org_id='org-123',
)

res = s.dataset_profile.list_delete_analyzer_results_requests(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.ListDeleteAnalyzerResultsRequestsRequest](../../models/operations/listdeleteanalyzerresultsrequestsrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.ListDeleteAnalyzerResultsRequestsResponse](../../models/operations/listdeleteanalyzerresultsrequestsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_delete_dataset_profiles_requests

List the requests to delete dataset profiles.

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.ListDeleteDatasetProfilesRequestsRequest(
    org_id='org-123',
)

res = s.dataset_profile.list_delete_dataset_profiles_requests(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.ListDeleteDatasetProfilesRequestsRequest](../../models/operations/listdeletedatasetprofilesrequestsrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.ListDeleteDatasetProfilesRequestsResponse](../../models/operations/listdeletedatasetprofilesrequestsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_reference_profiles

Returns a list of Reference Profiles between a given time range filtered on the upload timestamp.

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.ListReferenceProfilesRequest(
    from_epoch=1577836800000,
    model_id='model-123',
    org_id='org-123',
    to_epoch=1893456000000,
)

res = s.dataset_profile.list_reference_profiles(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListReferenceProfilesRequest](../../models/operations/listreferenceprofilesrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.ListReferenceProfilesResponse](../../models/operations/listreferenceprofilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_segments

Returns a list of segments for the dataset.

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.ListSegmentsRequest(
    model_id='model-123',
    org_id='org-123',
)

res = s.dataset_profile.list_segments(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListSegmentsRequest](../../models/operations/listsegmentsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListSegmentsResponse](../../models/operations/listsegmentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
