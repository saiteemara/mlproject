# A Logger is a tool used to record messages (events) during program execution.
# Track execution
# Debug errors
# Monitor application behavior

'''
| Level    | Meaning                        |
| -------- | ------------------------------ |
| DEBUG    | Detailed info (for developers) |
| INFO     | General information            |
| WARNING  | Something unexpected           |
| ERROR    | Error occurred                 |
| CRITICAL | Serious failure                |'''


import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)