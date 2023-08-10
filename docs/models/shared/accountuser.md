# AccountUser

Account User metadata


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `active`                               | *Optional[bool]*                       | :heavy_minus_sign:                     | Flag to indicate if the user is active |
| `email`                                | *Optional[str]*                        | :heavy_minus_sign:                     | The user's email address               |
| `id`                                   | *str*                                  | :heavy_check_mark:                     | The account user id                    |
| `org_id`                               | *Optional[str]*                        | :heavy_minus_sign:                     | The WhyLabs organization id            |
| `source_id`                            | *Optional[str]*                        | :heavy_minus_sign:                     | Source provider id                     |
| `source_user_id`                       | *Optional[str]*                        | :heavy_minus_sign:                     | Source user id                         |
| `user_id`                              | *str*                                  | :heavy_check_mark:                     | The WhyLabs user id                    |
| `user_schema`                          | *Optional[str]*                        | :heavy_minus_sign:                     | User schema                            |