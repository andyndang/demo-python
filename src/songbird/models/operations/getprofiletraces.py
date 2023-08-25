"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import profiletracesresponse as shared_profiletracesresponse
from typing import Optional



@dataclasses.dataclass
class GetProfileTracesSecurity:
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    




@dataclasses.dataclass
class GetProfileTracesRequest:
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'dataset_id', 'style': 'simple', 'explode': False }})
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    trace_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'trace_id', 'style': 'simple', 'explode': False }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class GetProfileTracesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    profile_traces_response: Optional[shared_profiletracesresponse.ProfileTracesResponse] = dataclasses.field(default=None)
    r"""GetProfileTraces default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

