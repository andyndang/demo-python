"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import profiletrace as shared_profiletrace
from typing import Optional



@dataclasses.dataclass
class ListProfileTracesSecurity:
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    




@dataclasses.dataclass
class ListProfileTracesRequest:
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'dataset_id', 'style': 'simple', 'explode': False }})
    r"""The unique dataset ID"""
    from_epoch: int = dataclasses.field(metadata={'query_param': { 'field_name': 'from_epoch', 'style': 'form', 'explode': True }})
    r"""Milli epoch time that represents the end of the time range to query."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    r"""Your company's unique organization ID"""
    to_epoch: int = dataclasses.field(metadata={'query_param': { 'field_name': 'to_epoch', 'style': 'form', 'explode': True }})
    r"""Milli epoch time that represents the end of the time range to query."""
    




@dataclasses.dataclass
class ListProfileTracesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    profile_traces: Optional[list[shared_profiletrace.ProfileTrace]] = dataclasses.field(default=None)
    r"""The metadata for the summarized dataset profile including paths to JSON and protobuf data"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
