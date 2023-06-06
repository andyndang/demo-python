"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getconnectionresponse as shared_getconnectionresponse
from typing import Optional


@dataclasses.dataclass
class GetConnectionSecurity:
    
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    

@dataclasses.dataclass
class GetConnectionResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_connection_response: Optional[shared_getconnectionresponse.GetConnectionResponse] = dataclasses.field(default=None)
    r"""GetConnection default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    