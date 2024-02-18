import unittest
import os
from pdf_analyzer.api.visualize.links_search import LinksSearch
from pdf_analyzer.config_load import load_config

TEST_DIR = "tests/api_test/visualize_test"

import matplotlib
class links_search_test(unittest.TestCase):
    
    

    def setUp(self):
        self.load_configs()
        self.build_api()
        matplotlib.use('Agg')
        
    def test_setUp(self):
        self.assertIsNotNone(self.server_config)
        self.assertIsNotNone(self.api)
        self.assertIsNotNone(self.result)
        
    def test_len(self):
        self.assertEqual(self.result.get_len(),2)
    
    def test_print_reports(self):
        try:
           self.result.print_all_reports()
        except Exception as e:
            self.fail("Fail to print result"+str(e))

   
    def load_configs(self):
        try:
            self.server_config = load_config(os.path.join(TEST_DIR,"test_configs/grobid-server-config.yaml"))
            self.api = load_config(os.path.join(TEST_DIR,"test_configs/list_links-config.yaml"))
        except Exception:
            self.fail("configs loading raise a Exception")


    def build_api(self):
        try:
            self.result = LinksSearch(self.api,self.server_config)
        except Exception as e:
            self.fail("builder raise a Exception"+str(e))
        



if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()