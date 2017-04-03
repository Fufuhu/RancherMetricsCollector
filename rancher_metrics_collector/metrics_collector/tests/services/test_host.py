from metrics_collector.services.host import RancherHostClient
from rancher_metrics_collector import settings
import unittest



class TestRancherHostClient(unittest.TestCase):

    def test_get_project_list(self):
        """
        Getting project list correctly.
        """
        api_keys = settings.API_KEYS
        target_host = settings.RANCHER_HOST

        client = RancherHostClient(api_keys, target_host)
        environments = client.get_project_list()

        self.assertIsNotNone(environments)
        self.assertEqual(len(environments), 2)


    def test_get_host_list(self):
        """
        Getting host list correctly.
        """
        api_keys = settings.API_KEYS
        target_host = settings.RANCHER_HOST

        client = RancherHostClient(api_keys, target_host)

        environment = '1a5'
        hosts = client.get_host_lists(environment)
        self.assertIsNotNone(hosts)
        self.assertGreaterEqual(len(hosts), 0)
