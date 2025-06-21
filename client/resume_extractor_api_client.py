import base64
import json
import requests
from utils.login_api_client import LoginAPIClient
from hirepro_automation.enviroment import apis
from utils.data_loader import DataLoader


class ResumeExtractorAPIClient(LoginAPIClient):
    def __init__(self):
        super().__init__()

    def extract_resume(self, file_path):
        file_content = None
        file_name = file_path.split('/')[-1]
        with open(file_path, 'rb') as fr:
            file_content = base64.b64encode(fr.read()).decode('utf-8')

        posting_request = {"FileContent": file_content, "FileName": file_name}
        url = apis.get("extract_resume")
        response = requests.post(url, headers=self.header, json=posting_request)
        response.raise_for_status()
        return response.json()



resume = ResumeExtractorAPIClient()
data1 = DataLoader()
logged_in_data = data1.load_login_data()
resume.login(logged_in_data)
print(json.dumps(resume.extract_resume("/home/niteshgupta/Documents/internalams-automation/resume-extractor-automation/data/resume_data/Resume2.pdf"), indent=2))
