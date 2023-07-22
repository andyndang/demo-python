# RunJobRequest


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `job_id`                                                        | *int*                                                           | :heavy_check_mark:                                              | The id of the job to run in the connected Databricks workspace. |
| `org_id`                                                        | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Look up a connection by the org that is connected to.           |
| `workspace_id`                                                  | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Look up a connection by the workspace that it originates from.  |