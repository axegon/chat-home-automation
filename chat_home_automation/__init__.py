import logging
import os
import sys

logging.basicConfig(
    stream=sys.stdout,
    level=getattr(logging, os.environ.get("CHATHOMEAUTOMATIONLOG", "INFO")),
)
