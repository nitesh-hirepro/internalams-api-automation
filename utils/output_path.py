import os
import datetime
from hirepro_automation.enviroment import login_server

# path = os.getenv("HOME")
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
generic_output_path = "%s/reports/" % path
now = datetime.datetime.now().strftime('%d-%m-%Y_%I:%M:%S_%p')

output_paths = {
    'automation_report': generic_output_path + "impact/test_api_automation_report.xls",
    'resume_extractor_report': generic_output_path + f'resume_extractor/resume_extraction_report_{login_server}_{now}.xlsx'
}