# PatchAccountMembershipsRequest

Request for the PatchOrgRoleMemberships API


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `user_ids_to_add`                            | list[*str*]                                  | :heavy_check_mark:                           | A list of userIds that should be members     |
| `user_ids_to_delete`                         | list[*str*]                                  | :heavy_check_mark:                           | A list of userIds that should not be members |