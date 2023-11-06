"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from songbird import utils
from songbird.models import errors, operations, shared
from typing import Optional

class Sessions:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def batch_create_reference_profile_upload(self, request: operations.BatchCreateReferenceProfileUploadRequest) -> operations.BatchCreateReferenceProfileUploadResponse:
        r"""Create multiple reference profile uploads for a given session.
        Create multiple reference profile uploads for a given session.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.BatchCreateReferenceProfileUploadRequest, base_url, '/v0/sessions/{session_id}/references', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "batch_log_reference_request", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.BatchCreateReferenceProfileUploadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.BatchLogSessionReferenceResponse])
                res.batch_log_session_reference_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def claim_guest_session(self, request: operations.ClaimGuestSessionRequest) -> operations.ClaimGuestSessionResponse:
        r"""Claim a guest session, copying its model data into another org and expiring the session.
        Claim a guest session, copying its model data into another org and expiring the session.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ClaimGuestSessionRequest, base_url, '/v0/sessions/{session_id}/claim', request)
        headers = {}
        query_params = utils.get_query_params(operations.ClaimGuestSessionRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ClaimGuestSessionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Void])
                res.void = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def create_dataset_profile_upload(self, request: operations.CreateDatasetProfileUploadRequest) -> operations.CreateDatasetProfileUploadResponse:
        r"""Create an upload for a given session.
        Create an upload for a given session.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreateDatasetProfileUploadRequest, base_url, '/v0/sessions/{session_id}/upload', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "log_async_request", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateDatasetProfileUploadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateDatasetProfileUploadResponse])
                res.create_dataset_profile_upload_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def create_reference_profile_upload(self, request: operations.CreateReferenceProfileUploadRequest) -> operations.CreateReferenceProfileUploadResponse:
        r"""Create a reference profile upload for a given session.
        Create a reference profile upload for a given session.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreateReferenceProfileUploadRequest, base_url, '/v0/sessions/{session_id}/reference', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "log_reference_request", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateReferenceProfileUploadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.LogSessionReferenceResponse])
                res.log_session_reference_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def create_session(self, request: shared.CreateSessionRequest) -> operations.CreateSessionResponse:
        r"""Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.
        Create a new session that can be used to upload dataset profiles from whylogs for display in whylabs.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v0/sessions'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateSessionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.CreateSessionResponse])
                res.create_session_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_session(self, request: operations.GetSessionRequest) -> operations.GetSessionResponse:
        r"""Get information about a session.
        Get information about a session.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetSessionRequest, base_url, '/v0/sessions/{session_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetSessionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetSessionResponse])
                res.get_session_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_session_profile_observatory_link(self, request: operations.GetSessionProfileObservatoryLinkRequest) -> operations.GetSessionProfileObservatoryLinkResponse:
        r"""Get observatory links for profiles in a given session. A max of 3 profiles can be viewed a a time.
        Get observatory links for profiles in a given session. A max of 3 profiles can be viewed a a time.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetSessionProfileObservatoryLinkRequest, base_url, '/v0/sessions/observatory-link/{session_id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "get_profile_observatory_link_request", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetSessionProfileObservatoryLinkResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetProfileObservatoryLinkResponse])
                res.get_profile_observatory_link_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    