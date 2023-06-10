"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import membershipmetadata as shared_membershipmetadata
from typing import Optional



@dataclasses.dataclass
class UpdateMembershipByEmailSecurity:
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    




@dataclasses.dataclass
class UpdateMembershipByEmailResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    membership_metadata: Optional[shared_membershipmetadata.MembershipMetadata] = dataclasses.field(default=None)
    r"""UpdateMembershipByEmail default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

