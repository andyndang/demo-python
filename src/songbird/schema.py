"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from songbird import utils
from songbird.models import operations

class Schema:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def get_monitor_config_schema(self, request: operations.GetMonitorConfigSchemaRequest, security: operations.GetMonitorConfigSchemaSecurity) -> operations.GetMonitorConfigSchemaResponse:
        r"""Get the current supported schema of the monitor configuration
        Get the current supported schema of the  monitor configuration
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetMonitorConfigSchemaRequest, base_url, '/v0/organizations/{org_id}/schema/monitor-config', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetMonitorConfigSchemaResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                res.get_monitor_config_schema_default_application_json_string = http_res.content

        return res

    