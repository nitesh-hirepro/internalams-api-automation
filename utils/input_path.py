import os
# path = os.getenv("HOME")
# generic_path = "%s/"
# generic_input_path = "%s/internalams_api_automation/input_data/" % path

generic_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
generic_input_path = generic_path + "/input_data/"

input_paths = {
    'login_input_sheet': generic_input_path  + "login/login.xls",
    'api_automation_log': generic_path + "/logs/api_automation.log",
    'resume_extractor_input_sheet': generic_input_path + 'resume_extractor_sheet/resume_extractor_input_sheet.xlsx'
}