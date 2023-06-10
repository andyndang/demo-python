# notification_settings

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

s = songbird.Songbird()

req = operations.AddNotificationActionRequest(
    request_body='in',
    action_id='user-action',
    org_id='org-123',
    type=shared.ActionType.EMAIL,
)

res = s.notification_settings.add_notification_action(req, operations.AddNotificationActionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.AddNotificationActionRequest](../../models/operations/addnotificationactionrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.AddNotificationActionSecurity](../../models/operations/addnotificationactionsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.AddNotificationActionResponse](../../models/operations/addnotificationactionresponse.md)**


## delete_notification_action

Delete notification action

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.DeleteNotificationActionRequest(
    action_id='user-action',
    org_id='org-123',
)

res = s.notification_settings.delete_notification_action(req, operations.DeleteNotificationActionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.DeleteNotificationActionRequest](../../models/operations/deletenotificationactionrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.DeleteNotificationActionSecurity](../../models/operations/deletenotificationactionsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.DeleteNotificationActionResponse](../../models/operations/deletenotificationactionresponse.md)**


## disable_notification_action

Disable notification action

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.DisableNotificationActionRequest(
    action_id='user-action',
    org_id='org-123',
)

res = s.notification_settings.disable_notification_action(req, operations.DisableNotificationActionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.DisableNotificationActionRequest](../../models/operations/disablenotificationactionrequest.md)   | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `security`                                                                                                   | [operations.DisableNotificationActionSecurity](../../models/operations/disablenotificationactionsecurity.md) | :heavy_check_mark:                                                                                           | The security requirements to use for the request.                                                            |


### Response

**[operations.DisableNotificationActionResponse](../../models/operations/disablenotificationactionresponse.md)**


## enable_notification_action

Enable notification action

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.EnableNotificationActionRequest(
    action_id='user-action',
    org_id='org-123',
)

res = s.notification_settings.enable_notification_action(req, operations.EnableNotificationActionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.EnableNotificationActionRequest](../../models/operations/enablenotificationactionrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.EnableNotificationActionSecurity](../../models/operations/enablenotificationactionsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.EnableNotificationActionResponse](../../models/operations/enablenotificationactionresponse.md)**


## get_notification_action

Get notification action for id

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetNotificationActionRequest(
    action_id='user-action',
    org_id='org-123',
)

res = s.notification_settings.get_notification_action(req, operations.GetNotificationActionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetNotificationActionRequest](../../models/operations/getnotificationactionrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.GetNotificationActionSecurity](../../models/operations/getnotificationactionsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.GetNotificationActionResponse](../../models/operations/getnotificationactionresponse.md)**


## get_notification_settings

Get notification settings for an org

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.GetNotificationSettingsRequest(
    org_id='architecto',
)

res = s.notification_settings.get_notification_settings(req, operations.GetNotificationSettingsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetNotificationSettingsRequest](../../models/operations/getnotificationsettingsrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.GetNotificationSettingsSecurity](../../models/operations/getnotificationsettingssecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.GetNotificationSettingsResponse](../../models/operations/getnotificationsettingsresponse.md)**


## list_notification_actions

Get notification actions for an org

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.ListNotificationActionsRequest(
    org_id='org-123',
)

res = s.notification_settings.list_notification_actions(req, operations.ListNotificationActionsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.ListNotificationActionsRequest](../../models/operations/listnotificationactionsrequest.md)   | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `security`                                                                                               | [operations.ListNotificationActionsSecurity](../../models/operations/listnotificationactionssecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |


### Response

**[operations.ListNotificationActionsResponse](../../models/operations/listnotificationactionsresponse.md)**


## put_notification_action

Add new notification action

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.PutNotificationActionRequest(
    request_body='repudiandae',
    action_id='user-action',
    org_id='org-123',
    type=shared.ActionType.SLACK,
)

res = s.notification_settings.put_notification_action(req, operations.PutNotificationActionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PutNotificationActionRequest](../../models/operations/putnotificationactionrequest.md)   | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `security`                                                                                           | [operations.PutNotificationActionSecurity](../../models/operations/putnotificationactionsecurity.md) | :heavy_check_mark:                                                                                   | The security requirements to use for the request.                                                    |


### Response

**[operations.PutNotificationActionResponse](../../models/operations/putnotificationactionresponse.md)**


## test_notification_action

Test a notification action

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()

req = operations.TestNotificationActionRequest(
    action_id='user-action',
    org_id='org-123',
)

res = s.notification_settings.test_notification_action(req, operations.TestNotificationActionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.TestNotificationActionRequest](../../models/operations/testnotificationactionrequest.md)   | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `security`                                                                                             | [operations.TestNotificationActionSecurity](../../models/operations/testnotificationactionsecurity.md) | :heavy_check_mark:                                                                                     | The security requirements to use for the request.                                                      |


### Response

**[operations.TestNotificationActionResponse](../../models/operations/testnotificationactionresponse.md)**


## update_notification_action

Update notification action

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.UpdateNotificationActionRequest(
    request_body='expedita',
    action_id='user-action',
    org_id='org-123',
    type=shared.ActionType.SLACK,
)

res = s.notification_settings.update_notification_action(req, operations.UpdateNotificationActionSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.UpdateNotificationActionRequest](../../models/operations/updatenotificationactionrequest.md)   | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `security`                                                                                                 | [operations.UpdateNotificationActionSecurity](../../models/operations/updatenotificationactionsecurity.md) | :heavy_check_mark:                                                                                         | The security requirements to use for the request.                                                          |


### Response

**[operations.UpdateNotificationActionResponse](../../models/operations/updatenotificationactionresponse.md)**


## update_notification_settings

Update notification settings for an org

### Example Usage

```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.UpdateNotificationSettingsRequest(
    notification_settings=shared.NotificationSettings(
        email_settings=shared.UberNotificationSchedule(
            cadence=shared.NotificationSqsMessageCadence.INDIVIDUAL,
            day_of_week=shared.NotificationSettingsDay.FRIDAY,
            enabled=False,
            local24_hour_of_day=149448,
            local_minute_of_hour=904648,
            local_timezone='pariatur',
        ),
        pager_duty_settings=shared.UberNotificationSchedule(
            cadence=shared.NotificationSqsMessageCadence.HOURLY,
            day_of_week=shared.NotificationSettingsDay.MONDAY,
            enabled=False,
            local24_hour_of_day=508315,
            local_minute_of_hour=615560,
            local_timezone='magni',
        ),
        slack_settings=shared.UberNotificationSchedule(
            cadence=shared.NotificationSqsMessageCadence.HOURLY,
            day_of_week=shared.NotificationSettingsDay.FRIDAY,
            enabled=False,
            local24_hour_of_day=848009,
            local_minute_of_hour=864934,
            local_timezone='maxime',
        ),
    ),
    org_id='ea',
)

res = s.notification_settings.update_notification_settings(req, operations.UpdateNotificationSettingsSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.UpdateNotificationSettingsRequest](../../models/operations/updatenotificationsettingsrequest.md)   | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `security`                                                                                                     | [operations.UpdateNotificationSettingsSecurity](../../models/operations/updatenotificationsettingssecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |


### Response

**[operations.UpdateNotificationSettingsResponse](../../models/operations/updatenotificationsettingsresponse.md)**


## get_email_notification_action_payload

Get dummy notification action payload

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()


res = s.notification_settings.get_email_notification_action_payload(operations.GetEmailNotificationActionPayloadSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                   | [operations.GetEmailNotificationActionPayloadSecurity](../../models/operations/getemailnotificationactionpayloadsecurity.md) | :heavy_check_mark:                                                                                                           | The security requirements to use for the request.                                                                            |


### Response

**[operations.GetEmailNotificationActionPayloadResponse](../../models/operations/getemailnotificationactionpayloadresponse.md)**


## get_pager_duty_notification_action_payload

Get dummy notification action payload

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()


res = s.notification_settings.get_pager_duty_notification_action_payload(operations.GetPagerDutyNotificationActionPayloadSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                           | [operations.GetPagerDutyNotificationActionPayloadSecurity](../../models/operations/getpagerdutynotificationactionpayloadsecurity.md) | :heavy_check_mark:                                                                                                                   | The security requirements to use for the request.                                                                                    |


### Response

**[operations.GetPagerDutyNotificationActionPayloadResponse](../../models/operations/getpagerdutynotificationactionpayloadresponse.md)**


## get_slack_notification_action_payload

Get dummy notification action payload

### Example Usage

```python
import songbird
from songbird.models import operations

s = songbird.Songbird()


res = s.notification_settings.get_slack_notification_action_payload(operations.GetSlackNotificationActionPayloadSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                   | [operations.GetSlackNotificationActionPayloadSecurity](../../models/operations/getslacknotificationactionpayloadsecurity.md) | :heavy_check_mark:                                                                                                           | The security requirements to use for the request.                                                                            |


### Response

**[operations.GetSlackNotificationActionPayloadResponse](../../models/operations/getslacknotificationactionpayloadresponse.md)**

