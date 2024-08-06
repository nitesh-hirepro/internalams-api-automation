import datetime
import xlwt
from utils import styles
from hirepro_automation.enviroment import sprint_version, login_server
from utils.logger import logger
from utils.output_path import output_paths
from utils.Result import impact_result


class OutputReport(styles.FontColor):
    def __init__(self):
        super().__init__()
        self.date_today = datetime.datetime.now()
        self.date_today = self.date_today.strftime('%d %B %Y')
        self.Expected_success_cases = list(map(lambda x: 'Pass', range(0, 7)))
        self.Actual_success_cases = []

        # Write Excel sheet for output results
        logger.info('===============================================================')
        self.wb_Result = xlwt.Workbook()
        logger.info('Excel Workbook Created')
        self.ws = self.wb_Result.add_sheet('API_Automation_{}'.format(sprint_version))

        self.impact_use_case_col = 0
        self.impact_status_col = 1
        self.row = 2

        excel_headers = ['Impact UseCases', 'Status']

        header_style = self.style0

        for index, header in enumerate(excel_headers):
            self.ws.write(1, index, header, header_style)

        logger.info('Excel headers are printed successfully')

    def output_report(self):
        # self.ws.write(row, column, data, style)
        self.ws.write(2, self.impact_use_case_col, 'Get Impact Data', self.style8)
        self.ws.write(3, self.impact_use_case_col, 'Create Impact Entry', self.style8)
        self.ws.write(4, self.impact_use_case_col, 'Search Impact Data', self.style8)
        self.ws.write(5, self.impact_use_case_col, 'Update Imapct Data', self.style8)
        self.ws.write(6, self.impact_use_case_col, 'Submit Impact', self.style8)
        self.ws.write(7, self.impact_use_case_col, 'Approve Impact', self.style8)
        self.ws.write(8, self.impact_use_case_col, 'Create Bulk Impact', self.style8)

        logger.info(f'result list {impact_result}')
        if impact_result[0]['Test Case'] == 'get_impact_data':
            if impact_result[0]['Status'] == 'Pass':
                self.Actual_success_cases.append('Pass')
                self.ws.write(self.row, self.impact_status_col, 'Pass', self.style7)
            else:
                self.Actual_success_cases.append('Fail')
                self.ws.write(self.row, self.impact_status_col, 'Fail', self.style3)
            self.row = self.row + 1

        if impact_result[1]['Test Case'] == 'create_impact_entry':
            if impact_result[1]['Status'] == 'Pass':
                self.Actual_success_cases.append('Pass')
                self.ws.write(self.row, self.impact_status_col, 'Pass', self.style7)
            else:
                self.Actual_success_cases.append('Fail')
                self.ws.write(self.row, self.impact_status_col, 'Fail', self.style3)
            self.row = self.row + 1

        if impact_result[2]['Test Case'] == 'search_impact':
            if impact_result[2]['Status'] == 'Pass':
                self.Actual_success_cases.append('Pass')
                self.ws.write(self.row, self.impact_status_col, 'Pass', self.style7)
            else:
                self.Actual_success_cases.append('Fail')
                self.ws.write(self.row, self.impact_status_col, 'Fail', self.style3)
            self.row = self.row + 1

        if impact_result[3]['Test Case'] == 'update_impact_entry':
            if impact_result[3]['Status'] == 'Pass':
                self.Actual_success_cases.append('Pass')
                self.ws.write(self.row, self.impact_status_col, 'Pass', self.style7)
            else:
                self.Actual_success_cases.append('Fail')
                self.ws.write(self.row, self.impact_status_col, 'Fail', self.style3)
            self.row = self.row + 1

        if impact_result[4]['Test Case'] == 'submit_impact':
            if impact_result[4]['Status'] == 'Pass':
                self.Actual_success_cases.append('Pass')
                self.ws.write(self.row, self.impact_status_col, 'Pass', self.style7)
            else:
                self.Actual_success_cases.append('Fail')
                self.ws.write(self.row, self.impact_status_col, 'Fail', self.style3)
            self.row = self.row + 1

        if impact_result[5]['Test Case'] == 'approve_impact':
            if impact_result[5]['Status'] == 'Pass':
                self.Actual_success_cases.append('Pass')
                self.ws.write(self.row, self.impact_status_col, 'Pass', self.style7)
            else:
                self.Actual_success_cases.append('Fail')
                self.ws.write(self.row, self.impact_status_col, 'Fail', self.style3)
            self.row = self.row + 1

        if impact_result[6]['Test Case'] == 'create_bulk_impact':
            if impact_result[6]['Status'] == 'Pass':
                self.Actual_success_cases.append('Pass')
                self.ws.write(self.row, self.impact_status_col, 'Pass', self.style7)
            else:
                self.Actual_success_cases.append('Fail')
                self.ws.write(self.row, self.impact_status_col, 'Fail', self.style3)
            self.row = self.row + 1

    def overall_status(self):
        self.ws.write(0, 0, 'OVERALL STATUS', self.style4)
        if self.Expected_success_cases == self.Actual_success_cases:
            self.ws.write(0, 1, 'Pass', self.style5)
        else:
            self.ws.write(0, 1, 'Fail', self.style6)

        self.ws.write(0, 2, 'SPRINT VERSION', self.style4)
        self.ws.write(0, 3, sprint_version, self.style5)
        self.ws.write(0, 4, 'SPRINT DATE', self.style4)
        self.ws.write(0, 5, self.date_today, self.style5)
        self.ws.write(0, 6, 'SERVER', self.style4)
        self.ws.write(0, 7, login_server, self.style5)
        self.wb_Result.save(output_paths.get('impact_report'))
