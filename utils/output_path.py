import os
path = os.getenv("HOME")

generic_output_path = "%s/internalams_api_automation/reports/" % path

output_paths = {
    'automation_report': generic_output_path + "impact/test_api_automation_report.xls",
}