"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import batchlogreferencerequest as shared_batchlogreferencerequest
from ...models.shared import batchlogsessionreferenceresponse as shared_batchlogsessionreferenceresponse
from typing import Optional


@dataclasses.dataclass
class BatchCreateReferenceProfileUploadRequest:
    batch_log_reference_request: shared_batchlogreferencerequest.BatchLogReferenceRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    session_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'session_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class BatchCreateReferenceProfileUploadResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    batch_log_session_reference_response: Optional[shared_batchlogsessionreferenceresponse.BatchLogSessionReferenceResponse] = dataclasses.field(default=None)
    r"""BatchCreateReferenceProfileUpload default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

