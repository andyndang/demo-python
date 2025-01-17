"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import dto_jobs_jobsettingsdto as shared_dto_jobs_jobsettingsdto
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from songbird import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DTOJobsJobDTO:
    
    created_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    creator_user_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creatorUserName'), 'exclude': lambda f: f is None }})
    job_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jobId'), 'exclude': lambda f: f is None }})
    settings: Optional[shared_dto_jobs_jobsettingsdto.DTOJobsJobSettingsDTO] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('settings'), 'exclude': lambda f: f is None }})
    