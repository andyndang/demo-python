# dataset_profile

### Available Operations

* [create_reference_profile](#create_reference_profile) - Returns data needed to uploading the reference profile
* [delete_analyzer_results](#delete_analyzer_results) - Deletes a set of analyzer results
* [delete_dataset_profiles](#delete_dataset_profiles) - Deletes a set of dataset profiles
* [delete_reference_profile](#delete_reference_profile) - Delete a single reference profile
* [get_profile_traces](#get_profile_traces) - Returns a list for profile traces matching a trace id
* [get_reference_profile](#get_reference_profile) - Returns a single reference profile
* [hide_segments](#hide_segments) - Hides a list of segments
* [list_profile_traces](#list_profile_traces) - Returns a list for profile traces
* [list_reference_profiles](#list_reference_profiles) - Returns a list for reference profiles
* [list_segments](#list_segments) - Returns a list of segments

## create_reference_profile

Returns data needed to upload the reference profile. Supports uploading segmented reference profiles. 
            If segments are omitted, provides data needed to upload a single reference profile. 
            This replaces the deprecated LogReference operation.
        

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.CreateReferenceProfileRequest(
    create_reference_profile_request=shared.CreateReferenceProfileRequest(
        alias='quo',
        dataset_timestamp=140350,
        segments=[
            shared.Segment(
                tags=[
                    shared.SegmentTag(
                        key='at',
                        value='at',
                    ),
                ],
            ),
        ],
        tags=[
            'maiores',
        ],
        version='molestiae',
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.dataset_profile.create_reference_profile(req, operations.CreateReferenceProfileSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateReferenceProfileRequest](../../models/operations/createreferenceprofilerequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.CreateReferenceProfileSecurity](../../models/operations/createreferenceprofilesecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.CreateReferenceProfileResponse](../../models/operations/createreferenceprofileresponse.md)**


## delete_analyzer_results

Deletes a set of analyzer results. Returns false if scheduling deletion encountered some error.

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.DeleteAnalyzerResultsRequest(
    dataset_id='model-123',
    end_timestamp=1893456000000,
    org_id='org-123',
    start_timestamp=1577836800000,
)

res = s.dataset_profile.delete_analyzer_results(req, operations.DeleteAnalyzerResultsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.DeleteAnalyzerResultsRequest](../../models/operations/deleteanalyzerresultsrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.DeleteAnalyzerResultsSecurity](../../models/operations/deleteanalyzerresultssecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.DeleteAnalyzerResultsResponse](../../models/operations/deleteanalyzerresultsresponse.md)**


## delete_dataset_profiles

Deletes a set of dataset profiles. Returns false if scheduling deletion encountered some error.

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.DeleteDatasetProfilesRequest(
    before_upload_timestamp=1577836800000,
    dataset_id='model-123',
    org_id='org-123',
    profile_end_timestamp=1893456000000,
    profile_start_timestamp=1577836800000,
)

res = s.dataset_profile.delete_dataset_profiles(req, operations.DeleteDatasetProfilesSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.DeleteDatasetProfilesRequest](../../models/operations/deletedatasetprofilesrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.DeleteDatasetProfilesSecurity](../../models/operations/deletedatasetprofilessecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.DeleteDatasetProfilesResponse](../../models/operations/deletedatasetprofilesresponse.md)**


## delete_reference_profile

Delete a a Reference Profile. Returns false if the deletion encountered some error.

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.DeleteReferenceProfileRequest(
    model_id='model-123',
    org_id='org-123',
    reference_id='ref-xxy',
)

res = s.dataset_profile.delete_reference_profile(req, operations.DeleteReferenceProfileSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.DeleteReferenceProfileRequest](../../models/operations/deletereferenceprofilerequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.DeleteReferenceProfileSecurity](../../models/operations/deletereferenceprofilesecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.DeleteReferenceProfileResponse](../../models/operations/deletereferenceprofileresponse.md)**


## get_profile_traces

Returns a list of profile traces matching a trace id

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetProfileTracesRequest(
    dataset_id='model-123',
    limit=50,
    offset=0,
    org_id='org-123',
    trace_id='a756f8bb-de30-48a2-be41-178ae6af7100',
)

res = s.dataset_profile.get_profile_traces(req, operations.GetProfileTracesSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetProfileTracesRequest](../../models/operations/getprofiletracesrequest.md)   | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.GetProfileTracesSecurity](../../models/operations/getprofiletracessecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.GetProfileTracesResponse](../../models/operations/getprofiletracesresponse.md)**


## get_reference_profile

Returns a Reference Profile.

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetReferenceProfileRequest(
    model_id='model-123',
    org_id='org-123',
    reference_id='ref-xxy',
)

res = s.dataset_profile.get_reference_profile(req, operations.GetReferenceProfileSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetReferenceProfileRequest](../../models/operations/getreferenceprofilerequest.md)   | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `security`                                                                                       | [operations.GetReferenceProfileSecurity](../../models/operations/getreferenceprofilesecurity.md) | :heavy_check_mark:                                                                               | The security requirements to use for the request.                                                |


### Response

**[operations.GetReferenceProfileResponse](../../models/operations/getreferenceprofileresponse.md)**


## hide_segments

Returns a list of segments that were hidden for a dataset.

        

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.HideSegmentsRequest(
    segments_list_request=shared.SegmentsListRequest(
        segments=[
            'quod',
        ],
    ),
    dataset_id='model-123',
    org_id='org-123',
)

res = s.dataset_profile.hide_segments(req, operations.HideSegmentsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.HideSegmentsRequest](../../models/operations/hidesegmentsrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.HideSegmentsSecurity](../../models/operations/hidesegmentssecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.HideSegmentsResponse](../../models/operations/hidesegmentsresponse.md)**


## list_profile_traces

Returns a list of profile traces.

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.ListProfileTracesRequest(
    dataset_id='model-123',
    from_epoch=1577836800000,
    limit=50,
    offset=0,
    org_id='org-123',
    to_epoch=1893456000000,
)

res = s.dataset_profile.list_profile_traces(req, operations.ListProfileTracesSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.ListProfileTracesRequest](../../models/operations/listprofiletracesrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.ListProfileTracesSecurity](../../models/operations/listprofiletracessecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.ListProfileTracesResponse](../../models/operations/listprofiletracesresponse.md)**


## list_reference_profiles

Returns a list of Reference Profiles.

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.ListReferenceProfilesRequest(
    from_epoch=1577836800000,
    model_id='model-123',
    org_id='org-123',
    to_epoch=1893456000000,
)

res = s.dataset_profile.list_reference_profiles(req, operations.ListReferenceProfilesSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.ListReferenceProfilesRequest](../../models/operations/listreferenceprofilesrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.ListReferenceProfilesSecurity](../../models/operations/listreferenceprofilessecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.ListReferenceProfilesResponse](../../models/operations/listreferenceprofilesresponse.md)**


## list_segments

Returns a list of segments for the dataset.

        

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.ListSegmentsRequest(
    model_id='model-123',
    org_id='org-123',
)

res = s.dataset_profile.list_segments(req, operations.ListSegmentsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListSegmentsRequest](../../models/operations/listsegmentsrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.ListSegmentsSecurity](../../models/operations/listsegmentssecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.ListSegmentsResponse](../../models/operations/listsegmentsresponse.md)**

