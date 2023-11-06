"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from songbird import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MetricSchema:
    r"""Schema for user-defined metrics"""
    column: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('column') }})
    r"""Entity column to extract the metric from"""
    default_metric: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultMetric') }})
    r"""whylogs metric to extract. Note that other metrics may be available for this column as well, this is the one to be used by default. Should match the values of the SimpleColumnMetric enum within the monitor config schema."""
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label') }})
    r"""User-friendly label for the metric. This should be a unique for the entity."""
    

