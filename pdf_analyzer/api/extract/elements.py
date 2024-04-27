from pdf_analyzer.uploaders.file_uploader import FileUploader
from grobid_client.grobid_client import GrobidClient
from pdf_analyzer.api.API import BaseAPI
from pdf_analyzer.logger import logging
from bs4 import BeautifulSoup
from omegaconf import DictConfig





def find_part(soup:BeautifulSoup,dir:str):
        partes = dir.split('.')

        actual = soup
        for parte in partes:
            
            actual = actual.find(parte)        
            if actual is None:
                break

        return actual
    
    
def extract_element_soup(soup:BeautifulSoup,dir:str,element_find:str,type=None):
    result_dict = dict()
    if dir is not None :
        soup = find_part(soup,dir)
        if soup ==None:
            return result_dict
    if element_find==None:
        return soup
    elements_found = soup.find_all(element_find,type=type)
    
    return elements_found



class extract_elements(BaseAPI):
    
    """_summary_ WordCloud when initialise creates word clouds from the pdfs
        it will use the config file for the differente behaviours  
    """
    def __init__(self,api_config:DictConfig,server_config:DictConfig):
        try:
            self.config = api_config
            super().__init__(api_config,server_config)
            self.elements =self.proccesed_files
        except Exception as e:
            logging.error("Error with WordCloud creation :"+str(e))
            raise ValueError(e)

    #teiHeader.fileDesc.sourceDesc.biblStruct.analytic
    
    
    
    
    
    def process_file(self,file_path:str):
        result_dict = dict()
        file_name = self.extract_file_name(file_path)
        soup = super().process_file(file_path)
        
        found_elements = extract_element_soup(soup,self.config.extract.dir,self.config.extract.element,self.config.extract.type)
        
        result_dict["file_name"] = file_name
        result_dict["elements"] =found_elements
        
        logging.info("All elements of of the xml_file "+file_name +" have been extracted")
        
        return result_dict

    def get_len(self):
        return len(self.elements)
    
    
    def print_elements(self):
        try:
            for file in self.elements:
                print("Showing elements "+self.config.extract.element+" in paper "+file["file_name"]+"\n\n")
                for element in file["elements"]:
                    print(element)
                    print("\n")
                print("\n\n\n\n")
        except Exception as e:
            logging.error("Elements could not been shown: ",str(e))
            
            
   
            

            
    