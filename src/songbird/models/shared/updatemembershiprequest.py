"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import role as shared_role
from dataclasses_json import Undefined, dataclass_json
from songbird import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateMembershipRequest:
    
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    org_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orgId') }})
    role: shared_role.Role = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    