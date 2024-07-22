import datetime
import json
import time
import requests
import urllib3
from hirepro_automation.enviroment import *
from utils.read_excel import ExcelRead


class LoginWithCaptchaOff:
    def __init__(self):
        self.app_name = input("App-Name: crpo: ")
        self.header = {"content-type": "application/json", "APP-NAME": self.app_name}
        self.get_token = ''

    def common_login(self, tenant_name, login_name, user_name, password):
        # ---------------------- INTERNALAMS LOGIN ------------------------------
        print("-------------------------------------")
        now = datetime.datetime.now()
        now = now.strftime('%A %d %B %Y')
        print("Run started at: ", now)

        login_data = {"LoginName": login_name, "Password": password, "TenantAlias": tenant_name, "UserName": user_name}

        try:
            urllib3.disable_warnings()
            login_api = requests.post(apis.get('login_to_internalams'), headers=self.header, data=json.dumps(login_data),
                                      verify=False)
            response = login_api.json()
            self.get_token = response.get("Token")
            print("Token", self.get_token)
            time.sleep(1)
            resp_dict = json.loads(login_api.content)
            status = resp_dict['status']
            if status == 'OK':
                self.login = 'OK'
                print("Internalams Login successfully")
            else:
                self.login = 'KO'
                print("Internalams Login Failed")
        except ValueError as login_error:
            print(login_error)


login_object = LoginWithCaptchaOff()
read_data = ExcelRead()
read_data.excel_read("../input_data/login/login.xls", 0)
data = read_data.complete_excel_data[0]
login_object.common_login(data.get('Tenant'), data.get('Username'), data.get('Loginname'), data.get('Password'))
