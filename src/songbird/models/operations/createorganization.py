"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import organizationsummary as shared_organizationsummary
from ..shared import subscriptiontier as shared_subscriptiontier
from typing import Optional



@dataclasses.dataclass
class CreateOrganizationRequest:
    name: str = dataclasses.field(metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""The name of the organization"""
    domain: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'domain', 'style': 'form', 'explode': True }})
    r"""Domain associated with this organization"""
    email_domains: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'email_domains', 'style': 'form', 'explode': True }})
    r"""Email domains associated with this organization, as a comma separated list"""
    notification_email_address: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'notification_email_address', 'style': 'form', 'explode': True }})
    r"""Email address that should be used for notifications for this organization"""
    observatory_url: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'observatory_url', 'style': 'form', 'explode': True }})
    r"""Url that users of this organization will be redirected to in some cases (such as via Siren notifications). NOTE: should NOT be followed by a trailing slash!"""
    override_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'override_id', 'style': 'form', 'explode': True }})
    r"""Custom ID. If this ID is invalid this method will throw an exception"""
    pager_duty_key: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pager_duty_key', 'style': 'form', 'explode': True }})
    parent_org_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'parent_org_id', 'style': 'form', 'explode': True }})
    slack_webhook: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'slack_webhook', 'style': 'form', 'explode': True }})
    r"""Slack Webhook that should be used for notifications for this organization"""
    subscription_tier: Optional[shared_subscriptiontier.SubscriptionTier] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'subscription_tier', 'style': 'form', 'explode': True }})
    r"""Organization's subscription tier. Should be PAID for real customers"""
    




@dataclasses.dataclass
class CreateOrganizationResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    organization_summary: Optional[shared_organizationsummary.OrganizationSummary] = dataclasses.field(default=None)
    r"""A summary of the organization object if succeeds"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

