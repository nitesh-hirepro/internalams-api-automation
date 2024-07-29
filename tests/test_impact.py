import unittest
from utils.impact.impact_api_client import ImpactAPIClient
from utils.exceptions import APIClientError
from utils.logger import logger
from utils.data_loader import DataLoader
import pandas as pd
from utils.output_path import output_paths

results = []


class TestImpact(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.impact_api_client = ImpactAPIClient()
        data1 = DataLoader()
        logged_in_data = data1.load_login_data()
        cls.impact_api_client.login(logged_in_data)

    def test_get_impact_data(self):
        logger.info('===================================================================')
        logger.info('Running get_impact_data test case')
        try:
            impact_data = self.impact_api_client.get_impact_data()
            self.assertEqual(impact_data['statusCode'], 200)
            self.assertIsInstance(impact_data, dict)
            self.assertGreater(len(impact_data['TimeSheetEntrys']), 0)
            results.append({'Test Case': 'get_impact_data', 'Status': 'Pass'})
        except APIClientError as e:
            logger.error(f'Error while fetching impact data: {e}', exc_info=True)
            results.append({'Test Case': 'get_impact_data', 'Status': 'Fail', 'Error': str(e)})
            raise APIClientError(f'Failed to get impact data: {e}')

    # @unittest.skip('data already created')
    def test_create_impact_entry(self):
        logger.info('===================================================================')
        logger.info('Running create_impact_entry test case')
        try:
            impact_created_data = self.impact_api_client.create_impact_data()
            self.assertEqual(impact_created_data['statusCode'], 200)
            self.assertEqual(impact_created_data['status'], 'OK')
            self.assertGreater(impact_created_data['TimeSheetId'], 1000000)
            results.append({'Test Case': 'create_impact_entry', 'Status': 'Pass'})
        except APIClientError as e:
            logger.error(f'Error while fetching impact data: {e}', exc_info=True)
            results.append({'Test Case': 'create_impact_data', 'Status': 'Fail', 'Error': str(e)})
            raise APIClientError(f'Failed to get impact data: {e}')

    def test_search_impact(self):
        logger.info('==================================================================')
        logger.info('Running search_impact test case')
        try:
            impact_search_data = self.impact_api_client.search_impact()
            self.assertIsInstance(impact_search_data, dict, 'return data is not of dict type')
            self.assertEqual(impact_search_data['statusCode'], 200)
            self.assertGreater(impact_search_data['TotalItem'], 0, 'search count is not greater than 3')
            results.append({'Test Case': 'search_impact', 'Status': 'Pass'})
        except APIClientError as e:
            logger.exception(f'Error while fetching impact data: {e}')
            results.append({'Test Case': 'search_impact', 'Status': 'Fail', 'Error': str(e)})
            raise APIClientError(f'Failed to get impact data: {e}')

    @classmethod
    def tearDownClass(cls):
        df = pd.DataFrame(results)
        print(df)
        df.to_excel(output_paths.get('impact_report'), index=False, sheet_name='impact cases')


if __name__ == '__main__':
    unittest.main()
