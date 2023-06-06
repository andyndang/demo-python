"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listorganizationmembershipsresponse as shared_listorganizationmembershipsresponse
from typing import Optional


@dataclasses.dataclass
class ListOrganizationMembershipsSecurity:
    
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    

@dataclasses.dataclass
class ListOrganizationMembershipsRequest:
    
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListOrganizationMembershipsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_organization_memberships_response: Optional[shared_listorganizationmembershipsresponse.ListOrganizationMembershipsResponse] = dataclasses.field(default=None)
    r"""ListOrganizationMemberships default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    