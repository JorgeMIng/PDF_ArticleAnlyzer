import unittest
import os
from pdf_analyzer.api.visualize.word_cloud import WordCloud
from pdf_analyzer.config_load import load_config

TEST_DIR = "tests/api_test/visualize_test"

import matplotlib
class word_cloud(unittest.TestCase):
    
    

    def setUp(self):
        self.load_configs()
        self.build_api()
        matplotlib.use('Agg')
        
    def test_setUp(self):
        self.assertIsNotNone(self.server_config)
        self.assertIsNotNone(self.api)
        self.assertIsNotNone(self.result)
        
    def test_len(self):
        self.assertEqual(self.result.get_len(),10)

    def test_complex(self):
        try:
            self.result.show_all_cloud()
        except Exception:
            self.fail("Fail to download and show plots")
   
    def load_configs(self):
        try:
            self.server_config = load_config(os.path.join(TEST_DIR,"test_configs/grobid-server-config.yaml"))
            self.api = load_config(os.path.join(TEST_DIR,"test_configs/word-cloud-config.yaml"))
        except Exception:
            self.fail("configs loading raise a Exception")


    def build_api(self):
        try:
            self.result = WordCloud(self.api,self.server_config)
        except Exception as e:
            self.fail("builder raise a Exception"+str(e))
        



if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()