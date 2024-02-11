from util.uploaders.file_uploader import FileUploader
from util.api.grobid_client_python.grobid_client.grobid_client import GrobidClient
from util.logger import logging
from bs4 import BeautifulSoup
from omegaconf import DictConfig
from wordcloud import WordCloud as WC
import matplotlib.pyplot as plt

import os




class BaseAPI():
    
    """_summary_ general class for functions that use grobid
    """
    def __init__(self,api_config:DictConfig,server_config:DictConfig):
        
   
        try:
            url = server_config.url.protocol+"://"+server_config.url.api_domain+":"+str(server_config.url.port)
            
            self.api_config = api_config
            
            full_path = os.path.abspath(self.api_config.data.data_dir)
            file_uploader_original = FileUploader(full_path)
            self.original_files_names = file_uploader_original.get_all_files_with_format(self.api_config.data.format,self.api_config.data.recursive)
            
            
            api = GrobidClient(grobid_server=url)
            api.process(self.api_config.grobid.operation_key,self.api_config.data.data_dir,output=self.api_config.grobid.cache_dir,force=not self.api_config.grobid.cache)
            logging.info("All files have been process by the api")
            
            full_path = os.path.abspath(self.api_config.grobid.cache_dir)
            file_uploader = FileUploader(full_path)
            files_names = file_uploader.get_all_files_with_format(self.api_config.grobid.format,self.api_config.grobid.recursive)
            if len(files_names)==0:
                messege="No files found at "+full_path+" with format "+self.api_config.grobid.format
                logging.warning(messege)
            
            self.proccesed_files = list(map(lambda file_path: self.process_file(file_path), files_names))
        
        except Exception as e:
            logging.error("Error with BaseAPI creation :"+str(e))
            raise ValueError(e)
        
        
    
    
    def process_file(self,file_path):
        xml_file = open(file_path,"r")
        soup = BeautifulSoup(xml_file,"xml")
        xml_file.close()

        return soup
    
    
    def extract_file_name(self,file_path):
        return os.path.basename(file_path).split(self.api_config.grobid.format)[0]