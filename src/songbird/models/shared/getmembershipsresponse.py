"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import membership as shared_membership
from dataclasses_json import Undefined, dataclass_json
from songbird import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetMembershipsResponse:
    r"""Response for the GetMemberships API"""
    memberships: List[shared_membership.Membership] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberships') }})
    r"""A list of all memberships that a user has."""
    

