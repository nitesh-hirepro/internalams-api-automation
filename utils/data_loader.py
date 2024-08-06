from utils.read_excel import ExcelRead
from utils.input_path import input_paths


class DataLoader(ExcelRead):
    def __init__(self):
        super().__init__()

    def load_login_data(self):
        self.excel_read(input_paths['login_input_sheet'], 0)
        return self.complete_excel_data[0]

    def load_login_data_manager(self):
        self.excel_read(input_paths['login_input_sheet'], 0)
        return self.complete_excel_data[1]

    def load_login_data_admin(self):
        self.excel_read(input_paths['login_input_sheet'], 0)
        return self.complete_excel_data[2]

