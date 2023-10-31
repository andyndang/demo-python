"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import getmarketplacemetadataresponse as shared_getmarketplacemetadataresponse
from typing import Optional


@dataclasses.dataclass
class GetAWSMarketplaceMetadataRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetAWSMarketplaceMetadataResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    get_marketplace_metadata_response: Optional[shared_getmarketplacemetadataresponse.GetMarketplaceMetadataResponse] = dataclasses.field(default=None)
    r"""GetAWSMarketplaceMetadata default response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

