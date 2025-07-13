import os
import datetime
from hirepro_automation.enviroment import login_server

path = os.getenv("HOME")
generic_output_path = "%s/internalams_api_automation/reports/" % path
now = datetime.datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')

output_paths = {
    'automation_report': generic_output_path + "impact/test_api_automation_report.xls",
    'resume_extractor_report': generic_output_path + f'resume_extractor/resume_extraction_report_{login_server}_{now}.xlsx'
}