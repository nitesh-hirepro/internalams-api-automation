import json
import requests
from hirepro_automation.enviroment import apis, sprint_version
# from hirepro_automation.login import read_data
# from utils.logger import logger
from utils.login_api_client import LoginAPIClient
from utils.data_loader import DataLoader
from utils.helper import generate_dummy_email, generate_today_and_year_later_date


class SourceAPIClient(LoginAPIClient):
    def __init__(self):
        super().__init__()

    def get_all_source_data(self):
        payload = {
            "PagingCriteria":
                {
                    "MaxResults": 20,
                    "PageNo": 1
                },
            "SourceFilters":
                {
                    "TypeOfSource": 0
                }
        }
        url = apis.get('get_all_sources')
        response = requests.post(url, headers=self.header, json=payload)
        response.raise_for_status()
        return response.json()

    def get_all_unarchived_source_data(self):
        payload = {
            "PagingCriteria": {
                "MaxResults": 20,
                "PageNo": 1,
                "ObjectState": 1
            },
            "SourceFilters": {
                "TypeOfSource": 0
            }
        }
        url = apis.get('get_all_sources')
        response = requests.post(url, headers=self.header, json=payload)
        response.raise_for_status()
        return response.json()

    def create_source(self):
        source_name = "job portal automation" + sprint_version
        date = generate_today_and_year_later_date()
        payload = {
            "Source": {
                "SourceTypeId": 2,
                "SourceName": source_name,
                "EmailId": generate_dummy_email(),
                "Location": 1805,
                "ValidFrom": date[0],
                "ValidTill": date[1],
                "Description": "Dummy Description",
                "ContractId": "1371"
            }
        }
        url = apis.get('create_source')
        response = requests.post(url, headers=self.header, json=payload)
        response.raise_for_status()
        return response.json()

    def get_latest_all_source_details(self):
        data = self.get_all_source_data()
        sources = data['Sources']
        latest_id = sources[0].get("Id")
        name = sources[0].get("SourceName")
        email = sources[0].get("Email")
        return latest_id, name, email

    def get_latest_unarchived_detail(self):
        data = self.get_all_unarchived_source_data()
        sources = data['Sources']
        latest_id = sources[0].get("Id")
        return latest_id


    def search_source(self):
        data = self.get_latest_all_source_details()
        payload = {
            "PagingCriteria": {
                "MaxResults": 20,
                "PageNo": 1
            },
            "SourceFilters": {
                "Name": data[1],
                "Email": data[2],
                "TypeOfSource": 0
            }
        }
        url = apis.get('get_all_sources')
        response = requests.post(url, headers=self.header, json=payload)
        response.raise_for_status()
        return response.json()

    def update_source(self):
        response = self.get_latest_all_source_details()
        date = generate_today_and_year_later_date()
        payload = {
            "Source": {
                "SourceTypeId": 2,
                "SourceName": response[1],
                "EmailId": response[2],
                "Location": 1803,
                "ValidFrom": date[0],
                "ValidTill": date[1],
                "Description": "Description updated",
                "ContractId": "1371"
            },
            "SourceId": response[0]
        }
        url = apis.get('update_source')
        response = requests.post(url, headers=self.header, json=payload)
        response.raise_for_status()
        return response.json()

    def archive_source(self):
        data = self.get_latest_all_source_details()
        latest_id = data[0]
        payload = {
            "Ids": [latest_id]
        }
        url = apis.get('archive_source')
        response = requests.post(url, headers=self.header, json=payload)
        response.raise_for_status()
        return response.json()

    def unarchive_source(self):
        data = self.get_latest_unarchived_detail()
        latest_id = data
        payload = {
            "Ids": [latest_id]
        }
        url = apis.get('unarchive_source')
        response = requests.post(url, headers=self.header, json=payload)
        response.raise_for_status()
        return response.json()

# source = SourceAPIClient()
# data1 = DataLoader()
# logged_in_data = data1.load_login_data_admin()
# source.login(logged_in_data)
# print(json.dumps(source.unarchive_source(), indent=2))
