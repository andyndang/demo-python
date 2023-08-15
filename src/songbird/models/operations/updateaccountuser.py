"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import accountuser as shared_accountuser
from ..shared import updateaccountuserrequest as shared_updateaccountuserrequest
from typing import Optional



@dataclasses.dataclass
class UpdateAccountUserSecurity:
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    




@dataclasses.dataclass
class UpdateAccountUserRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    update_account_user_request: shared_updateaccountuserrequest.UpdateAccountUserRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    user_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'user_id', 'style': 'form', 'explode': True }})
    




@dataclasses.dataclass
class UpdateAccountUserResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    account_user: Optional[shared_accountuser.AccountUser] = dataclasses.field(default=None)
    r"""UpdateAccountUser default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

