"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import accountuser as shared_accountuser
from dataclasses_json import Undefined, dataclass_json
from songbird import utils
from typing import Optional



@dataclasses.dataclass
class CreateAccountUserSecurity:
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class CreateAccountUserRequestBody:
    user: Optional[shared_accountuser.AccountUser] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})
    r"""Information held about a user in an account"""
    




@dataclasses.dataclass
class CreateAccountUserRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    request_body: CreateAccountUserRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class CreateAccountUserResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    account_user: Optional[shared_accountuser.AccountUser] = dataclasses.field(default=None)
    r"""CreateAccountUser default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

