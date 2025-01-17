"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import emailnotificationaction as shared_emailnotificationaction
from typing import Optional


@dataclasses.dataclass
class GetEmailNotificationActionPayloadSecurity:
    
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    

@dataclasses.dataclass
class GetEmailNotificationActionPayloadResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    email_notification_action: Optional[shared_emailnotificationaction.EmailNotificationAction] = dataclasses.field(default=None)
    r"""getEmailNotificationActionPayload default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    