"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class DTOClustersAwsAvailabilityDTO(str, Enum):
    SPOT = 'SPOT'
    ON_DEMAND = 'ON_DEMAND'
    SPOT_WITH_FALLBACK = 'SPOT_WITH_FALLBACK'