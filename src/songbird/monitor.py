"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from songbird import utils
from songbird.models import operations, shared
from typing import Optional

class Monitor:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def delete_analyzer(self, request: operations.DeleteAnalyzerRequest, security: operations.DeleteAnalyzerSecurity) -> operations.DeleteAnalyzerResponse:
        r"""Delete the analyzer config for a given dataset.
        Delete the analyzer config for a given dataset.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteAnalyzerRequest, base_url, '/v0/organizations/{org_id}/models/{dataset_id}/monitor-config/analyzer/{analyzer_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteAnalyzerResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Response])
                res.response = out

        return res

    
    def delete_monitor(self, request: operations.DeleteMonitorRequest, security: operations.DeleteMonitorSecurity) -> operations.DeleteMonitorResponse:
        r"""Delete the monitor for a given dataset.
        Delete the monitor for a given dataset.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteMonitorRequest, base_url, '/v0/organizations/{org_id}/models/{dataset_id}/monitor-config/monitor/{monitor_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteMonitorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Response])
                res.response = out

        return res

    
    def get_analyzer(self, request: operations.GetAnalyzerRequest, security: operations.GetAnalyzerSecurity) -> operations.GetAnalyzerResponse:
        r"""Get the analyzer config for a given dataset.
        Get the analyzer config for a given dataset.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAnalyzerRequest, base_url, '/v0/organizations/{org_id}/models/{dataset_id}/monitor-config/analyzer/{analyzer_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAnalyzerResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                res.get_analyzer_default_application_json_string = http_res.content

        return res

    
    def get_monitor(self, request: operations.GetMonitorRequest, security: operations.GetMonitorSecurity) -> operations.GetMonitorResponse:
        r"""Get the monitor config for a given dataset.
        Get the monitor config for a given dataset.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetMonitorRequest, base_url, '/v0/organizations/{org_id}/models/{dataset_id}/monitor-config/monitor/{monitor_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetMonitorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                res.get_monitor_default_application_json_string = http_res.content

        return res

    
    def get_monitor_config_v3(self, request: operations.GetMonitorConfigV3Request, security: operations.GetMonitorConfigV3Security) -> operations.GetMonitorConfigV3Response:
        r"""Get the monitor config document for a given dataset.
        Get the monitor config document for a given dataset.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetMonitorConfigV3Request, base_url, '/v0/organizations/{org_id}/models/{dataset_id}/monitor-config/v3', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetMonitorConfigV3Request, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetMonitorConfigV3Response(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                res.get_monitor_config_v3_default_application_json_string = http_res.content

        return res

    
    def get_monitor_config_v3_version(self, request: operations.GetMonitorConfigV3VersionRequest, security: operations.GetMonitorConfigV3VersionSecurity) -> operations.GetMonitorConfigV3VersionResponse:
        r"""Get the monitor config document version for a given dataset.
        Get the monitor config document version for a given dataset.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetMonitorConfigV3VersionRequest, base_url, '/v0/organizations/{org_id}/models/{dataset_id}/monitor-config/v3/versions/{version_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetMonitorConfigV3VersionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                res.get_monitor_config_v3_version_default_application_json_string = http_res.content

        return res

    
    def list_monitor_config_v3_versions(self, request: operations.ListMonitorConfigV3VersionsRequest, security: operations.ListMonitorConfigV3VersionsSecurity) -> operations.ListMonitorConfigV3VersionsResponse:
        r"""List the monitor config document versions for a given dataset.
        List the monitor config document versions for a given dataset.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListMonitorConfigV3VersionsRequest, base_url, '/v0/organizations/{org_id}/models/{dataset_id}/monitor-config/v3/versions', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListMonitorConfigV3VersionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.MonitorConfigVersion]])
                res.monitor_config_versions = out

        return res

    
    def patch_monitor_config_v3(self, request: operations.PatchMonitorConfigV3Request, security: operations.PatchMonitorConfigV3Security) -> operations.PatchMonitorConfigV3Response:
        r"""Patch an updated monitor config document for a given dataset.
        Save an updated monitor config document for a given dataset.  Monitors and analyzers matching an existing ID are replaced.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PatchMonitorConfigV3Request, base_url, '/v0/organizations/{org_id}/models/{dataset_id}/monitor-config/v3', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'string')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PatchMonitorConfigV3Response(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Response])
                res.response = out

        return res

    
    def put_analyzer(self, request: operations.PutAnalyzerRequest, security: operations.PutAnalyzerSecurity) -> operations.PutAnalyzerResponse:
        r"""Save the analyzer config for a given dataset.
        Save the analyzer config for a given dataset.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PutAnalyzerRequest, base_url, '/v0/organizations/{org_id}/models/{dataset_id}/monitor-config/analyzer/{analyzer_id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'string')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutAnalyzerResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Response])
                res.response = out

        return res

    
    def put_monitor(self, request: operations.PutMonitorRequest, security: operations.PutMonitorSecurity) -> operations.PutMonitorResponse:
        r"""Save the monitor for a given dataset.
        Save the monitor for a given dataset.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PutMonitorRequest, base_url, '/v0/organizations/{org_id}/models/{dataset_id}/monitor-config/monitor/{monitor_id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'string')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutMonitorResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Response])
                res.response = out

        return res

    
    def put_monitor_config_v3(self, request: operations.PutMonitorConfigV3Request, security: operations.PutMonitorConfigV3Security) -> operations.PutMonitorConfigV3Response:
        r"""Save the monitor config document for a given dataset.
        Save the monitor config document for a given dataset.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PutMonitorConfigV3Request, base_url, '/v0/organizations/{org_id}/models/{dataset_id}/monitor-config/v3', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'string')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutMonitorConfigV3Response(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Response])
                res.response = out

        return res

    
    def put_request_monitor_run_config(self, request: operations.PutRequestMonitorRunConfigRequest, security: operations.PutRequestMonitorRunConfigSecurity) -> operations.PutRequestMonitorRunConfigResponse:
        r"""Put the RequestMonitorRun config into S3.
        Put the RequestMonitorRun config into S3.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PutRequestMonitorRunConfigRequest, base_url, '/v0/organizations/{org_id}/models/{dataset_id}/request-monitor-run', request)
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

        res = operations.PutRequestMonitorRunConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                res.put_request_monitor_run_config_default_application_json_string = http_res.content

        return res

    
    def validate_monitor_config_v3(self, request: operations.ValidateMonitorConfigV3Request, security: operations.ValidateMonitorConfigV3Security) -> operations.ValidateMonitorConfigV3Response:
        r"""Validate the monitor config document for a given dataset.
        Validate the monitor config document for a given dataset.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ValidateMonitorConfigV3Request, base_url, '/v0/organizations/{org_id}/models/{dataset_id}/monitor-config/v3/validate', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'string')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.ValidateMonitorConfigV3Request, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ValidateMonitorConfigV3Response(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Response])
                res.response = out

        return res

    