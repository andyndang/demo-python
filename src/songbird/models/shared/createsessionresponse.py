"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from songbird import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateSessionResponse:
    r"""Response for creating sessions"""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Token for the created session, to be passsed into other session APIs."""
    