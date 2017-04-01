from metrics_collector.services.host import RancherHostClient
from rancher_metrics_collector import settings
import unittest



class TestRancherHostClient(unittest.TestCase):

    def test_get_project_list(self):
        api_keys = settings.API_KEYS
        target_host = settings.RANCHER_HOST

        client = RancherHostClient(api_keys, target_host)
        client.get_project_list()
