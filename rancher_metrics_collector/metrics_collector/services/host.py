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
        logger = getLogger(__name__)
        logger.setLevel(DEBUG)
        PATH = '/v2-beta/projects/'
        TARGET_PATH = self.target_host + PATH
        logger.info('TARGET_PATH:' + TARGET_PATH)
        r = requests.get(TARGET_PATH)
        response_body = r.json()
        logger.info("RESPONSE_BODY:" + str(response_body))
        data = response_body.get('data')
        print("\n\n\n")
        logger.info("DATA_LENGTH:" + str(len(data)))

        for elem in data:
            logger.info('ID:' + elem.get('id'))
            logger.info('Name:' + elem.get('name'))

        # print("LENGTH:" + int(len(data)))


    def get_host_lists(self):
        """
        Get the list of hosts.
        """
        PATH = '/v2-beta/projects/1a5/hosts/'
