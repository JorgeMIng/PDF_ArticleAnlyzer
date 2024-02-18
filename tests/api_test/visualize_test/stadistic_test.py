import unittest
import os
from pdf_analyzer.api.visualize.stadistic import CountAtritubte
from pdf_analyzer.config_load import load_config

TEST_DIR = "tests/api_test/visualize_test"

import matplotlib
class stadistic_test(unittest.TestCase):
    
    

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
    
    def test_basic_funcs(self):
        list_result = self.result.list_stat("figure")
        if (list_result[0] != 8 or list_result[1]!=17 ) and ( list_result[1] != 8 or list_result[0]!=17):
            self.fail("Incorrect list_result expected "+str([17,8])+" or "+str([8,17])+" recived "+str(list_result))
        self.assertEqual(['figure'],self.result.get_stats_names())

    def test_complex(self):
        try:
            self.result.download_plots()
            self.result.show_plots()
        except Exception:
            self.fail("Fail to download and show plots")
   
    def load_configs(self):
        try:
            self.server_config = load_config(os.path.join(TEST_DIR,"test_configs/grobid-server-config.yaml"))
            self.api = load_config(os.path.join(TEST_DIR,"test_configs/count-config.yaml"))
        except Exception:
            self.fail("configs loading raise a Exception")


    def build_api(self):
        try:
            self.result = CountAtritubte(self.api,self.server_config)
        except Exception as e:
            self.fail("builder raise a Exception"+str(e))
        



if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()