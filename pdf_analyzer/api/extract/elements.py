from pdf_analyzer.uploaders.file_uploader import FileUploader
from pdf_analyzer.api.grobid_client_python.grobid_client.grobid_client import GrobidClient
from pdf_analyzer.api.API import BaseAPI
from pdf_analyzer.logger import logging
from bs4 import BeautifulSoup
from omegaconf import DictConfig
from wordcloud import WordCloud as WC
import matplotlib.pyplot as plt

import os
import time



class extract_element(BaseAPI):
    
    """_summary_ WordCloud when initialise creates word clouds from the pdfs
        it will use the config file for the differente behaviours  
    """
    def __init__(self,api_config:DictConfig,server_config:DictConfig):
        try:
            self.dir_start = api_config.extract.dir
            self.element_find = api_config.extract.element
            self.config = api_config
            super().__init__(api_config,server_config)
            self.elements =self.proccesed_files
        except Exception as e:
            logging.error("Error with WordCloud creation :"+str(e))
            raise ValueError(e)

    #teiHeader.fileDesc.sourceDesc.biblStruct.analytic
    
    def find_part(self,soup,dir):
        partes = dir.split('.')

        actual = soup
        for parte in partes:
            
            actual = actual.find(parte)        
            if actual is None:
                break

        return actual
    
    
    
    def process_file(self,file_path):
        result_dict = dict()
        file_name = self.extract_file_name(file_path)
        soup = super().process_file(file_path)
        
        if self.dir_start is not None:
            soup = self.find_part(soup,self.dir_start)
            if soup ==None:
                return result_dict
        if self.element_find==None:
            return result_dict
        elements_found = soup.find_all(self.element_find,type=self.config.extract.type)
        result_dict["file_name"] = file_name
        result_dict["elements"] =elements_found
        
        logging.info("All elements of of the xml_file "+file_name +" have been extracted")
        
        return result_dict

    def get_len(self):
        return len(self.elements)
    
    
    def print_elements(self):
        try:
            for file in self.elements:
                print("Showing elements "+self.element_find+" in paper "+file["file_name"]+"\n\n")
                for element in file["elements"]:
                    print(element)
                    print("\n")
                print("\n\n\n\n")
        except Exception as e:
            logging.error("Elements could not been shown: ",str(e))
            
            
   
            

            
    