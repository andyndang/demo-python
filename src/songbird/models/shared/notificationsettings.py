"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import ubernotificationschedule as shared_ubernotificationschedule
from dataclasses_json import Undefined, dataclass_json
from songbird import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NotificationSettings:
    r"""Settings that control how and when notifications are delivered."""
    
    email_settings: Optional[shared_ubernotificationschedule.UberNotificationSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailSettings'), 'exclude': lambda f: f is None }})
    r"""Combination of all possible schedule types, a hacky workaround for bugs in generated clients that use polymorphic types.
    There are three types of schedules. Weekly, Daily, and Individual. You need to set the right fields for each one.
    
    Weekly:
        enabled, cadence=WEEKLY, dayOfWeek, local24HourOfDay, localMinuteOfHour, localTimezone
        
    Daily:
        enabled, cadence=DAILY, local24HourOfDay, localMinuteOfHour, localTimezone
        
    Individual:
        enabled, cadence=INDIVIDUAL
    """
    pager_duty_settings: Optional[shared_ubernotificationschedule.UberNotificationSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagerDutySettings'), 'exclude': lambda f: f is None }})
    r"""Combination of all possible schedule types, a hacky workaround for bugs in generated clients that use polymorphic types.
    There are three types of schedules. Weekly, Daily, and Individual. You need to set the right fields for each one.
    
    Weekly:
        enabled, cadence=WEEKLY, dayOfWeek, local24HourOfDay, localMinuteOfHour, localTimezone
        
    Daily:
        enabled, cadence=DAILY, local24HourOfDay, localMinuteOfHour, localTimezone
        
    Individual:
        enabled, cadence=INDIVIDUAL
    """
    slack_settings: Optional[shared_ubernotificationschedule.UberNotificationSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slackSettings'), 'exclude': lambda f: f is None }})
    r"""Combination of all possible schedule types, a hacky workaround for bugs in generated clients that use polymorphic types.
    There are three types of schedules. Weekly, Daily, and Individual. You need to set the right fields for each one.
    
    Weekly:
        enabled, cadence=WEEKLY, dayOfWeek, local24HourOfDay, localMinuteOfHour, localTimezone
        
    Daily:
        enabled, cadence=DAILY, local24HourOfDay, localMinuteOfHour, localTimezone
        
    Individual:
        enabled, cadence=INDIVIDUAL
    """
    