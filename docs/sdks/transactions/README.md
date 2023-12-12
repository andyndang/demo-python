# Transactions
(*transactions*)

### Available Operations

* [commit_transaction](#commit_transaction) - Commit a log transaction
* [log_transaction](#log_transaction) - Add to a log transaction
* [start_transaction](#start_transaction) - Start a log transaction
* [transaction_status](#transaction_status) - Get the status of a log transaction

## commit_transaction

API to commit a log transaction

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.CommitTransactionRequest(
    transaction_commit_request=shared.TransactionCommitRequest(),
    transaction_id='28541e19-72c2-4c43-bbce-84e4de362101',
)

res = s.transactions.commit_transaction(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CommitTransactionRequest](../../models/operations/committransactionrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CommitTransactionResponse](../../models/operations/committransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## log_transaction

API to add to a log transaction

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.LogTransactionRequest(
    transaction_log_request=shared.TransactionLogRequest(
        segment_tags=[
            shared.SegmentTag(
                key='<key>',
                value='string',
            ),
        ],
    ),
    transaction_id='28541e19-72c2-4c43-bbce-84e4de362101',
)

res = s.transactions.log_transaction(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.LogTransactionRequest](../../models/operations/logtransactionrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.LogTransactionResponse](../../models/operations/logtransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## start_transaction

API to start a log transaction

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = shared.TransactionStartRequest()

res = s.transactions.start_transaction(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.TransactionStartRequest](../../models/shared/transactionstartrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.StartTransactionResponse](../../models/operations/starttransactionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## transaction_status

API to get the status of a log transaction

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird(
    api_key_auth="<YOUR_API_KEY_HERE>",
)

req = operations.TransactionStatusRequest(
    transaction_id='28541e19-72c2-4c43-bbce-84e4de362101',
)

res = s.transactions.transaction_status(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.TransactionStatusRequest](../../models/operations/transactionstatusrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.TransactionStatusResponse](../../models/operations/transactionstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
