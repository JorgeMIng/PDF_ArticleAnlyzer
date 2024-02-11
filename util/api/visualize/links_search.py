from util.uploaders.file_uploader import FileUploader
from util.api.grobid_client_python.grobid_client.grobid_client import GrobidClient
from util.logger import logging
from bs4 import BeautifulSoup
from bs4.element import Tag
from omegaconf import DictConfig
from wordcloud import WordCloud as WC
import matplotlib.pyplot as plt
from util.api.API import BaseAPI
import os
import time
from typing import Dict

from rich.console import Console
from rich.table import Table
import re

def print_link(link:Tag):
    return str(link.text)
    

        
        



class LinksSearch(BaseAPI):
    
    """_summary_ visualize links of the articles 
    """

    def __init__(self,api_config:DictConfig,server_config:DictConfig):
        try:
            super().__init__(api_config,server_config)
            self.file_reports =self.proccesed_files
        except Exception as e:
            logging.error("Error with LinkSearch creation :"+str(e))
            raise ValueError(e)

    
    def process_file(self,file_path):
        file_name = self.extract_file_name(file_path)
        xml_file = open(file_path,"r")
        soup = BeautifulSoup(xml_file,"xml")
        xml_file.close()
        links = soup.find_all("ref")
        
        p_elments = soup.find_all("p")
        regex = r'https?://[^\s]+(?:\s[^\s]+)?'
        links_htmls=[]
        for p in p_elments:
            text_p = p.get_text()
            link_html=re.findall(regex, text_p)
            if(link_html):
                links_htmls.extend(link_html)
        
        
        
        logging.info("All links have been extracted from file "+file_name)  
        file_report = dict()
        file_report["file_name"]=file_name
        file_report["links"]=links
        file_report["html"]=links_htmls
        return file_report
    
    
    def print_all_reports(self):
        for file_link_report in self.file_reports:
            self.print_file_report(file_link_report)

    def get_len(self):
        return len(self.file_reports)
    
    
    def print_file_report(self,link_file_report):
        console = Console()

        # Crear una tabla rica
        table = Table(title="File: "+link_file_report["file_name"],style=self.api_config.list.style)
        table.add_column("Index", style=self.api_config.list.index.style, justify=self.api_config.list.index.justify)
        table.add_column("Links Refs", style=self.api_config.list.refs.style,justify=self.api_config.list.refs.justify)
        table.add_column("Links Html", style=self.api_config.list.html.style,justify=self.api_config.list.html.justify)

        # Agregar filas a la tabla
        
        
        link_len = len(link_file_report["links"])
        html_len = len(link_file_report["html"])
        biggest_len = max(link_len,html_len)
        i=1
        
        for i in range(biggest_len):
            if i<link_len-1:
                link_str = print_link(link_file_report["links"][i+1])
            else:
                link_str=""
            if i<html_len:
                html_str=str(link_file_report["html"][i])
            else:
                html_str=""
            
            table.add_row(str(i + 1), link_str,html_str)
            
        
    
        # Imprimir la tabla
        console.print(table)