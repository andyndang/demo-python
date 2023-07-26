"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import dto_clusters_awsavailabilitydto as shared_dto_clusters_awsavailabilitydto
from ..shared import dto_ebsvolumetypedto as shared_dto_ebsvolumetypedto
from dataclasses_json import Undefined, dataclass_json
from songbird import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DTOClustersAwsAttributesDTO:
    availability: Optional[shared_dto_clusters_awsavailabilitydto.DTOClustersAwsAvailabilityDTO] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('availability'), 'exclude': lambda f: f is None }})
    ebs_volume_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ebsVolumeCount'), 'exclude': lambda f: f is None }})
    ebs_volume_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ebsVolumeSize'), 'exclude': lambda f: f is None }})
    ebs_volume_type: Optional[shared_dto_ebsvolumetypedto.DTOEbsVolumeTypeDTO] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ebsVolumeType'), 'exclude': lambda f: f is None }})
    first_on_demand: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('firstOnDemand'), 'exclude': lambda f: f is None }})
    instance_profile_arn: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instanceProfileArn'), 'exclude': lambda f: f is None }})
    spot_bid_price_percent: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('spotBidPricePercent'), 'exclude': lambda f: f is None }})
    zone_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('zoneId'), 'exclude': lambda f: f is None }})
    

