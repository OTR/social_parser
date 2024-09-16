"""
# Plain text file to keep logs from the script
_LOG_FILE = '.data/logs/error.log'

# Default logging level, messages at that level will be displayed in log file
LOG_LEVEL = logging.DEBUG

# Log message format
# See: https://docs.python.org/3/library/logging.html#logging.Formatter
_LOG_MESSAGE_FORMAT = "%(asctime)-8s %(levelname)-8s %(message)s"

# Date format used for logging
# See: https://docs.python.org/3/library/time.html#time.strftime
_LOG_DATE_FORMAT = "%d.%m.%Y %H:%M:%S"
"""
import logging
import os
from pathlib import Path

class FileLogger:
    """"""
    _instance = None
    _PROJECT_ROOT = Path(__file__).parent.parent
    _LOG_FILE = _PROJECT_ROOT / '.data/logs/error.log'
    _LOG_MESSAGE_FORMAT = "%(asctime)-8s %(levelname)-8s %(message)s"
    _LOG_DATE_FORMAT = "%d.%m.%Y %H:%M:%S"
    _LOG_LEVEL = logging.DEBUG

    def __new__(cls, *args, **kwargs):
        """Python's implementation of singleton"""
        if not cls._instance:
            cls._instance = super(FileLogger, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, log_file=_LOG_FILE, log_level=_LOG_LEVEL):
        if self._initialized:
            return
        self._initialized = True

        # Ensure the log directory exists
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # Configure logging
        self.logger = logging.getLogger('FileLogger')

        file_handler = logging.FileHandler(self._LOG_FILE)
        file_handler.setFormatter(
            logging.Formatter(fmt=self._LOG_MESSAGE_FORMAT,
                              datefmt=self._LOG_DATE_FORMAT)
        )
        self.logger.addHandler(file_handler)
        self.logger.setLevel(log_level)

    def get_logger(self):
        return self.logger
