"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import modelmetadataresponse as shared_modelmetadataresponse
from ..shared import modeltype as shared_modeltype
from ..shared import timeperiod as shared_timeperiod
from typing import Optional


@dataclasses.dataclass
class UpdateModelSecurity:
    
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    

@dataclasses.dataclass
class UpdateModelRequest:
    
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'model_id', 'style': 'simple', 'explode': False }})
    r"""The model ID"""
    model_name: str = dataclasses.field(metadata={'query_param': { 'field_name': 'model_name', 'style': 'form', 'explode': True }})
    r"""The name of a model"""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    r"""The organization ID"""
    time_period: shared_timeperiod.TimePeriod = dataclasses.field(metadata={'query_param': { 'field_name': 'time_period', 'style': 'form', 'explode': True }})
    r"""The [TimePeriod] for data aggregation/alerting for a model"""
    model_type: Optional[shared_modeltype.ModelType] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'model_type', 'style': 'form', 'explode': True }})
    r"""The [ModelType] of the dataset"""
    

@dataclasses.dataclass
class UpdateModelResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    model_metadata_response: Optional[shared_modelmetadataresponse.ModelMetadataResponse] = dataclasses.field(default=None)
    r"""The [ModelMetadataResponse] if operation succeeds"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    