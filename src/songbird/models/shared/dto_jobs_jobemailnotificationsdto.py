"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from songbird import utils
from typing import Optional



@dataclasses.dataclass
class DTOJobsJobEmailNotificationsDTOOnFailure:
    pass



@dataclasses.dataclass
class DTOJobsJobEmailNotificationsDTOOnStart:
    pass



@dataclasses.dataclass
class DTOJobsJobEmailNotificationsDTOOnSuccess:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DTOJobsJobEmailNotificationsDTO:
    no_alert_for_skipped_runs: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('noAlertForSkippedRuns'), 'exclude': lambda f: f is None }})
    on_failure: Optional[list[DTOJobsJobEmailNotificationsDTOOnFailure]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onFailure'), 'exclude': lambda f: f is None }})
    on_start: Optional[list[DTOJobsJobEmailNotificationsDTOOnStart]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onStart'), 'exclude': lambda f: f is None }})
    on_success: Optional[list[DTOJobsJobEmailNotificationsDTOOnSuccess]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onSuccess'), 'exclude': lambda f: f is None }})
    

