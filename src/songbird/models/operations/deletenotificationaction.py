"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Any, Optional


@dataclasses.dataclass
class DeleteNotificationActionSecurity:
    
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    

@dataclasses.dataclass
class DeleteNotificationActionRequest:
    
    action_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'action_id', 'style': 'simple', 'explode': False }})
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteNotificationActionResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    void: Optional[dict[str, Any]] = dataclasses.field(default=None)
    r"""DeleteNotificationAction default response"""
    