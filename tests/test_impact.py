import unittest
from utils.impact.impact_api_client import ImpactAPIClient
from utils.exceptions import APIClientError
from utils.logger import logger
from utils.data_loader import DataLoader
# import pandas as pd
# from utils.output_path import output_paths
# from test_output_report import OutputReport
from utils.Result import impact_result


class TestImpact(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.impact_api_client = ImpactAPIClient()
        data1 = DataLoader()
        logged_in_data = data1.load_login_data()
        cls.impact_api_client.login(logged_in_data)

    def test_01_get_impact_data(self):
        logger.info('===================================================================')
        logger.info('Running get_impact_data test case')
        try:
            impact_data = self.impact_api_client.get_impact_data()
            self.assertEqual(impact_data['statusCode'], 200)
            self.assertIsInstance(impact_data, dict)
            self.assertGreater(len(impact_data['TimeSheetEntrys']), 0)
            impact_result.append({'Test Case': 'get_impact_data', 'Status': 'Pass'})
        except APIClientError as e:
            logger.error(f'Error while fetching impact data: {e}', exc_info=True)
            impact_result.append({'Test Case': 'get_impact_data', 'Status': 'Fail', 'Error': str(e)})
            raise APIClientError(f'Failed to get impact data: {e}')

    # @unittest.skip('data already created')
    def test_02_create_impact_entry(self):
        logger.info('===================================================================')
        logger.info('Running create_impact_entry test case')
        try:
            impact_created_data = self.impact_api_client.create_impact_data()
            self.assertEqual(impact_created_data['statusCode'], 200)
            self.assertEqual(impact_created_data['status'], 'OK')
            self.assertGreater(impact_created_data['TimeSheetId'], 1000000)
            impact_result.append({'Test Case': 'create_impact_entry', 'Status': 'Pass'})
        except APIClientError as e:
            logger.error(f'Error while fetching impact data: {e}', exc_info=True)
            impact_result.append({'Test Case': 'create_impact_data', 'Status': 'Fail', 'Error': str(e)})
            raise APIClientError(f'Failed to get impact data: {e}')
        except AssertionError as a:
            impact_result.append({'Test Case': 'create_impact_entry', 'Status': 'Fail', 'Error': str(a)})

    def test_03_search_impact(self):
        logger.info('==================================================================')
        logger.info('Running search_impact test case')
        try:
            impact_search_data = self.impact_api_client.search_impact()
            self.assertIsInstance(impact_search_data, dict, 'return data is not of dict type')
            self.assertEqual(impact_search_data['statusCode'], 200)
            self.assertGreater(impact_search_data['TotalItem'], 0, 'search count is not greater than 3')
            impact_result.append({'Test Case': 'search_impact', 'Status': 'Pass'})
        except APIClientError as e:
            logger.exception(f'Error while fetching impact data: {e}')
            impact_result.append({'Test Case': 'search_impact', 'Status': 'Fail', 'Error': str(e)})
            raise APIClientError(f'Failed to get impact data: {e}')

    def test_04_update_impact_data(self):
        logger.info('===================================================================')
        logger.info('Running update_impact_entry test case')
        try:
            impact_update_data = self.impact_api_client.update_impact_data()
            latest_timesheet_id = self.impact_api_client.get_latest_impact_id()
            self.assertEqual(impact_update_data['statusCode'], 200)
            self.assertEqual(impact_update_data['TimeSheetId'], latest_timesheet_id)
            impact_result.append({'Test Case': 'update_impact_entry', 'Status': 'Pass'})
        except AssertionError as a:
            impact_result.append({'Test Case': 'update_impact_entry', 'Status': 'Fail', 'Error': str(a)})
        except APIClientError as e:
            logger.error(f'Error while updating impact data: {e}', exc_info=True)
            impact_result.append({'Test Case': 'update_impact_data', 'Status': 'Fail', 'Error': str(e)})
            raise APIClientError(f'Failed to update impact data: {e}')

    # @classmethod
    # def tearDownClass(cls):
    #     final_report = OutputReport()
    #     final_report.output_report()
    #     final_report.overall_status()
    #     df = pd.DataFrame(results)
    #     print(df)
    #     df.to_excel(output_paths.get('impact_report'), index=False, sheet_name='impact cases')


# if __name__ == '__main__':
#     unittest.main()
