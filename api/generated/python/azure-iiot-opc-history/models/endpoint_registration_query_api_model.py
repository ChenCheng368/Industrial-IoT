# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 2.3.33.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EndpointRegistrationQueryApiModel(Model):
    """Endpoint query.

    :param url: Endoint url for direct server access
    :type url: str
    :param user_authentication: Type of credential selected for
     authentication. Possible values include: 'None', 'UserName',
     'X509Certificate', 'JwtToken'
    :type user_authentication: str or
     ~azure-iiot-opc-history.models.CredentialType
    :param certificate: Certificate of the endpoint
    :type certificate: bytearray
    :param security_mode: Security Mode. Possible values include: 'Best',
     'Sign', 'SignAndEncrypt', 'None'
    :type security_mode: str or ~azure-iiot-opc-history.models.SecurityMode
    :param security_policy: Security policy uri
    :type security_policy: str
    :param activated: Whether the endpoint was activated
    :type activated: bool
    :param connected: Whether the endpoint is connected on supervisor.
    :type connected: bool
    :param endpoint_state: The last state of the the activated endpoint.
     Possible values include: 'Connecting', 'NotReachable', 'Busy', 'NoTrust',
     'CertificateInvalid', 'Ready', 'Error'
    :type endpoint_state: str or
     ~azure-iiot-opc-history.models.EndpointConnectivityState
    :param include_not_seen_since: Whether to include endpoints that were soft
     deleted
    :type include_not_seen_since: bool
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
        'user_authentication': {'key': 'userAuthentication', 'type': 'CredentialType'},
        'certificate': {'key': 'certificate', 'type': 'bytearray'},
        'security_mode': {'key': 'securityMode', 'type': 'SecurityMode'},
        'security_policy': {'key': 'securityPolicy', 'type': 'str'},
        'activated': {'key': 'activated', 'type': 'bool'},
        'connected': {'key': 'connected', 'type': 'bool'},
        'endpoint_state': {'key': 'endpointState', 'type': 'EndpointConnectivityState'},
        'include_not_seen_since': {'key': 'includeNotSeenSince', 'type': 'bool'},
    }

    def __init__(self, url=None, user_authentication=None, certificate=None, security_mode=None, security_policy=None, activated=None, connected=None, endpoint_state=None, include_not_seen_since=None):
        super(EndpointRegistrationQueryApiModel, self).__init__()
        self.url = url
        self.user_authentication = user_authentication
        self.certificate = certificate
        self.security_mode = security_mode
        self.security_policy = security_policy
        self.activated = activated
        self.connected = connected
        self.endpoint_state = endpoint_state
        self.include_not_seen_since = include_not_seen_since
