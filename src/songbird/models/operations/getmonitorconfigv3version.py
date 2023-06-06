"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class GetMonitorConfigV3VersionSecurity:
    
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    

@dataclasses.dataclass
class GetMonitorConfigV3VersionRequest:
    
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'dataset_id', 'style': 'simple', 'explode': False }})
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'version_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetMonitorConfigV3VersionResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_monitor_config_v3_version_default_application_json_string: Optional[str] = dataclasses.field(default=None)
    r"""GetMonitorConfigV3Version default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    