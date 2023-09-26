"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getnotificationsettingsresponse as shared_getnotificationsettingsresponse
from typing import Optional



@dataclasses.dataclass
class GetNotificationSettingsRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class GetNotificationSettingsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_notification_settings_response: Optional[shared_getnotificationsettingsresponse.GetNotificationSettingsResponse] = dataclasses.field(default=None)
    r"""GetNotificationSettings default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

