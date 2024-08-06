import requests
from hirepro_automation.enviroment import apis
from utils.login_api_client import LoginAPIClient
from utils.data_loader import DataLoader
from utils.helper import get_datetime_utc, get_tomorrow_date_utc
from utils.logger import logger


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

    def get_manager_team_record_impact_data(self):
        payload = {
            "PagingCriteria": {
                "MaxResults": 20,
                "PageNo": 1,
                "IsCountRequired": True
            },
            "TimeSheetOption": 2,
            "Filters": {
                "Status": 3
            }
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

    def get_latest_impact_id(self):
        all_impact_data = self.get_impact_data()
        latest_impact_data = all_impact_data['TimeSheetEntrys'][0]
        logger.info(f'latest impact data: {latest_impact_data}')
        latest_impact_id = latest_impact_data['Id']
        logger.info(f'latest impact id: {latest_impact_id}')
        return latest_impact_id

    def get_all_time_sheet_entrys_id(self):
        time_sheet_id = self.get_latest_impact_id()
        payload = {
            "TimeSheetEntryOption": "0",
            "TimeSheetId": str(time_sheet_id)
        }
        logger.info('Calling get_all_time_sheet_entry api')
        url = apis.get('get_all_time_sheet_entrys')
        response = requests.post(url, headers=self.header, json=payload)
        response.raise_for_status()
        logger.info('got get_all_time_sheet_entry api response succesfully')
        response_data = response.json()
        time_sheet_entrys = response_data['TimeSheetEntrys']['Entrys']
        latest_entry = time_sheet_entrys[0]
        latest_entry_id = latest_entry['Id']
        logger.info(f'latest entry id: {latest_entry_id}')
        created_on_date = latest_entry['Date']
        logger.info(f'created_on_date: {created_on_date}')
        return latest_entry_id, created_on_date

    def update_impact_data(self):
        time_sheet_id = self.get_latest_impact_id()
        entry_id, created_on_date = self.get_all_time_sheet_entrys_id()
        payload = {
            "TimeSheet": {
                "Entrys": [
                    {
                        "Id": entry_id,
                        "User": "Nitesh",
                        "UserId": "Nitesh",
                        "Date": created_on_date,
                        "Percentage": 100,
                        "Customer": 2749,
                        "CustomCustomerText": "",
                        "CustomerText": "python 3.10 account",
                        "BusinessOrder": 472,
                        "BusinessOrderText": "python 3.10 opp",
                        "Requisition": 30304,
                        "CustomRequisitionText": "",
                        "RequisitionText": "python 3.10 Job",
                        "Activity": 9889,
                        "ActivityText": "General Administration",
                        "ActivityType": 9846,
                        "ActivityTypeText": "Administration",
                        "Notes": "remarks updated",
                        "AccountId": 1,
                        "AccountText": "Account Latest Two",
                        "TimeSheetId": time_sheet_id,
                        "Bu": None,
                        "Sbu": None,
                        "Pl": None
                    }
                ],
                "Date": created_on_date,
                "TimeSheetId": time_sheet_id
            }
        }
        url = apis.get('create_impact')
        response = requests.post(url, headers=self.header, json=payload)
        response.raise_for_status()
        return response.json()

    def submit_impact(self):
        time_sheet_id = self.get_latest_impact_id()
        payload = {
            "TimeSheetDetails": {
                "Comments": "",
                "TimeSheetIds": [time_sheet_id]
            }
        }
        url = apis.get('submit_impact')
        response = requests.post(url, headers=self.header, json=payload)
        response.raise_for_status()
        return response.json()

    def get_latest_my_team_record_data(self):
        time_sheet_entrys = self.get_manager_team_record_impact_data()['TimeSheetEntrys']
        impact_id = time_sheet_entrys[0].get('Id')
        return impact_id

    def approve_impact(self):
        impact_id = self.get_latest_my_team_record_data()
        payload = {
            "TimeSheetDetails":
                {
                    "Comments": "data: approve",
                    "TimeSheetIds": [impact_id],
                    "Status": 1
                }
        }
        url = apis.get('approve_time_sheet')
        print(self.header)
        response = requests.post(url, headers=self.header, json=payload)
        response.raise_for_status()
        return response.json()

    def create_bulk_impact(self):
        today_date = get_datetime_utc()
        tomorrow_date = get_tomorrow_date_utc()
        payload = {
            "FromDate": today_date,
            "ToDate": tomorrow_date,
            "ActivityType": 7055,
            "Activity": 9848,
            "EmployeeIds": ["Ascript1", "Ascript2"]
        }
        url = apis.get('bulk_create_impact')
        response = requests.post(url, headers=self.header, json=payload)
        response.raise_for_status()
        return response.json()


# impact = ImpactAPIClient()
# data1 = DataLoader()
# logged_in_data = data1.load_login_data_manager()
# impact.login(logged_in_data)
# print(impact.approve_impact())
