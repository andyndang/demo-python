"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .dto_clusters_autoscaledto import DTOClustersAutoScaleDTO
from .dto_clusters_awsattributesdto import DTOClustersAwsAttributesDTO
from .dto_clusters_clusterlogconfdto import DTOClustersClusterLogConfDTO
from .dto_jobs_datasecuritymodedto import DTOJobsDataSecurityModeDTO
from dataclasses_json import Undefined, dataclass_json
from songbird import utils
from typing import Dict, List, Optional


@dataclasses.dataclass
class InitScripts:
    pass


@dataclasses.dataclass
class SSHPublicKeys:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DTOJobsNewClusterDTO:
    artifact_paths: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('artifactPaths'), 'exclude': lambda f: f is None }})
    auto_scale: Optional[DTOClustersAutoScaleDTO] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('autoScale'), 'exclude': lambda f: f is None }})
    auto_termination_minutes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('autoTerminationMinutes'), 'exclude': lambda f: f is None }})
    aws_attributes: Optional[DTOClustersAwsAttributesDTO] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('awsAttributes'), 'exclude': lambda f: f is None }})
    cluster_log_conf: Optional[DTOClustersClusterLogConfDTO] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clusterLogConf'), 'exclude': lambda f: f is None }})
    cluster_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clusterName'), 'exclude': lambda f: f is None }})
    custom_tags: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customTags'), 'exclude': lambda f: f is None }})
    data_security_mode: Optional[DTOJobsDataSecurityModeDTO] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataSecurityMode'), 'exclude': lambda f: f is None }})
    driver_node_type_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('driverNodeTypeId'), 'exclude': lambda f: f is None }})
    enable_elastic_disk: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enableElasticDisk'), 'exclude': lambda f: f is None }})
    init_scripts: Optional[List[InitScripts]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initScripts'), 'exclude': lambda f: f is None }})
    instance_pool_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instancePoolId'), 'exclude': lambda f: f is None }})
    node_type_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nodeTypeId'), 'exclude': lambda f: f is None }})
    num_workers: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('numWorkers'), 'exclude': lambda f: f is None }})
    policy_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('policyId'), 'exclude': lambda f: f is None }})
    runtime_engine: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('runtimeEngine'), 'exclude': lambda f: f is None }})
    spark_conf: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sparkConf'), 'exclude': lambda f: f is None }})
    spark_env_vars: Optional[Dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sparkEnvVars'), 'exclude': lambda f: f is None }})
    spark_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sparkVersion'), 'exclude': lambda f: f is None }})
    ssh_public_keys: Optional[List[SSHPublicKeys]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sshPublicKeys'), 'exclude': lambda f: f is None }})
    

