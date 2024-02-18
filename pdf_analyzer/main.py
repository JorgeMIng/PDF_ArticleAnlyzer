# Main script that launches can launch all scripts
import argparse
import os

from pdf_analyzer import api
from pdf_analyzer.config_load import load_config
from pdf_analyzer.logger import logging

from omegaconf import OmegaConf
import matplotlib.pyplot as plt



def word_cloud_execute(api_config,server_config):
    from api.visualize.word_cloud import WordCloud
    result = WordCloud(api_config,server_config)
    result.show_all_cloud()

def stadistic_execute(api_config,server_config):
    from api.visualize.stadistic import CountAtritubte
    result = CountAtritubte(api_config,server_config)
    result.download_plots()
    result.show_plots()

def links_execute(api_config,server_config):
    from api.visualize.links_search import LinksSearch
    result = LinksSearch(api_config,server_config)
    result.print_all_reports()
    

    
valid_services = [
        "visualize.stadistic",
        "visualize.links_search",
        "visualize.word_cloud"
]

services = [
        word_cloud_execute,
        stadistic_execute,
        links_execute
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
        default="example",
        help="domain to use, default example.com ",
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
        logging.error("Missing or invalid service, must be one of", valid_services)
        exit(1)
    
    api_config_dir = args.service.replace('.', '/')
    api_config = load_config(os.path.join("base_config/api",api_config_dir,"api-config.yaml"))
    server_config = load_config("base_config/api/grobid-server-config.yaml")
    
    server_config.port = args.port
    server_config.protocol = args.protocol
    server_config.api_domain = args.domain
    try:
        services[args.serice](server_config,api_config)
    except Exception as e:
        logging.error(e)
        exit(1)
    
    

    