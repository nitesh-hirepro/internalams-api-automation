import os
path = os.getenv("HOME")

generic_output_path = "%s/internalams_api_automation/reports/" % path

output_paths = {
    'impact_report': generic_output_path + "impact/test_impact_report.xlsx",
}