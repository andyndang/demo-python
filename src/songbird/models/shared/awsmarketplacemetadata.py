"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import marketplacedimensions as shared_marketplacedimensions
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from songbird import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AWSMarketplaceMetadata:
    
    aws_marketplace_customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsMarketplaceCustomerId') }})
    aws_marketplace_product_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsMarketplaceProductCode') }})
    dimension: shared_marketplacedimensions.MarketplaceDimensions = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dimension') }})
    expiration_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expirationTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    expiration_update_time: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expirationUpdateTime'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    org_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orgId') }})
    created_by: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdBy'), 'exclude': lambda f: f is None }})
    