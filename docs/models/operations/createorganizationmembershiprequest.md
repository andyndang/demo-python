# CreateOrganizationMembershipRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `email`                                                  | *Optional[str]*                                          | :heavy_check_mark:                                       | N/A                                                      | user@whylabs.ai                                          |
| `org_id`                                                 | *Optional[str]*                                          | :heavy_check_mark:                                       | N/A                                                      | org-123                                                  |
| `role`                                                   | [Optional[shared.Role]](undefined/models/shared/role.md) | :heavy_check_mark:                                       | N/A                                                      |                                                          |
| `set_default`                                            | *Optional[bool]*                                         | :heavy_minus_sign:                                       | N/A                                                      |                                                          |