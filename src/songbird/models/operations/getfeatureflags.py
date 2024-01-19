"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import featureflags as shared_featureflags
from typing import Optional


@dataclasses.dataclass
class GetFeatureFlagsRequest:
    org_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'org_id', 'style': 'form', 'explode': True }})
    user_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'user_id', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class GetFeatureFlagsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    feature_flags: Optional[shared_featureflags.FeatureFlags] = dataclasses.field(default=None)
    r"""GetFeatureFlags default response"""
    

