import logging
import pandas as pd

logger = logging.getLogger(__name__)


class ExcelReport:
    def __init__(self, filename):
        self.file_name = filename
        logger.debug("Preparing Excel writer for %s", filename)
        self.writer = pd.ExcelWriter(self.file_name)