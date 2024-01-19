"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import registerdatabricksconnectionresponse as shared_registerdatabricksconnectionresponse
from typing import Optional


@dataclasses.dataclass
class RegisterDatabricksConnectionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    register_databricks_connection_response: Optional[shared_registerdatabricksconnectionresponse.RegisterDatabricksConnectionResponse] = dataclasses.field(default=None)
    r"""RegisterDatabricksConnection default response"""
    

