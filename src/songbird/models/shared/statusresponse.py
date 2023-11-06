"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import errorstatus as shared_errorstatus
from dataclasses_json import Undefined, dataclass_json
from songbird import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StatusResponse:
    errors: Optional[List[shared_errorstatus.ErrorStatus]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors'), 'exclude': lambda f: f is None }})
    request_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requestId') }})
    

