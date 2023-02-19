import os
from google.cloud import logging

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cred.json"

logging_client = logging.Client()
log_name = "my-log"
logger = logging_client.logger(log_name)
text = "Hello, world!!!!!!!!"
logger.log_text(text)
print("Logged: {}".format(text))
