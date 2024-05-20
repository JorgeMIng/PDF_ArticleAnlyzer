
from pdf_analyzer.logger import logging
import os
import glob
from bs4 import BeautifulSoup
from grobid_client.grobid_client import GrobidClient
from typing import Callable, Dict, List, Optional, Union,IO

     

class FileUploader():
    
    
    def __init__(self,data_dir:str):
        """_summary_  Initialize file_uploader, it will use the data_dir for file searching

        Args:
            data_dir (str): _description_. folder for searching files.

        """        
        
        self.data_dir = data_dir
       
       
        
           
    def get_all_files_with_format(self,file_format:str,recursive_search=False): 
        """_summary_ get all files with the specific format from data_dir , 
        if recursive is set to True it will search all folder at the folder

        Args:
            file_format (str): _description_
            recursive_search (bool, optional): _description_. Defaults to False.

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        if  not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
                 
        if not os.path.exists(self.data_dir) or not os.path.isdir(self.data_dir):
            error_messege = "data_dir: "+self.data_dir+" is not a valid or existing directory"
            logging.error(error_messege)
            raise ValueError(error_messege)   
        pattern = os.path.join(self.data_dir, f"**/*{file_format}")
        file_paths = glob.glob(pattern, recursive=recursive_search)
        return file_paths

   
   