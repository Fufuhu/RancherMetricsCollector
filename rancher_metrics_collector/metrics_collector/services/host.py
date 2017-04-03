import json
import requests
from logging import getLogger, StreamHandler, DEBUG
from rancher_metrics_collector import settings


class RancherHostClient():

    def __init__(self, api_keys, target_host):
        self.api_keys = api_keys
        self.rancher_host = target_host
        self.target_host = \
            'http://' + self.api_keys['access_key'] + \
            ':' + self.api_keys['secret_key'] + '@' + self.rancher_host
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        self.logger = getLogger(__name__)
        self.logger.addHandler(handler)


  


    def get_project_list(self):
        """
        Get the list of environments.
        """
        self.logger.setLevel(DEBUG)
        request_path = '/v2-beta/projects/'
        target_path = self.target_host + request_path
        self.logger.info('TARGET_FULL_PATH:' + target_path)

        response = requests.get(target_path)
        response_body = response.json()

        data = response_body.get('data')
        self.logger.info("DATA_LENGTH:" + str(len(data)))

        environments = []
        for elem in data:
            environment = {
                "id": elem.get('id'),
                "name": elem.get('name'),
            }
            self.logger.info('ID:' + elem.get('id'))
            self.logger.info('Name:' + elem.get('name'))
            environments = environments + [environment]

        # print("LENGTH:" + int(len(data)))
        return environments


    def get_host_lists(self, environment):
        """
        Get the list of hosts.
        """
        request_path = '/v2-beta/projects/' + environment + '/hosts/'

        self.logger.setLevel(DEBUG)

        target_path = self.target_host + request_path
        self.logger.info('TARGET_PATH:' + target_path)
        response = requests.get(target_path)
        response_body = response.json()

        data = response_body.get('data')
        self.logger.info("DATA_LENGTH:" + str(len(data)))

        hosts = []
        for elem in data:
            host = {
                "id": elem.get('id'),
                "hostname": elem.get('hostname'),
            }
            self.logger.info('id:' + host.get('id', 'NoID'))
            self.logger.info('hostname:' + host.get('hostname', 'NoHostName'))
            hosts = hosts + [host]

        return hosts
