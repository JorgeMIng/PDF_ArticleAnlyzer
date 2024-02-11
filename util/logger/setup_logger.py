
import sys
import logging
from datetime import datetime
from pathlib import Path
import os


def setup_logger():
    logger_name="grobid_logger"
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    
    now_time_str=datetime.now().strftime('d_%m_%Y')
    
    
    
    father_path = Path(os.path.dirname(__file__))

    father_path = father_path.parents[1]
    file_dir = os.path.join(father_path,"logs",logger_name+"_"+now_time_str)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    

    # Create handlers for logging to the standard output and a file
    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    err_handler = logging.FileHandler(os.path.join(file_dir,"error.log"),delay=True)
    warn_handler = logging.FileHandler(os.path.join(file_dir,"warn.log"),delay=True)
    warning_handler = logging.FileHandler(os.path.join(file_dir,"warning.log"),delay=True)
    info_handler = logging.FileHandler(os.path.join(file_dir,"info.log"),delay=True)
    debug_handler = logging.FileHandler(os.path.join(file_dir,"debug.log"),delay=True)
    critical_handler = logging.FileHandler(os.path.join(file_dir,"critical.log"),delay=True)
    fatal_handler = logging.FileHandler(os.path.join(file_dir,"fatal.log"),delay=True)

    # Set the log levels on the handlers
    
    stdout_handler.setLevel(logging.DEBUG)
    
    err_handler.setLevel(logging.ERROR)
    warn_handler.setLevel(logging.WARN)
    info_handler.setLevel(logging.INFO)
    critical_handler.setLevel(logging.CRITICAL)
    debug_handler.setLevel(logging.DEBUG)
    warning_handler.setLevel(logging.WARNING)
    fatal_handler.setLevel(logging.FATAL)
    

    
    # Create a log format using Log Record attributes
    fmt = logging.Formatter(
        "%(name)s: %(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(process)d >>> %(message)s"
    )

    # Set the log format on each handler
    stdout_handler.setFormatter(fmt)
    err_handler.setFormatter(fmt)
    warn_handler.setFormatter(fmt)
    info_handler.setFormatter(fmt)
    critical_handler.setFormatter(fmt)
    debug_handler.setFormatter(fmt)
    warning_handler.setFormatter(fmt)
    fatal_handler.setFormatter(fmt)
    
    # Add each handler to the Logger object
    logger.addHandler(stdout_handler)
    logger.addHandler(err_handler)
    logger.addHandler(warn_handler)
    logger.addHandler(info_handler)
    
    logger.addHandler(critical_handler)
    logger.addHandler(debug_handler)
    logger.addHandler(warning_handler)
    logger.addHandler(fatal_handler) 
                     
    return logger
    
    

  