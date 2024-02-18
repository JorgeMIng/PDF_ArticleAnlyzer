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



class WordCloud(BaseAPI):
    
    """_summary_ WordCloud when initialise creates word clouds from the pdfs
        it will use the config file for the differente behaviours  
    """
    def __init__(self,api_config:DictConfig,server_config:DictConfig):
        try:
            super().__init__(api_config,server_config)
            self.word_clouds =self.proccesed_files
        except Exception as e:
            logging.error("Error with WordCloud creation :"+str(e))
            raise ValueError(e)

    
    def process_file(self,file_path):
        file_name = self.extract_file_name(file_path)
        xml_file = open(file_path,"r")
        soup = BeautifulSoup(xml_file,"xml")
        xml_file.close()
        
        abstract_blocks = soup.find_all('abstract')
        all_p_string=""
        for abstract in abstract_blocks:
            p_elements = abstract.find_all("p")
            for p in p_elements:
                all_p_string=all_p_string+" "+p.text
        logging.info("All paragraphs of the abtract of the xml_file "+file_name +" are joined")
        wordcloud = WC(width=self.api_config.image.width,height=self.api_config.image.height,background_color=self.api_config.image.background).generate(all_p_string)   
        logging.info("WordCloud of the file "+file_name +" is created")
        
        if self.api_config.image.cache:
            abs_path = os.path.abspath(self.api_config.image.cache_dir)
            file_dir = os.path.join(abs_path,self.api_config.grobid.operation_key)
            
            file_path = os.path.join(file_dir,file_name+self.api_config.image.format)
            
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
            wordcloud.to_file(file_path)
            logging.info("WordCloud png is store at "+file_path)
        return wordcloud

    def get_len(self):
        return len(self.word_clouds)
    
    
    def plot_cloud(self,cloud):
        try:
            plt.imshow(cloud, interpolation='bilinear')
            plt.axis("off")
            plt.show()
        except Exception as e:
            logging.error("Cloud image could not be shown: ",str(e))
            
            
    def show_all_cloud(self):
        
        for index,cloud in enumerate(self.word_clouds):
            try:
                self.plot_cloud(cloud)
            except Exception as e:
                logging.error("Cloud with index "+index,"could not be shown: ",str(e))
            

            
    