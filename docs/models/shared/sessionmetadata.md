# SessionMetadata

Response for getting sessions.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `model_id`                                                        | *Optional[str]*                                                   | :heavy_minus_sign:                                                | The model id of the session. There should only be a single model. |
| `org_id`                                                          | *Optional[str]*                                                   | :heavy_minus_sign:                                                | The org id of the session                                         |
| `session_id`                                                      | *Optional[str]*                                                   | :heavy_minus_sign:                                                | The id of the session                                             |
| `user_id`                                                         | *Optional[str]*                                                   | :heavy_minus_sign:                                                | The generated user id for the session.                            |