"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from songbird import utils
from songbird.models import operations, shared
from typing import Any, Optional

class Membership:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create_membership(self, request: shared.AddMembershipRequest, security: operations.CreateMembershipSecurity) -> operations.CreateMembershipResponse:
        r"""Create a membership for a user, making them apart of an organization. Uses the user's current email address.
        Create a membership for a user, making them apart of an organization. Uses the user's current email address.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v0/membership'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateMembershipResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.MembershipMetadata])
                res.membership_metadata = out

        return res

    
    def create_organization_membership(self, request: operations.CreateOrganizationMembershipRequest, security: operations.CreateOrganizationMembershipSecurity) -> operations.CreateOrganizationMembershipResponse:
        r"""Create a membership for a user, making them apart of an organization. Uses the user's current email address.
        Create a membership for a user, making them apart of an organization. Uses the user's current email address.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreateOrganizationMembershipRequest, base_url, '/v0/organizations/{org_id}/membership', request)
        headers = {}
        query_params = utils.get_query_params(operations.CreateOrganizationMembershipRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateOrganizationMembershipResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.MembershipMetadata])
                res.membership_metadata = out

        return res

    
    def get_default_membership_for_email(self, request: operations.GetDefaultMembershipForEmailRequest, security: operations.GetDefaultMembershipForEmailSecurity) -> operations.GetDefaultMembershipForEmailResponse:
        r"""Get the default membership for a user.
        Get the default membership for a user.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v0/membership/default'
        headers = {}
        query_params = utils.get_query_params(operations.GetDefaultMembershipForEmailRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDefaultMembershipForEmailResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetDefaultMembershipResponse])
                res.get_default_membership_response = out

        return res

    
    def get_memberships(self, request: operations.GetMembershipsRequest, security: operations.GetMembershipsSecurity) -> operations.GetMembershipsResponse:
        r"""Get memberships for a user.
        Get memberships for a user.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetMembershipsRequest, base_url, '/v0/membership/user/{user_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetMembershipsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetMembershipsResponse])
                res.get_memberships_response = out

        return res

    
    def get_memberships_by_email(self, request: operations.GetMembershipsByEmailRequest, security: operations.GetMembershipsByEmailSecurity) -> operations.GetMembershipsByEmailResponse:
        r"""Get memberships for a user given that user's email address.
        Get memberships for a user given that user's email address.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v0/membership/user'
        headers = {}
        query_params = utils.get_query_params(operations.GetMembershipsByEmailRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetMembershipsByEmailResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetMembershipsResponse])
                res.get_memberships_response = out

        return res

    
    def get_memberships_by_org(self, request: operations.GetMembershipsByOrgRequest, security: operations.GetMembershipsByOrgSecurity) -> operations.GetMembershipsByOrgResponse:
        r"""Get memberships for an org.
        Get memberships for an org.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetMembershipsByOrgRequest, base_url, '/v0/membership/org/{org_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetMembershipsByOrgResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetMembershipsResponse])
                res.get_memberships_response = out

        return res

    
    def list_organization_memberships(self, request: operations.ListOrganizationMembershipsRequest, security: operations.ListOrganizationMembershipsSecurity) -> operations.ListOrganizationMembershipsResponse:
        r"""List organization memberships
        list memberships for an organization
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListOrganizationMembershipsRequest, base_url, '/v0/organizations/{org_id}/membership', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListOrganizationMembershipsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ListOrganizationMembershipsResponse])
                res.list_organization_memberships_response = out

        return res

    
    def remove_membership_by_email(self, request: shared.RemoveMembershipRequest, security: operations.RemoveMembershipByEmailSecurity) -> operations.RemoveMembershipByEmailResponse:
        r"""Removes membership in a given org from a user, using the user's email address.
        Removes membership in a given org from a user, using the user's email address.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v0/membership'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('DELETE', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RemoveMembershipByEmailResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Response])
                res.response = out

        return res

    
    def remove_organization_membership(self, request: operations.RemoveOrganizationMembershipRequest, security: operations.RemoveOrganizationMembershipSecurity) -> operations.RemoveOrganizationMembershipResponse:
        r"""Removes membership in a given org from a user, using the user's email address.
        Removes membership in a given org from a user, using the user's email address.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.RemoveOrganizationMembershipRequest, base_url, '/v0/organizations/{org_id}/membership', request)
        headers = {}
        query_params = utils.get_query_params(operations.RemoveOrganizationMembershipRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('DELETE', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RemoveOrganizationMembershipResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[dict[str, Any]])
                res.void = out

        return res

    
    def set_default_membership(self, request: shared.SetDefaultMembershipRequest, security: operations.SetDefaultMembershipSecurity) -> operations.SetDefaultMembershipResponse:
        r"""Sets the organization that should be used when logging a user in
        Sets the organization that should be used when logging a user in
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v0/membership/default'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SetDefaultMembershipResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Response])
                res.response = out

        return res

    
    def update_membership_by_email(self, request: shared.UpdateMembershipRequest, security: operations.UpdateMembershipByEmailSecurity) -> operations.UpdateMembershipByEmailResponse:
        r"""Updates the role in an membership
        Updates the role in an membership, given the organization and the user's email address.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v0/membership'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateMembershipByEmailResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.MembershipMetadata])
                res.membership_metadata = out

        return res

    
    def update_organization_membership(self, request: operations.UpdateOrganizationMembershipRequest, security: operations.UpdateOrganizationMembershipSecurity) -> operations.UpdateOrganizationMembershipResponse:
        r"""Updates the role in an membership
        Updates the role in an membership, given the organization and the user's email address.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateOrganizationMembershipRequest, base_url, '/v0/organizations/{org_id}/membership', request)
        headers = {}
        query_params = utils.get_query_params(operations.UpdateOrganizationMembershipRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PUT', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateOrganizationMembershipResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.MembershipMetadata])
                res.membership_metadata = out

        return res

    