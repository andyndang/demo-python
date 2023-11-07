"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .organizationrolemembers import OrganizationRoleMembers
from dataclasses_json import Undefined, dataclass_json
from songbird import utils
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetAccountMembershipsResponse:
    r"""Response for the GetAccountMemberships API"""
    memberships: List[OrganizationRoleMembers] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('memberships') }})
    r"""A list of memberships in the account"""
    

