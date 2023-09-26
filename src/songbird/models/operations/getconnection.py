"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getconnectionresponse as shared_getconnectionresponse
from typing import Optional



@dataclasses.dataclass
class GetConnectionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_connection_response: Optional[shared_getconnectionresponse.GetConnectionResponse] = dataclasses.field(default=None)
    r"""GetConnection default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

