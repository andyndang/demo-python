"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listmodelsresponse as shared_listmodelsresponse
from typing import Optional



@dataclasses.dataclass
class ListModelsSecurity:
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    




@dataclasses.dataclass
class ListModelsRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    r"""Your company's unique organization ID"""
    




@dataclasses.dataclass
class ListModelsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_models_response: Optional[shared_listmodelsresponse.ListModelsResponse] = dataclasses.field(default=None)
    r"""A list of model summary items"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

