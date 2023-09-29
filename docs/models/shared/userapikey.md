# UserAPIKey

Response when creating an API key successfully


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `alias`                                                        | *Optional[str]*                                                | :heavy_minus_sign:                                             | Human-readable alias for the key                               |
| `creation_time`                                                | *Optional[str]*                                                | :heavy_check_mark:                                             | Creation time in human readable format                         |
| `expiration_time`                                              | *Optional[str]*                                                | :heavy_minus_sign:                                             | Expiration time in human readable format                       |
| `key`                                                          | *Optional[str]*                                                | :heavy_minus_sign:                                             | The full value of the key. This is not persisted in the system |
| `key_id`                                                       | *Optional[str]*                                                | :heavy_check_mark:                                             | The key id. Can be used to identify keys for a given user      |
| `org_id`                                                       | *Optional[str]*                                                | :heavy_check_mark:                                             | The organization that the key belongs to                       |
| `revoked`                                                      | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Whether the key has been revoked                               |
| `scopes`                                                       | list[*str*]                                                    | :heavy_minus_sign:                                             | Scope of the key                                               |
| `user_id`                                                      | *Optional[str]*                                                | :heavy_check_mark:                                             | The user that the key represents                               |