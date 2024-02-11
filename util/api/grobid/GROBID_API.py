import requests
from util.logger import logging


post_keys=["referenceAnnotations","processReferences","processHeaderNames","processHeaderDocument",
               "processFulltextDocument","processFulltextAssetDocument","processDate",
               "processCitationPatentTXT","processCitationPatentST36","processCitationPatentPDF"
               "processCitationNames","processCitation","processAffiliations","citationPatentAnnotations","annotatePDF"]

from omegaconf import DictConfig, OmegaConf

class GrobidAPI():
    
    def list_post_operations(self):
        """_summary_

        List of all posible post operations of the GrobidAPI as a list
        
        Returns: 
            _list[str]_: List of string with the operations 
        """
        return post_keys

    def __init__(self,server_config: DictConfig):
        """_summary_

        Starts a API client asociated with the url {protocol}://{api_domain}:port
        Args:
        server_config (DictConfig): configuration file from omegaconf
        
        Example
        
        config directorie:
        
        config
            \--api
               \-server_config.yaml
               \-api.yaml
            \--data
                \-data.yaml
                
        config_name examples
         api/server_config.yaml
         api/api.yaml
         data/data.yaml

        Returns:
        GrobidAPI object

    """
       
        
        try:
            self.protocol=server_config.url.protocol
            self.api_domain = server_config.url.api_domain
            self.port=str(server_config.url.port)
        except Exception:
            error_messege= "Error key are not correctly set at config_file, there must be [url.protocol, url.api_domain, url.port] set"
            logging.error(error_messege)
            raise ValueError(error_messege)
        self.api_url=self.protocol+"://"+self.api_domain+":"+self.port

    def send_post_request(self,operation_key:str,f) :
        """Executes a POST operation to the GrobidAPI

                Parameters:
                operation_key (str): identifier for the operation to be done; use list_post_operation for the list of avabaile operations
                f (file): files or file to send with the POST request
                
                Returns:
                Response from the GrobidAPI

            """ 
     
        full_url =self.api_url+"/api/"+operation_key
        if operation_key not in post_keys:
            error_messege = "Operation "+operation_key+"is not a valid operation"
            logging.error(error_messege)
            raise ValueError(error_messege)
                  
        try:
            input_f = {
            "input": f
            }
            logging.info(full_url)
            response = requests.post(url=full_url, files=input_f)
            
            
            if response.status_code == 200:
                logging.info("Reponse OK from "+full_url)
                return response
        except Exception as e:
            messege="ERROR:Grobid is not online at "+full_url+" "+str(e)
            logging.error(messege)
            raise ValueError(messege)

