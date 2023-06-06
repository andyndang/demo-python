"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import organizationsummary as shared_organizationsummary
from ..shared import subscriptiontier as shared_subscriptiontier
from dataclasses_json import Undefined, dataclass_json
from songbird import utils
from typing import Optional


@dataclasses.dataclass
class PartiallyUpdateOrgSecurity:
    
    api_key_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'X-API-Key' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PartiallyUpdateOrgRequestBody:
    
    org_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_id'), 'exclude': lambda f: f is None }})
    r"""The unique ID of an organization. If an organization with this ID does not exist, this method will throw an exception."""
    

@dataclasses.dataclass
class PartiallyUpdateOrgRequest:
    
    request_body: PartiallyUpdateOrgRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    domain: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'domain', 'style': 'form', 'explode': True }})
    r"""Domain associated with this organization"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""The name of the organization"""
    notification_email_address: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'notification_email_address', 'style': 'form', 'explode': True }})
    r"""Email address that should be used for notifications for this organization"""
    observatory_url: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'observatory_url', 'style': 'form', 'explode': True }})
    r"""Url that users of this organization will be redirected to in some cases (such as via Siren notifications). NOTE: should NOT be followed by a trailing slash!"""
    slack_webhook: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'slack_webhook', 'style': 'form', 'explode': True }})
    r"""Slack Webhook that should be used for notifications for this organization"""
    subscription_tier: Optional[shared_subscriptiontier.SubscriptionTier] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'subscription_tier', 'style': 'form', 'explode': True }})
    r"""Organization's subscription tier. Should be PAID for real customers"""
    

@dataclasses.dataclass
class PartiallyUpdateOrgResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    organization_summary: Optional[shared_organizationsummary.OrganizationSummary] = dataclasses.field(default=None)
    r"""A summary of the organization object if succeeds"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    