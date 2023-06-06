"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from songbird import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProvisionNewUserResponse:
    r"""ProvisionNewUser default response"""
    
    model_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId') }})
    org_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orgId') }})
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userId') }})
    