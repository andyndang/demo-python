"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deletedatasetprofilesresponse as shared_deletedatasetprofilesresponse
from typing import Optional


@dataclasses.dataclass
class DeleteDatasetProfilesSecurity:
    
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    

@dataclasses.dataclass
class DeleteDatasetProfilesRequest:
    
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'dataset_id', 'style': 'simple', 'explode': False }})
    r"""The unique dataset ID in your company."""
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    r"""Your company's unique organization ID"""
    before_upload_timestamp: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'before_upload_timestamp', 'style': 'form', 'explode': True }})
    r"""Optional, scope deleting profiles uploaded prior to the timestamp"""
    profile_end_timestamp: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'profile_end_timestamp', 'style': 'form', 'explode': True }})
    r"""Optional, scope deleting profiles older than the timestamp"""
    profile_start_timestamp: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'profile_start_timestamp', 'style': 'form', 'explode': True }})
    r"""Optional, scope deleting profiles more recently than the timestamp"""
    

@dataclasses.dataclass
class DeleteDatasetProfilesResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_dataset_profiles_response: Optional[shared_deletedatasetprofilesresponse.DeleteDatasetProfilesResponse] = dataclasses.field(default=None)
    r"""The [DeleteDatasetProfilesResponse] if operation succeeds"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    