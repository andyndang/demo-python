"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import userapikey as shared_userapikey
from typing import Optional


@dataclasses.dataclass
class RevokeAPIKeyRequest:
    key_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'key_id', 'style': 'form', 'explode': True }})
    r"""ID of the key to revoke
     Metadata for the revoked API Key
    """
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    user_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'user_id', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class RevokeAPIKeyResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    user_api_key: Optional[shared_userapikey.UserAPIKey] = dataclasses.field(default=None)
    r"""Revoked API Key's metadata"""
    

