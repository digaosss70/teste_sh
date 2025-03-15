import logging
from datetime import datetime

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        filename='./logs/app.log',
        format=f'{now} - %(asctime)s - %(pathname)s - %(lineno)d - %(levelname)s - %(message)s'
    )

