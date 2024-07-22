import logging
from utils import input_path

logging.basicConfig(
    level=logging.DEBUG,
    filename=input_path.input_paths.get('api_automation_log'),
    filemode='w',
    format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d-%B-%Y %H:%M:%S'
)

logger = logging.getLogger(__name__)
