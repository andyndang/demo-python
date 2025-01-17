"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deleteanalyzerresultsresponse as shared_deleteanalyzerresultsresponse
from typing import Optional


@dataclasses.dataclass
class DeleteAnalyzerResultsSecurity:
    
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    

@dataclasses.dataclass
class DeleteAnalyzerResultsRequest:
    
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'dataset_id', 'style': 'simple', 'explode': False }})
    r"""The unique dataset ID in your company."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    r"""Your company's unique organization ID"""
    end_timestamp: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end_timestamp', 'style': 'form', 'explode': True }})
    r"""Optional, scope deleting analyzer results older than the timestamp"""
    start_timestamp: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'start_timestamp', 'style': 'form', 'explode': True }})
    r"""Optional, scope deleting analyzer results more recent than the timestamp"""
    

@dataclasses.dataclass
class DeleteAnalyzerResultsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_analyzer_results_response: Optional[shared_deleteanalyzerresultsresponse.DeleteAnalyzerResultsResponse] = dataclasses.field(default=None)
    r"""The [DeleteAnalyzerResultsResponse] if operation succeeds"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    