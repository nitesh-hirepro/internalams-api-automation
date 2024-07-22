import os
path = os.getenv("HOME")

generic_input_path = "%s/internalams_api_automation/input_data/" % path

input_paths = {
    'login_input_sheet': generic_input_path + "login/login.xls",
    'api_automation_log': "/home/niteshgupta/internalams_api_automation/logs/api_automation.log"
}