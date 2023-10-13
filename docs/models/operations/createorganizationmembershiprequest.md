# CreateOrganizationMembershipRequest


## Fields

| Field                                      | Type                                       | Required                                   | Description                                | Example                                    |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `email`                                    | *str*                                      | :heavy_check_mark:                         | N/A                                        | user@whylabs.ai                            |
| `org_id`                                   | *str*                                      | :heavy_check_mark:                         | N/A                                        | org-123                                    |
| `role`                                     | [shared.Role](../../models/shared/role.md) | :heavy_check_mark:                         | N/A                                        |                                            |
| `set_default`                              | *Optional[bool]*                           | :heavy_minus_sign:                         | N/A                                        |                                            |