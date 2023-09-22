<!-- Start SDK Example Usage -->


```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird(
    security=shared.Security(
        api_key_auth="",
    ),
)

req = operations.CreateAccountUserRequest(
    create_account_user_request=shared.CreateAccountUserRequest(
        active=False,
        email='Larue_Rau85@yahoo.com',
        external_id='corrupti',
        user_schema='illum',
    ),
    org_id='org-123',
)

res = s.account.create_account_user(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->