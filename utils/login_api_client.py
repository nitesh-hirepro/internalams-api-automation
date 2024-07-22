import json
import datetime
import requests
from utils.logger import logger
from utils.exceptions import APIClientError
from hirepro_automation.enviroment import apis
from utils.data_loader import DataLoader


class LoginAPIClient:
    def __init__(self):
        self.app_name = input("App-Name: crpo: ")
        self.header = {"Content-Type": "application/json", "app-name": self.app_name}
        self.get_token = ''

    def login(self, login_data):
        try:
            # ---------------------- INTERNALAMS LOGIN ------------------------------
            print("-------------------------------------")
            now = datetime.datetime.now()
            now = now.strftime('%A %d %B %Y')
            print("Run started at: ", now)
            login_response = requests.post(apis.get('login_to_internalams'), headers=self.header,
                                           data=json.dumps(login_data))
            login_response.raise_for_status()
            logger.debug('Login successfully: %s', login_response.json())
            self.get_token = login_response.json()['Token']
            self.header['X-Auth-Token'] = self.get_token
            print(self.header)
        except requests.RequestException as e:
            logger.error('Login failed: %s', e)
            raise APIClientError(f"Login failed: {e}")


"""
login = LoginAPIClient()
data = DataLoader()
# below method returns a list
logged_in_data = data.load_login_data()
login.login(logged_in_data[0])
"""
