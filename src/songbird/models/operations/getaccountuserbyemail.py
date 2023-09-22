"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import accountuser as shared_accountuser
from typing import Optional



@dataclasses.dataclass
class GetAccountUserByEmailRequest:
    email: str = dataclasses.field(metadata={'query_param': { 'field_name': 'email', 'style': 'form', 'explode': True }})
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    




@dataclasses.dataclass
class GetAccountUserByEmailResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    account_user: Optional[shared_accountuser.AccountUser] = dataclasses.field(default=None)
    r"""GetAccountUserByEmail default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

