"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import entityweightrecord as shared_entityweightrecord
from typing import Optional


@dataclasses.dataclass
class GetColumnWeightsSecurity:
    
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    

@dataclasses.dataclass
class GetColumnWeightsRequest:
    
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'dataset_id', 'style': 'simple', 'explode': False }})
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetColumnWeightsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    entity_weight_record: Optional[shared_entityweightrecord.EntityWeightRecord] = dataclasses.field(default=None)
    r"""GetColumnWeights default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    