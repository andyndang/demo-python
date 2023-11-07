"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import deleteanalyzerresultsresponse as shared_deleteanalyzerresultsresponse
from typing import Optional


@dataclasses.dataclass
class DeleteAnalyzerResultsRequest:
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'dataset_id', 'style': 'simple', 'explode': False }})
    r"""The unique dataset ID in your company."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    r"""Your company's unique organization ID"""
    end_timestamp: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end_timestamp', 'style': 'form', 'explode': True }})
    start_timestamp: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'start_timestamp', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class DeleteAnalyzerResultsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    delete_analyzer_results_response: Optional[shared_deleteanalyzerresultsresponse.DeleteAnalyzerResultsResponse] = dataclasses.field(default=None)
    r"""The [DeleteAnalyzerResultsResponse] if operation succeeds"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

