"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class GetMonitorConfigV3Request:
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'dataset_id', 'style': 'simple', 'explode': False }})
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    include_entity_schema: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include_entity_schema', 'style': 'form', 'explode': True }})
    include_entity_weights: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include_entity_weights', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class GetMonitorConfigV3Response:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    res: Optional[str] = dataclasses.field(default=None)
    r"""GetMonitorConfigV3 default response"""
    

