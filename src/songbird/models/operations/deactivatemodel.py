"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import modelmetadataresponse as shared_modelmetadataresponse
from typing import Optional


@dataclasses.dataclass
class DeactivateModelSecurity:
    
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    

@dataclasses.dataclass
class DeactivateModelRequest:
    
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'model_id', 'style': 'simple', 'explode': False }})
    r"""The model ID"""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    r"""The organization ID"""
    

@dataclasses.dataclass
class DeactivateModelResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model_metadata_response: Optional[shared_modelmetadataresponse.ModelMetadataResponse] = dataclasses.field(default=None)
    r"""The [ModelMetadataResponse] if operation succeeds"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    