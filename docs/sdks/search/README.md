# search

### Available Operations

* [why_labs_search](#why_labs_search) - WhyLabs Search
* [why_labs_search_indexing](#why_labs_search_indexing) - WhyLabs Search Indexing

## why_labs_search

WhyLabs Search

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.WhyLabsSearchRequest(
    query='dolorum',
)

res = s.search.why_labs_search(req, operations.WhyLabsSearchSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.WhyLabsSearchRequest](../../models/operations/whylabssearchrequest.md)   | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.WhyLabsSearchSecurity](../../models/operations/whylabssearchsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.WhyLabsSearchResponse](../../models/operations/whylabssearchresponse.md)**


## why_labs_search_indexing

WhyLabs Search Indexing

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = shared.SearchIndexRequest(
    org_id='numquam',
    type=shared.SearchIndexType.MODELS,
)

res = s.search.why_labs_search_indexing(req, operations.WhyLabsSearchIndexingSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [shared.SearchIndexRequest](../../models/shared/searchindexrequest.md)                               | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.WhyLabsSearchIndexingSecurity](../../models/operations/whylabssearchindexingsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.WhyLabsSearchIndexingResponse](../../models/operations/whylabssearchindexingresponse.md)**

