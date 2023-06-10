"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from songbird import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ProvisionNewMarketplaceUserRequest:
    customer_id_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerIdToken') }})
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    model_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelName') }})
    org_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orgName') }})
    expect_existing: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expectExisting'), 'exclude': lambda f: f is None }})
    

