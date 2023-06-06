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
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```

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
    api_key_auth="YOUR_API_KEY_HERE",
))

if res.status_code == 200:
    # handle response
```
