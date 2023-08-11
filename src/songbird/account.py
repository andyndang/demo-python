"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from songbird import utils
from songbird.models import errors, operations, shared
from typing import Optional

class Account:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create_account_user(self, request: operations.CreateAccountUserRequest, security: operations.CreateAccountUserSecurity) -> operations.CreateAccountUserResponse:
        r"""Create an account user
        Create an account user
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreateAccountUserRequest, base_url, '/v0/accounts/org/{org_id}/user', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "account_user_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateAccountUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AccountUser])
                res.account_user = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def delete_account_user(self, request: operations.DeleteAccountUserRequest, security: operations.DeleteAccountUserSecurity) -> operations.DeleteAccountUserResponse:
        r"""Delete account user
        Delete an account user's details
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteAccountUserRequest, base_url, '/v0/accounts/org/{org_id}/user/{user_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteAccountUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Void])
                res.void = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_account_memberships(self, request: operations.GetAccountMembershipsRequest, security: operations.GetAccountMembershipsSecurity) -> operations.GetAccountMembershipsResponse:
        r"""Get memberships in an account
        Get memberships in the account organization and any managed organizations
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAccountMembershipsRequest, base_url, '/v0/accounts/org/{org_id}/memberships', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetAccountMembershipsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAccountMembershipsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetAccountMembershipsResponse])
                res.get_account_memberships_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_account_user_by_email(self, request: operations.GetAccountUserByEmailRequest, security: operations.GetAccountUserByEmailSecurity) -> operations.GetAccountUserByEmailResponse:
        r"""Get account user by email
        Get account user by email
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAccountUserByEmailRequest, base_url, '/v0/accounts/org/{org_id}/user/email', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetAccountUserByEmailRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAccountUserByEmailResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AccountUser])
                res.account_user = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_account_user_by_id(self, request: operations.GetAccountUserByIDRequest, security: operations.GetAccountUserByIDSecurity) -> operations.GetAccountUserByIDResponse:
        r"""Get account user by user_id
        Get account user by user_id
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAccountUserByIDRequest, base_url, '/v0/accounts/org/{org_id}/user/id', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetAccountUserByIDRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAccountUserByIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AccountUser])
                res.account_user = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_org_role_memberships(self, request: operations.GetOrgRoleMembershipsRequest, security: operations.GetOrgRoleMembershipsSecurity) -> operations.GetOrgRoleMembershipsResponse:
        r"""Get memberships for a specific org and role
        Get memberships in a specific organization and role within the account
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetOrgRoleMembershipsRequest, base_url, '/v0/accounts/org/{org_id}/memberships/{managed_org_id}/{role}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrgRoleMembershipsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetAccountMembershipsResponse])
                res.get_account_memberships_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def list_account_users(self, request: operations.ListAccountUsersRequest, security: operations.ListAccountUsersSecurity) -> operations.ListAccountUsersResponse:
        r"""List users in an account
        List users in the account organization and any managed organizations
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListAccountUsersRequest, base_url, '/v0/accounts/org/{org_id}/users', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAccountUsersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.AccountUser]])
                res.account_users = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def patch_org_role_memberships(self, request: operations.PatchOrgRoleMembershipsRequest, security: operations.PatchOrgRoleMembershipsSecurity) -> operations.PatchOrgRoleMembershipsResponse:
        r"""Add or delete memberships in a specific role and managed organization
        Add or delete all of the memberships in a specific role and managed organization
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PatchOrgRoleMembershipsRequest, base_url, '/v0/accounts/org/{org_id}/memberships/{managed_org_id}/{role}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PatchOrgRoleMembershipsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Void])
                res.void = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def put_org_role_memberships(self, request: operations.PutOrgRoleMembershipsRequest, security: operations.PutOrgRoleMembershipsSecurity) -> operations.PutOrgRoleMembershipsResponse:
        r"""Replace the memberships in a specific role and managed organization
        Replace all of the memberships in a specific role and managed organization
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PutOrgRoleMembershipsRequest, base_url, '/v0/accounts/org/{org_id}/memberships/{managed_org_id}/{role}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutOrgRoleMembershipsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Void])
                res.void = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def update_account_user(self, request: operations.UpdateAccountUserRequest, security: operations.UpdateAccountUserSecurity) -> operations.UpdateAccountUserResponse:
        r"""Update account user
        Update an account user's details
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateAccountUserRequest, base_url, '/v0/accounts/org/{org_id}/user', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "account_user_request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.UpdateAccountUserRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateAccountUserResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AccountUser])
                res.account_user = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    