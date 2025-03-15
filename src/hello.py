import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from utils import setup_logging


setup_logging()
logger = logging.getLogger(__name__)

def main():
    logger.debug('This is a debug message')    
    logger.info('This is an info message')
    logger.warning('This is an warning message')
    logger.error('This is an error message')
    logger.critical('This is an critical message')

if __name__ == '__main__':
    main()

