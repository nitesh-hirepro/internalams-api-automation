from utils.read_excel import ExcelRead
from utils.input_path import input_paths
from hirepro_automation.enviroment import login_server


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

    def load_login_data_by_server(self):
        """
        Load login data based on the login_server variable from environment.py
        """
        if login_server == 'beta-internalams':
            return self.load_login_data()
        elif login_server == 'internalams':
            return self.load_login_data_recruiter_internalams()
        elif login_server == 'amsin':
            return self.load_login_data_recruiter_amsin()
        elif login_server == 'beta' or login_server == 'ams':
            return self.load_login_data_recruiter_ams()
        else:
            print(f'{login_server} server not found')
            return {}

