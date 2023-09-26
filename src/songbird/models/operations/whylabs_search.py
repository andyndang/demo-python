"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import searchresponse as shared_searchresponse
from typing import Optional



@dataclasses.dataclass
class WhyLabsSearchRequest:
    query: str = dataclasses.field(metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class WhyLabsSearchResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    search_response: Optional[shared_searchresponse.SearchResponse] = dataclasses.field(default=None)
    r"""WhyLabs Search default response"""
    

