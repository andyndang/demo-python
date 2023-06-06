"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import logreferencerequest as shared_logreferencerequest
from ..shared import logreferenceresponse as shared_logreferenceresponse
from typing import Optional


@dataclasses.dataclass
class LogReferenceSecurity:
    
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    

@dataclasses.dataclass
class LogReferenceRequest:
    
    log_reference_request: shared_logreferencerequest.LogReferenceRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'model_id', 'style': 'simple', 'explode': False }})
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class LogReferenceResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    log_reference_response: Optional[shared_logreferenceresponse.LogReferenceResponse] = dataclasses.field(default=None)
    r"""LogReference default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    