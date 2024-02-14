import os
from util.logger import logging
from omegaconf import DictConfig, OmegaConf


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
        desired_path =os.path.join(os.path.dirname(__file__),config_name)
    except Exception:
        logging.error("config_name ",config_name," doesnt have a config file desiganated at config folder")


    try:
        config = OmegaConf.load(desired_path)
    except Exception as e:
        error_messege = "Error with config file loading: "+str(e)
        logging.error(error_messege)
        raise ValueError(error_messege)
    return config
    
        