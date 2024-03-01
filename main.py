# Main script that launches can launch all scripts
from pdf_analyzer.logger import logging
import argparse
import os

from pdf_analyzer import api
from pdf_analyzer.config_load import load_config


from omegaconf import OmegaConf
import matplotlib.pyplot as plt



def word_cloud_execute(api_config,server_config):
    result = api.visualize.word_cloud.WordCloud(api_config,server_config)
    if result.get_len()>0:
        result.show_all_cloud()

def stadistic_execute(api_config,server_config):

    result = api.visualize.stadistic.CountAtritubte(api_config,server_config)
    if result.get_len()>0:
        print(len(result))
        result.download_plots()
        result.show_plots()

def links_execute(api_config,server_config):
    result = api.visualize.links_search.LinksSearch(api_config,server_config)
    if result.get_len()>0:
        result.print_all_reports()
    

    
valid_services = ["visualize.word_cloud","visualize.links_search","visualize.stadistic"]

services = [
        word_cloud_execute,
        links_execute,
        stadistic_execute
        
]

service_map = dict(zip(valid_services, services))




def parse_arguments():
    parser = argparse.ArgumentParser(description="PDF Analyzer")

    parser.add_argument(
        "service",
        help="one of " + str(valid_services),
    )
    
    parser.add_argument(
        "--protocol",
        default="http",
        help="internet protocol, default http ",
    )
    
    parser.add_argument(
        "--domain",
        default="localhost",
        help="domain to use, default localhost ",
    )
    
    parser.add_argument(
        "--port",
        default="8070",
        help="port to use, default 8070 ",
    )
    
    return parser



if __name__ == "__main__":
    

    parser = parse_arguments()
    args = parser.parse_args()
    
    
    
    if args.service is None or args.service not in valid_services:
        logging.error("Missing or invalid service, must be one of"+ str(valid_services))
        exit(1)
    
    api_config_dir = args.service.replace('.', '/')
    api_config = load_config(os.path.join("base_config/api",api_config_dir,"api-config.yaml"))
    server_config = load_config("base_config/api/grobid-server-config.yaml")
    
    server_config.url.port = args.port
    server_config.url.protocol = args.protocol
    server_config.url.api_domain = args.domain
    
    
    try:
        service_map[args.service](api_config,server_config)
    except Exception as e:
        logging.error(e)
        exit(1)
    
    

    