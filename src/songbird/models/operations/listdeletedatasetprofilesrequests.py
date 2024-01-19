"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import deleteprofile as shared_deleteprofile
from typing import List, Optional


@dataclasses.dataclass
class ListDeleteDatasetProfilesRequestsRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    r"""Your company's unique organization ID"""
    



@dataclasses.dataclass
class ListDeleteDatasetProfilesRequestsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    classes: Optional[List[shared_deleteprofile.DeleteProfile]] = dataclasses.field(default=None)
    r"""The list of [DeleteProfile] requests if operation succeeds"""
    

