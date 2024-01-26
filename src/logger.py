import os
import logging
from datetime import datetime

# logging file formatting
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOGS_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE)

# check if logs directory exists, if not then make it
os.makedirs(LOGS_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOGS_PATH, LOG_FILE)

logging.basicConfig(
    level='INFO',
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
)
