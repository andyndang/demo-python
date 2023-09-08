"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .account import Account
from .admin import Admin
from .apikey import APIKey
from .databricks import Databricks
from .dataset_metadata import DatasetMetadata
from .datasetprofile import DatasetProfile
from .debugevents import DebugEvents
from .feature_weights import FeatureWeights
from .featureflags import FeatureFlags
from .internal import Internal
from .log import Log
from .membership import Membership
from .models_ import Models
from .monitor import Monitor
from .notification_settings import NotificationSettings
from .organizations import Organizations
from .payment import Payment
from .provision import Provision
from .schema import Schema
from .sdkconfiguration import SDKConfiguration
from .search import Search
from .sessions import Sessions
from .user import User
from songbird import utils

class Songbird:
    r"""WhyLabs Songbird: WhyLabs API that enables end-to-end AI observability"""
    account: Account
    admin: Admin
    api_key: APIKey
    databricks: Databricks
    dataset_metadata: DatasetMetadata
    dataset_profile: DatasetProfile
    debug_events: DebugEvents
    feature_weights: FeatureWeights
    feature_flags: FeatureFlags
    internal: Internal
    log: Log
    membership: Membership
    models: Models
    monitor: Monitor
    notification_settings: NotificationSettings
    organizations: Organizations
    payment: Payment
    provision: Provision
    schema: Schema
    search: Search
    sessions: Sessions
    user: User

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        security_client = client
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security_client, server_url, server_idx, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.account = Account(self.sdk_configuration)
        self.admin = Admin(self.sdk_configuration)
        self.api_key = APIKey(self.sdk_configuration)
        self.databricks = Databricks(self.sdk_configuration)
        self.dataset_metadata = DatasetMetadata(self.sdk_configuration)
        self.dataset_profile = DatasetProfile(self.sdk_configuration)
        self.debug_events = DebugEvents(self.sdk_configuration)
        self.feature_weights = FeatureWeights(self.sdk_configuration)
        self.feature_flags = FeatureFlags(self.sdk_configuration)
        self.internal = Internal(self.sdk_configuration)
        self.log = Log(self.sdk_configuration)
        self.membership = Membership(self.sdk_configuration)
        self.models = Models(self.sdk_configuration)
        self.monitor = Monitor(self.sdk_configuration)
        self.notification_settings = NotificationSettings(self.sdk_configuration)
        self.organizations = Organizations(self.sdk_configuration)
        self.payment = Payment(self.sdk_configuration)
        self.provision = Provision(self.sdk_configuration)
        self.schema = Schema(self.sdk_configuration)
        self.search = Search(self.sdk_configuration)
        self.sessions = Sessions(self.sdk_configuration)
        self.user = User(self.sdk_configuration)
    