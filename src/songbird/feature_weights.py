"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from songbird import utils
from songbird.models import operations, shared
from typing import Optional

class FeatureWeights:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def get_column_weights(self, request: operations.GetColumnWeightsRequest, security: operations.GetColumnWeightsSecurity) -> operations.GetColumnWeightsResponse:
        r"""Get column weights for the specified dataset
        Get column weights for the specified dataset
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetColumnWeightsRequest, base_url, '/v0/organizations/{org_id}/dataset/{dataset_id}/weights', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetColumnWeightsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.EntityWeightRecord])
                res.entity_weight_record = out

        return res

    
    def put_column_weights(self, request: operations.PutColumnWeightsRequest, security: operations.PutColumnWeightsSecurity) -> operations.PutColumnWeightsResponse:
        r"""Put column weights for the specified dataset
        Put column weights for the specified dataset
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PutColumnWeightsRequest, base_url, '/v0/organizations/{org_id}/dataset/{dataset_id}/weights', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'string')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = utils.configure_security_client(self.sdk_configuration.client, security)
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutColumnWeightsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if True:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Response])
                res.response = out

        return res

    