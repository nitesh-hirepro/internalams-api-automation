import logging
from utils import input_path

def setup_logging():
    root = logging.getLogger()
    root.handlers.clear()
    root.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        fmt='%(asctime)s - %(filename)s:%(lineno)d - %(name)s - %(levelname)s - %(message)s',
        datefmt='%d-%B-%Y %H:%M:%S',
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    root.addHandler(console_handler)

    file_handler = logging.FileHandler(input_path.input_paths.get('api_automation_log'), mode='w')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    root.addHandler(file_handler)

    # requests/urllib3 are very chatty at DEBUG - keeping them quiet unless something's wrong.
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    logging.getLogger('requests').setLevel(logging.WARNING)

logger = logging.getLogger(__name__)
