"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import actiontype as shared_actiontype
from ..shared import void as shared_void
from typing import Optional


@dataclasses.dataclass
class AddNotificationActionRequest:
    action_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'action_id', 'style': 'simple', 'explode': False }})
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    request_body: str = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    type: shared_actiontype.ActionType = dataclasses.field(metadata={'path_param': { 'field_name': 'type', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class AddNotificationActionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    void: Optional[shared_void.Void] = dataclasses.field(default=None)
    r"""AddNotificationAction default response"""
    

