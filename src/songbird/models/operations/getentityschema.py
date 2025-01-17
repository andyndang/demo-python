"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import entityschema as shared_entityschema
from typing import Optional


@dataclasses.dataclass
class GetEntitySchemaSecurity:
    
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    

@dataclasses.dataclass
class GetEntitySchemaRequest:
    
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'dataset_id', 'style': 'simple', 'explode': False }})
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetEntitySchemaResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    entity_schema: Optional[shared_entityschema.EntitySchema] = dataclasses.field(default=None)
    r"""GetEntitySchema default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    