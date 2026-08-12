import json
import datetime
import logging
import requests
from utils.logger import logger
from utils.exceptions import APIClientError
from hirepro_automation.enviroment import apis
from utils.data_loader import DataLoader
from utils.helper import prompt_or_env

logger = logging.getLogger(__name__)


class LoginAPIClient:
    def __init__(self):
        self.app_name = prompt_or_env("APP_NAME", "App-Name: crpo: ")
        self.header = {"Content-Type": "application/json", "app-name": self.app_name}
        self.get_token = ''

    def login(self, login_data):
        try:
            # ---------------------- INTERNALAMS LOGIN ------------------------------
            now = datetime.datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
            logger.info("Run started at: %s", now)
            login_response = requests.post(apis.get('login_to_internalams'), headers=self.header,
                                           data=json.dumps(login_data))
            login_response.raise_for_status()
            response_json = login_response.json()
            logger.info('Login successfully for user: %s', response_json.get('LoginName'))
            self.get_token = login_response.json()['Token']
            self.header['X-Auth-Token'] = self.get_token
            logger.debug("Auth header set (app-name=%s, token=%s...)", self.app_name, self.get_token[:10])
        except requests.RequestException as e:
            logger.error('Login failed: %s', e)
            raise APIClientError(f"Login failed: {e}")



# login = LoginAPIClient()
# data = DataLoader()
# logged_in_data = data.load_login_data()
# login.login(logged_in_data)

