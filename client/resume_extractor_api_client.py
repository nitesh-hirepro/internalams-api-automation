import base64
import json
import requests
from utils.login_api_client import LoginAPIClient
from hirepro_automation.enviroment import apis
from utils.data_loader import DataLoader
from utils.helper import get_value_or_empty, convert_date_format, transform_education_data, transform_work_experience


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

    def extract_personal_details(self, file_path):
        parsed_data = self.extract_resume(file_path)
        if parsed_data['status'] == 'OK' and parsed_data['statusCode'] == 200:
            personal_details_data = parsed_data['ParseResume']['PersonalDetails']
            work_profile_data = parsed_data['ParseResume']['WorkProfile']
            candidate_name = get_value_or_empty(personal_details_data, 'Name')
            candidate_email = get_value_or_empty(personal_details_data, 'Email1')
            candidate_mobile = get_value_or_empty(personal_details_data, 'Mobile1')
            candidate_location = (get_value_or_empty(personal_details_data, 'CurrentLocationMappedText') or
                                  get_value_or_empty(personal_details_data, 'CurrentLocationText'))
            candidate_experience_in_years = get_value_or_empty(personal_details_data, 'TotalExperienceInYears')
            candidate_experience_in_months = get_value_or_empty(personal_details_data,'TotalExperienceInMonths')
            if candidate_experience_in_years == "":
                candidate_experience_in_years = 0
            if candidate_experience_in_months == "":
                candidate_experience_in_months = 0
            candidate_experience = f"{candidate_experience_in_years}.{candidate_experience_in_months}"
            candidate_latest_company = self.extract_latest_company(work_profile_data)
            response_data = {
                'Name': candidate_name,
                'Email': candidate_email,
                'Mobile': candidate_mobile,
                'Location': candidate_location,
                'Experience': candidate_experience,
                'Company': candidate_latest_company
            }
            return response_data
        return parsed_data

    def extract_latest_company(self, work_profile_details) -> str:
        for work_profile in work_profile_details:
            if work_profile.get('IsLatest') == 1:
                return (
                        get_value_or_empty(work_profile, 'CompanyMappedText')
                        or get_value_or_empty(work_profile, 'EmployerText')
                )
        return ""

    def extract_additional_details(self, file_path):
        parsed_data = self.extract_resume(file_path)
        if not (parsed_data.get('status') == 'OK' and parsed_data.get('statusCode') == 200):
            return parsed_data

        resume_data = parsed_data.get('ParseResume', {})
        personal_details = resume_data.get('PersonalDetails', {})
        education_profile = resume_data.get('EducationProfile', [])
        work_profile = resume_data.get('WorkProfile', [])

        if "DateOfBirth" in personal_details:
            date_of_birth = convert_date_format(personal_details.get('DateOfBirth'))
        else:
            date_of_birth = ''

        output_education_profile = transform_education_data(education_profile)
        output_work_profile = transform_work_experience(work_profile)

        result = {
            "Secondary Email": personal_details.get("Email2", ""),
            "Secondary Phone": personal_details.get("PhoneOffice", ""),
            "Gender": personal_details.get("GenderText", ""),
            "Marital Status": personal_details.get("MaritalStatusText"),
            "DOB": date_of_birth,
            "PAN": personal_details.get("PanNo", ""),
            "Passport": personal_details.get("Passport", ""),
            "Educational Details": output_education_profile,
            "Work Profiles": output_work_profile
        }
        return result

# resume = ResumeExtractorAPIClient()
# data1 = DataLoader()
# logged_in_data = data1.load_login_data()
# resume.login(logged_in_data)
# print(json.dumps(resume.extract_additional_details("/home/niteshgupta/Downloads/RajkumarArumugam_Kanban.pdf"),
# indent=2))
