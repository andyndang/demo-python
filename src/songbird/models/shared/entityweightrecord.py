"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import entityweightrecordmetadata as shared_entityweightrecordmetadata
from ..shared import segmentweight as shared_segmentweight
from dataclasses_json import Undefined, dataclass_json
from songbird import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntityWeightRecord:
    r"""GetColumnWeights default response"""
    
    metadata: Optional[shared_entityweightrecordmetadata.EntityWeightRecordMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    segment_weights: Optional[list[shared_segmentweight.SegmentWeight]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('segmentWeights'), 'exclude': lambda f: f is None }})
    r"""A list of entity weights for a segment"""
    