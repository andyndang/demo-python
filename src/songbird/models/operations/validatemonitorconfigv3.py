"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import response as shared_response
from typing import Optional



@dataclasses.dataclass
class ValidateMonitorConfigV3Request:
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'dataset_id', 'style': 'simple', 'explode': False }})
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    request_body: str = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    verbose: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'verbose', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class ValidateMonitorConfigV3Response:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    response: Optional[shared_response.Response] = dataclasses.field(default=None)
    r"""ValidateMonitorConfigV3 default response"""
    

