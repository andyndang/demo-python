"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from songbird import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PatchAccountMembershipsRequest:
    r"""Request for the PatchAccountMemberships API"""
    user_ids_to_add: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userIdsToAdd') }})
    r"""A list of userIds that should be members"""
    user_ids_to_delete: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userIdsToDelete') }})
    r"""A list of userIds that should not be members"""
    

