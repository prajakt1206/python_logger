'''
This is logging config file having three types of logs files
1) error.log ------ you can see all application error logs in this file
2) debug.log------- you can see all application info and debug logs in this file
3) jobscheduler.lo- you can see all scheduler regarding logs in this file
'''

import logging

FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(message)s')



def setup_logger(name, log_file, level):
    """Function setup as many loggers as you want"""
    handler = logging.FileHandler(log_file)
    handler.setFormatter(FORMATTER)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

LOGGER_ERR = setup_logger('Error_logger', 'logs/error.log', logging.ERROR)
LOGGER_DEB = setup_logger('Debug_logger', 'logs/debug.log', logging.DEBUG)
LOGGER_SCHE = setup_logger('jobscheduler', 'logs/jobscheduler.log', logging.DEBUG)

def logger_error():
    """Function for error logs """
    return LOGGER_ERR


def logger_debug():
    """Function for debug logs """
    return LOGGER_DEB

def job_scheduler():
    """Function for jobscheduler logs """
    return LOGGER_SCHE
