<!-- Start SDK Example Usage -->


```python
import songbird
from songbird.models import operations, shared

s = songbird.Songbird()

req = operations.CreateAccountUserRequest(
    request_body=operations.CreateAccountUserRequestBody(
        user=shared.AccountUser(
            active=False,
            email='Larue_Rau85@yahoo.com',
            external_id='corrupti',
            user_id='illum',
        ),
    ),
    org_id='org-123',
)

res = s.account.create_account_user(req, operations.CreateAccountUserSecurity(
    api_key_auth="",
))

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->