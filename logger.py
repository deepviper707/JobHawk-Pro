"""JobHawk Pro: Mission Logging System"""
import logging
import sys

def setup_logger():
    logger = logging.getLogger('jobhawk_pro')
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        ch = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger
