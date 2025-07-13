from utils.read_excel import ExcelRead
from utils.input_path import input_paths


class DataLoader(ExcelRead):
    login_data_file_path = input_paths['login_input_sheet']

    def __init__(self):
        super().__init__()

    def load_login_data(self):
        self.excel_read(DataLoader.login_data_file_path, 0)
        return self.complete_excel_data[0]

    def load_login_data_manager(self):
        self.excel_read(DataLoader.login_data_file_path, 0)
        return self.complete_excel_data[1]

    def load_login_data_admin(self):
        self.excel_read(DataLoader.login_data_file_path, 0)
        return self.complete_excel_data[2]

    def load_login_data_recruiter_internalams(self):
        self.excel_read(DataLoader.login_data_file_path, 1)
        return self.complete_excel_data[0]

    def load_login_data_recruiter_amsin(self):
        self.excel_read(DataLoader.login_data_file_path, 2)
        return self.complete_excel_data[0]

    def load_login_data_recruiter_ams(self):
        self.excel_read(DataLoader.login_data_file_path, 3)
        return self.complete_excel_data[0]

