"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getsessionresponse as shared_getsessionresponse
from typing import Optional


@dataclasses.dataclass
class GetSessionSecurity:
    
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    

@dataclasses.dataclass
class GetSessionRequest:
    
    session_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'session_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSessionResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_session_response: Optional[shared_getsessionresponse.GetSessionResponse] = dataclasses.field(default=None)
    r"""GetSession default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    