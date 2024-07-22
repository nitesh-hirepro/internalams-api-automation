import pandas as pd


class ExcelReport:
    def __init__(self, filename):
        self.file_name = filename
        self.writer = pd.ExcelWriter(self.file_name)