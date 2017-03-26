from metrics_collector.services.host import RancherHostClient
import unittest



class TestRancherHostClient(unittest.TestCase):

    def test_get_project_list(self):
        client = RancherHostClient()
        client.get_project_list()
