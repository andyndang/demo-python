"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import membershipmetadata as shared_membershipmetadata
from ..shared import role as shared_role
from typing import Optional



@dataclasses.dataclass
class CreateOrganizationMembershipRequest:
    email: str = dataclasses.field(metadata={'query_param': { 'field_name': 'email', 'style': 'form', 'explode': True }})
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    role: shared_role.Role = dataclasses.field(metadata={'query_param': { 'field_name': 'role', 'style': 'form', 'explode': True }})
    set_default: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'set_default', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class CreateOrganizationMembershipResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    membership_metadata: Optional[shared_membershipmetadata.MembershipMetadata] = dataclasses.field(default=None)
    r"""CreateOrganizationMembership default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

