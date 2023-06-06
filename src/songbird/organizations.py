"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from songbird import utils
from songbird.models import operations, shared
from typing import Optional

class Organizations:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create_organization(self, request: operations.CreateOrganizationRequest, security: operations.CreateOrganizationSecurity) -> operations.CreateOrganizationResponse:
        r"""Create an organization
        Create an organization
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v0/organizations'
        headers = {}
        query_params = utils.get_query_params(operations.CreateOrganizationRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('POST', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateOrganizationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.OrganizationSummary])
                res.organization_summary = out

        return res

    
    def delete_organization(self, request: operations.DeleteOrganizationRequest, security: operations.DeleteOrganizationSecurity) -> operations.DeleteOrganizationResponse:
        r"""Delete an org
        Delete an org
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteOrganizationRequest, base_url, '/v0/organizations/{org_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteOrganizationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Response])
                res.response = out

        return res

    
    def get_aws_marketplace_metadata(self, request: operations.GetAWSMarketplaceMetadataRequest, security: operations.GetAWSMarketplaceMetadataSecurity) -> operations.GetAWSMarketplaceMetadataResponse:
        r"""Get marketplace metadata for an org if any exists.
        Get marketplace metadata for an org if any exists.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAWSMarketplaceMetadataRequest, base_url, '/v0/organizations/{org_id}/marketplace-metadata/', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAWSMarketplaceMetadataResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetMarketplaceMetadataResponse])
                res.get_marketplace_metadata_response = out

        return res

    
    def get_organization(self, request: operations.GetOrganizationRequest, security: operations.GetOrganizationSecurity) -> operations.GetOrganizationResponse:
        r"""Get the metadata about an organization.
        Returns various metadata about an organization
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetOrganizationRequest, base_url, '/v0/organizations/{org_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetOrganizationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.OrganizationMetadata])
                res.organization_metadata = out

        return res

    
    def list_organizations(self, security: operations.ListOrganizationsSecurity) -> operations.ListOrganizationsResponse:
        r"""Get a list of all of the organization ids.
        Get a list of all of the organization ids.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v0/organizations'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListOrganizationsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ListOrganizationsResponse])
                res.list_organizations_response = out

        return res

    
    def partially_update_org(self, request: operations.PartiallyUpdateOrgRequest, security: operations.PartiallyUpdateOrgSecurity) -> operations.PartiallyUpdateOrgResponse:
        r"""Update some fields of an organization to non-null values
        Update some fields of an organization to non-null values, leaving all other existing values the same
        
        Deprecated: this method will be removed in a future release, please migrate away from it as soon as possible
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v0/organizations/partial/'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.PartiallyUpdateOrgRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PartiallyUpdateOrgResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.OrganizationSummary])
                res.organization_summary = out

        return res

    
    def partially_update_organization(self, request: operations.PartiallyUpdateOrganizationRequest, security: operations.PartiallyUpdateOrganizationSecurity) -> operations.PartiallyUpdateOrganizationResponse:
        r"""Update some fields of an organization to non-null values
        Update some fields of an organization to non-null values, leaving all other existing values the same
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PartiallyUpdateOrganizationRequest, base_url, '/v0/organizations/partial/{org_id}', request)
        headers = {}
        query_params = utils.get_query_params(operations.PartiallyUpdateOrganizationRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PUT', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PartiallyUpdateOrganizationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.OrganizationSummary])
                res.organization_summary = out

        return res

    
    def update_org(self, request: operations.UpdateOrgRequest, security: operations.UpdateOrgSecurity) -> operations.UpdateOrgResponse:
        r"""Update an existing organization
        Update all fields of an existing organization
        
        Deprecated: this method will be removed in a future release, please migrate away from it as soon as possible
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v0/organizations'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.UpdateOrgRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateOrgResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.OrganizationSummary])
                res.organization_summary = out

        return res

    
    def update_organization(self, request: operations.UpdateOrganizationRequest, security: operations.UpdateOrganizationSecurity) -> operations.UpdateOrganizationResponse:
        r"""Update an existing organization
        Update all fields of an existing organization
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateOrganizationRequest, base_url, '/v0/organizations/{org_id}', request)
        headers = {}
        query_params = utils.get_query_params(operations.UpdateOrganizationRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PUT', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateOrganizationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.OrganizationSummary])
                res.organization_summary = out

        return res

    