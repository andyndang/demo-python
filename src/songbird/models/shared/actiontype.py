"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class ActionType(str, Enum):
    EMAIL = 'EMAIL'
    SLACK = 'SLACK'
    PAGER_DUTY = 'PAGER_DUTY'
    NA = 'NA'