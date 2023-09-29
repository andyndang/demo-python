"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import columnschema as shared_columnschema
from ..shared import metricschema as shared_metricschema
from ..shared import schemametadata as shared_schemametadata
from dataclasses_json import Undefined, dataclass_json
from songbird import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class EntitySchema:
    r"""Entity schema for a dataset"""
    columns: dict[str, shared_columnschema.ColumnSchema] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('columns') }})
    r"""Column schema for a given column"""
    metadata: Optional[shared_schemametadata.SchemaMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    metrics: Optional[dict[str, shared_metricschema.MetricSchema]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metrics') }})
    r"""Schema for user-defined metrics (map of unique custom metric labels to their definitions)"""
    

