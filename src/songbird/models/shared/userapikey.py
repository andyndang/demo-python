"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from songbird import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UserAPIKey:
    r"""Response when creating an API key successfully"""
    
    creation_time: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creationTime') }})
    r"""Creation time in human readable format"""
    key_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('keyId') }})
    r"""The key id. Can be used to identify keys for a given user"""
    org_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orgId') }})
    r"""The organization that the key belongs to"""
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userId') }})
    r"""The user that the key represents"""
    alias: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alias'), 'exclude': lambda f: f is None }})
    r"""Human-readable alias for the key"""
    expiration_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expirationTime'), 'exclude': lambda f: f is None }})
    r"""Expiration time in human readable format"""
    key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key'), 'exclude': lambda f: f is None }})
    r"""The full value of the key. This is not persisted in the system"""
    revoked: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('revoked'), 'exclude': lambda f: f is None }})
    r"""Whether the key has been revoked"""
    scopes: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scopes'), 'exclude': lambda f: f is None }})
    r"""Scope of the key"""
    