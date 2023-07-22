"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import modelmetadataresponse as shared_modelmetadataresponse
from dataclasses_json import Undefined, dataclass_json
from songbird import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ListModelsResponse:
    r"""Response for the ListModels API"""
    items: list[shared_modelmetadataresponse.ModelMetadataResponse] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    r"""A list of all known model ids for an organization."""
    

