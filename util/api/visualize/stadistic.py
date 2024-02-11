from util.uploaders.file_uploader import FileUploader
from util.api.grobid_client_python.grobid_client.grobid_client import GrobidClient
from util.logger import logging
from bs4 import BeautifulSoup
from omegaconf import DictConfig
from wordcloud import WordCloud as WC
import matplotlib.pyplot as plt
from util.api.API import BaseAPI
import os
import time



class CountAtritubte(BaseAPI):
    
    """_summary_ visualize counts of specific atributes 
    """

    def __init__(self,api_config:DictConfig,server_config:DictConfig):
        try:
            self.stats = api_config.count.stats if isinstance(api_config.count.stats,list) else [api_config.count.stats]
            logging.info("Stats to be count "+str(self.stats)) 
            super().__init__(api_config,server_config)
            self.stadistics =self.proccesed_files
        except Exception as e:
            logging.error("Error with Count creation :"+str(e))
            raise ValueError(e)

    
    def process_file(self,file_path):
        file_name = self.extract_file_name(file_path)
        xml_file = open(file_path,"r")
        soup = BeautifulSoup(xml_file,"xml")
        xml_file.close()
        output_dict = dict()
        for stat in self.stats:
            number = len(soup.find_all(stat))
            output_dict[stat]=number
        logging.info("All stats have been recorder from file "+file_name)  
        return output_dict
    
    
    def get_labels(self):
        return list(map(lambda file_path: self.extract_file_name(file_path),self.original_files_names) )
    
    def download_plots(self):
    
        
        abs_path = os.path.abspath(self.api_config.plot.cache_dir)
        file_dir = os.path.join(abs_path,self.api_config.grobid.operation_key)
        for stat in self.stats:
            file_path = os.path.join(file_dir,stat+self.api_config.plot.format)
        
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
                
            stat_values=self.list_stat(stat)
            self.draw_plot(self.get_labels(),stat_values) 
            plt.savefig(file_path)
            
            logging.info("Plot about "+stat+" is store at "+file_path)
        plt.close()
    
    def show_plots(self):
        
        for stat in self.stats:
            #os.path.basename(file_path).split(self.api_config.grobid.format)[0]
            stat_values=self.list_stat(stat)
            self.draw_plot(self.get_labels(),stat_values)
        plt.show()
        plt.close()
        
    def draw_plot(self,labels,stats): 
        print(labels)
        print(stats) 
        plt.bar(x=labels,height=stats,width=self.api_config.plot.width,align=self.api_config.plot.align,color=self.api_config.plot.color,edgecolor=self.api_config.plot.edgecolor)
    
    def list_stat(self,stat:str):
        return list(map(lambda dict: dict.get(stat), self.stadistics))
    
    def get_stats_names(self):
        return self.stats

    def get_len(self):
        return len(self.stadistics)
    
    
   