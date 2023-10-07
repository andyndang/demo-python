# NotificationSettings
(*notification_settings*)

### Available Operations

* [add_notification_action](#add_notification_action) - Add new notification action
* [delete_notification_action](#delete_notification_action) - Delete notification action
* [disable_notification_action](#disable_notification_action) - Disable notification action
* [enable_notification_action](#enable_notification_action) - Enable notification action
* [get_notification_action](#get_notification_action) - Get notification action for id
* [get_notification_settings](#get_notification_settings) - Get notification settings for an org
* [list_notification_actions](#list_notification_actions) - List notification actions for an org
* [put_notification_action](#put_notification_action) - Add new notification action
* [test_notification_action](#test_notification_action) - Test a notification action
* [update_notification_action](#update_notification_action) - Update notification action
* [update_notification_settings](#update_notification_settings) - Update notification settings for an org
* [get_email_notification_action_payload](#get_email_notification_action_payload) - Get dummy notification action payload
* [get_pager_duty_notification_action_payload](#get_pager_duty_notification_action_payload) - Get dummy notification action payload
* [get_slack_notification_action_payload](#get_slack_notification_action_payload) - Get dummy notification action payload

## add_notification_action

Add new notification action

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.AddNotificationActionRequest(
    request_body='withdrawal',
    action_id='user-action',
    org_id='org-123',
    type=shared.ActionType.NA,
)

res = s.notification_settings.add_notification_action(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.AddNotificationActionRequest](../../models/operations/addnotificationactionrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.AddNotificationActionResponse](../../models/operations/addnotificationactionresponse.md)**


## delete_notification_action

Delete notification action

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.DeleteNotificationActionRequest(
    action_id='user-action',
    org_id='org-123',
)

res = s.notification_settings.delete_notification_action(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.DeleteNotificationActionRequest](../../models/operations/deletenotificationactionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.DeleteNotificationActionResponse](../../models/operations/deletenotificationactionresponse.md)**


## disable_notification_action

Disable notification action

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.DisableNotificationActionRequest(
    action_id='user-action',
    org_id='org-123',
)

res = s.notification_settings.disable_notification_action(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.DisableNotificationActionRequest](../../models/operations/disablenotificationactionrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.DisableNotificationActionResponse](../../models/operations/disablenotificationactionresponse.md)**


## enable_notification_action

Enable notification action

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.EnableNotificationActionRequest(
    action_id='user-action',
    org_id='org-123',
)

res = s.notification_settings.enable_notification_action(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.EnableNotificationActionRequest](../../models/operations/enablenotificationactionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.EnableNotificationActionResponse](../../models/operations/enablenotificationactionresponse.md)**


## get_notification_action

Get notification action for id

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.GetNotificationActionRequest(
    action_id='user-action',
    org_id='org-123',
)

res = s.notification_settings.get_notification_action(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetNotificationActionRequest](../../models/operations/getnotificationactionrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetNotificationActionResponse](../../models/operations/getnotificationactionresponse.md)**


## get_notification_settings

Get notification settings for an org

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.GetNotificationSettingsRequest(
    org_id='virtual drive parallel',
)

res = s.notification_settings.get_notification_settings(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetNotificationSettingsRequest](../../models/operations/getnotificationsettingsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetNotificationSettingsResponse](../../models/operations/getnotificationsettingsresponse.md)**


## list_notification_actions

Get notification actions for an org

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.ListNotificationActionsRequest(
    org_id='org-123',
)

res = s.notification_settings.list_notification_actions(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ListNotificationActionsRequest](../../models/operations/listnotificationactionsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.ListNotificationActionsResponse](../../models/operations/listnotificationactionsresponse.md)**


## put_notification_action

Add new notification action

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.PutNotificationActionRequest(
    request_body='provided',
    action_id='user-action',
    org_id='org-123',
    type=shared.ActionType.NA,
)

res = s.notification_settings.put_notification_action(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PutNotificationActionRequest](../../models/operations/putnotificationactionrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.PutNotificationActionResponse](../../models/operations/putnotificationactionresponse.md)**


## test_notification_action

Test a notification action

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.TestNotificationActionRequest(
    action_id='user-action',
    org_id='org-123',
)

res = s.notification_settings.test_notification_action(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.TestNotificationActionRequest](../../models/operations/testnotificationactionrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.TestNotificationActionResponse](../../models/operations/testnotificationactionresponse.md)**


## update_notification_action

Update notification action

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.UpdateNotificationActionRequest(
    request_body='female perfectly',
    action_id='user-action',
    org_id='org-123',
    type=shared.ActionType.NA,
)

res = s.notification_settings.update_notification_action(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.UpdateNotificationActionRequest](../../models/operations/updatenotificationactionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.UpdateNotificationActionResponse](../../models/operations/updatenotificationactionresponse.md)**


## update_notification_settings

Update notification settings for an org

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.UpdateNotificationSettingsRequest(
    notification_settings=shared.NotificationSettings(
        email_settings=shared.UberNotificationSchedule(
            cadence=shared.NotificationSqsMessageCadence.HOURLY,
            enabled=False,
        ),
        pager_duty_settings=shared.UberNotificationSchedule(
            cadence=shared.NotificationSqsMessageCadence.DAILY,
            enabled=False,
        ),
        slack_settings=shared.UberNotificationSchedule(
            cadence=shared.NotificationSqsMessageCadence.INDIVIDUAL,
            enabled=False,
        ),
    ),
    org_id='deposit Account',
)

res = s.notification_settings.update_notification_settings(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.UpdateNotificationSettingsRequest](../../models/operations/updatenotificationsettingsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.UpdateNotificationSettingsResponse](../../models/operations/updatenotificationsettingsresponse.md)**


## get_email_notification_action_payload

Get dummy notification action payload

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.notification_settings.get_email_notification_action_payload()

if res.status_code == 200:
    # handle response
```


### Response

**[operations.GetEmailNotificationActionPayloadResponse](../../models/operations/getemailnotificationactionpayloadresponse.md)**


## get_pager_duty_notification_action_payload

Get dummy notification action payload

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.notification_settings.get_pager_duty_notification_action_payload()

if res.status_code == 200:
    # handle response
```


### Response

**[operations.GetPagerDutyNotificationActionPayloadResponse](../../models/operations/getpagerdutynotificationactionpayloadresponse.md)**


## get_slack_notification_action_payload

Get dummy notification action payload

### Example Usage

```python
import songbird
from songbird.models import shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)


res = s.notification_settings.get_slack_notification_action_payload()

if res.status_code == 200:
    # handle response
```


### Response

**[operations.GetSlackNotificationActionPayloadResponse](../../models/operations/getslacknotificationactionpayloadresponse.md)**

