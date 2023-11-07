"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import notificationsettings as shared_notificationsettings
from typing import Optional


@dataclasses.dataclass
class UpdateNotificationSettingsRequest:
    notification_settings: shared_notificationsettings.NotificationSettings = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class UpdateNotificationSettingsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    notification_settings: Optional[shared_notificationsettings.NotificationSettings] = dataclasses.field(default=None)
    r"""UpdateNotificationSettings default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

