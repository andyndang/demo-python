"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import accountuser as shared_accountuser
from ..shared import accountuserrequest as shared_accountuserrequest
from typing import Optional



@dataclasses.dataclass
class UpdateAccountUserSecurity:
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    




@dataclasses.dataclass
class UpdateAccountUserRequest:
    account_user_request: shared_accountuserrequest.AccountUserRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    user_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'user_id', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class UpdateAccountUserResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    account_user: Optional[shared_accountuser.AccountUser] = dataclasses.field(default=None)
    r"""UpdateAccountUser default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

