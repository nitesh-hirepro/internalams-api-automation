import requests
from hirepro_automation.enviroment import apis
from utils.login_api_client import LoginAPIClient
from utils.data_loader import DataLoader
from utils.helper import get_datetime_utc


class ImpactAPIClient(LoginAPIClient):
    def __init__(self):
        super().__init__()

    def get_impact_data(self):
        payload = {
            "PagingCriteria": {"MaxResults": 20,
                               "PageNo": 1,
                               "IsCountRequired": True
                               },
            "TimeSheetOption": 0,
            "Filters": {"Status": 0}
        }
        url = apis.get('get_impact_data')
        response = requests.post(url, headers=self.header, json=payload)
        response.raise_for_status()
        return response.json()

    def create_impact_data(self):
        payload = {
            "TimeSheet": {
                "Entrys": [
                    {
                        "Date": get_datetime_utc(),
                        "ActivityType": 9846,
                        "Activity": 9889,
                        "Requisition": 30207,
                        "Customer": 2594,
                        "BusinessOrder": 195,
                        "AccountId": 1,
                        "Percentage": 100,
                        "Id": None,
                        "Notes": "1223",
                        "CustomCustomerText": "",
                        "CustomRequisitionText": "",
                        "Pl": None,
                        "Bu": None,
                        "Sbu": None,
                        "ActivityText": "General Administration",
                        "ActivityTypeText": "Administration",
                        "CustomerText": "Sprint 122 live Acc",
                        "BusinessOrderText": "sprint 122 liv BO",
                        "AccountText": "Account Latest Two",
                        "RequisitionText": "New Database Job"
                    }
                ],
                "Date": get_datetime_utc()
            }
        }
        url = apis.get('create_impact')
        response = requests.post(url, headers=self.header, json=payload)
        response.raise_for_status()
        return response.json()

    def search_impact(self):
        payload = {
            "PagingCriteria": {
                 "MaxResults": 20,
                 "PageNo": 1,
                 "IsCountRequired": True
                 },
            "TimeSheetOption": 0,
            "Filters": {
                "UnlockExceededType": "-1",
                "ActivityIds": ["9889"],
                "Customer": "2594",
                "ActivityType": "9846",
                "Status": 0
            }
        }
        url = apis.get('search_impact')
        response = requests.post(url, headers=self.header, json=payload)
        response.raise_for_status()
        return response.json()


# impact = ImpactAPIClient()
# data1 = DataLoader()
# logged_in_data = data1.load_login_data()
# impact.login(logged_in_data)
# print(impact.search_impact())
