"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import dto_jobs_cronscheduledto as shared_dto_jobs_cronscheduledto
from ..shared import dto_jobs_jobemailnotificationsdto as shared_dto_jobs_jobemailnotificationsdto
from ..shared import dto_jobs_newclusterdto as shared_dto_jobs_newclusterdto
from ..shared import dto_jobs_notebooktaskdto as shared_dto_jobs_notebooktaskdto
from ..shared import dto_jobs_sparkjartaskdto as shared_dto_jobs_sparkjartaskdto
from ..shared import dto_jobs_sparkpythontaskdto as shared_dto_jobs_sparkpythontaskdto
from ..shared import dto_jobs_sparksubmittaskdto as shared_dto_jobs_sparksubmittaskdto
from dataclasses_json import Undefined, dataclass_json
from songbird import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DTOJobsJobSettingsDTO:
    
    email_notifications: Optional[shared_dto_jobs_jobemailnotificationsdto.DTOJobsJobEmailNotificationsDTO] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('emailNotifications'), 'exclude': lambda f: f is None }})
    existing_cluster_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('existingClusterId'), 'exclude': lambda f: f is None }})
    libraries: Optional[list[dict[str, Any]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('libraries'), 'exclude': lambda f: f is None }})
    max_concurrent_runs: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxConcurrentRuns'), 'exclude': lambda f: f is None }})
    max_retries: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('maxRetries'), 'exclude': lambda f: f is None }})
    min_retry_interval_millis: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('minRetryIntervalMillis'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    new_cluster: Optional[shared_dto_jobs_newclusterdto.DTOJobsNewClusterDTO] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('newCluster'), 'exclude': lambda f: f is None }})
    notebook_task: Optional[shared_dto_jobs_notebooktaskdto.DTOJobsNotebookTaskDTO] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notebookTask'), 'exclude': lambda f: f is None }})
    retry_on_timeout: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('retryOnTimeout'), 'exclude': lambda f: f is None }})
    schedule: Optional[shared_dto_jobs_cronscheduledto.DTOJobsCronScheduleDTO] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule'), 'exclude': lambda f: f is None }})
    spark_jar_task: Optional[shared_dto_jobs_sparkjartaskdto.DTOJobsSparkJarTaskDTO] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sparkJarTask'), 'exclude': lambda f: f is None }})
    spark_python_task: Optional[shared_dto_jobs_sparkpythontaskdto.DTOJobsSparkPythonTaskDTO] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sparkPythonTask'), 'exclude': lambda f: f is None }})
    spark_submit_task: Optional[shared_dto_jobs_sparksubmittaskdto.DTOJobsSparkSubmitTaskDTO] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sparkSubmitTask'), 'exclude': lambda f: f is None }})
    timeout_seconds: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeoutSeconds'), 'exclude': lambda f: f is None }})
    