import os
from pdf_analyzer.logger import logging
from omegaconf import OmegaConf


def load_config(config_name:str):
    """_summary_

    Args:
        config_name (str): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    try:
        abs_dir = os.path.abspath("")
        desired_path =os.path.join(abs_dir,config_name)
    except Exception:
        logging.error("config_name ",config_name," doesnt have a config file desiganated at config folder")

    try:
        config = OmegaConf.load(desired_path)
    except Exception as e:
        error_messege = "Error with config file loading: "+str(e)
        logging.error(error_messege)
        raise ValueError(error_messege)
    return config
    
        