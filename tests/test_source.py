import json
import unittest
from client.source.source_api_client import SourceAPIClient
from utils.exceptions import APIClientError
from utils.logger import logger
from utils.data_loader import DataLoader
from utils.Result import source_result


class TestSource(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.source_api_client = SourceAPIClient()
        data = DataLoader()
        logged_in_data = data.load_login_data_admin()
        cls.source_api_client.login(logged_in_data)

    def test_01_get_all_source_data(self):
        logger.info('===================================================================')
        logger.info('Running get_all_source_data test case')
        try:
            source_data = self.source_api_client.get_all_source_data()
            self.assertEqual(source_data['statusCode'], 200)
            self.assertIsInstance(source_data['Sources'], list)
            self.assertGreater(len(source_data['Sources']), 0)
            source_result.append({'Test Case': 'get_source_data', 'Status': 'Pass'})
        except AssertionError as a:
            logger.debug(f'Assertion Error Occured: {a}')
            source_result.append({'Test Case': 'get_source_data', 'Status': 'Fail'})
        except APIClientError as e:
            logger.exception(f'Error while fetching impact data: {e}')
            source_result.append({'Test Case': 'get_source_data', 'Status': 'Fail', 'Error': str(e)})
            raise APIClientError(f'Failed to get source data: {e}')

    def test_02_create_source(self):
        logger.info('===================================================================')
        logger.info('Running create source test case')
        try:
            response = self.source_api_client.create_source()
            self.assertEqual(response['status'], 'OK')
            self.assertEqual(response['statusCode'], 200)
            source_result.append({'Test Case': 'create_source', 'Status': 'Pass'})
        except AssertionError as a:
            logger.debug(f'Assertion Error Occured: {a}')
            source_result.append({'Test Case': 'create_source', 'Status': 'Fail'})
        except APIClientError as e:
            logger.exception(f'Error while creating source data: {e}')
            source_result.append({'Test Case': 'create_source', 'Status': 'Fail', 'Error': str(e)})
            raise APIClientError(f'Failed to create source data: {e}')

    def test_03_search_source(self):
        logger.info('======================================================================')
        logger.info('Running seacrh source test case')
        try:
            response = self.source_api_client.search_source()
            self.assertEqual(response['status'], "OK")
            self.assertGreater(len(response['Sources']), 0)
            self.assertEqual(response['TotalItem'], 1)
            source_result.append({'Test Case': 'search_source', 'Status': 'Pass'})
        except AssertionError as a:
            logger.debug(f'Assertion Error Occured: {a}')
            source_result.append({'Test Case': 'search_source', 'Status': 'Fail'})
        except APIClientError as e:
            logger.exception(f'Error while creating source data: {e}')
            source_result.append({'Test Case': 'search_source', 'Status': 'Fail', 'Error': str(e)})
            raise APIClientError(f'Failed to search source data: {e}')

    def test_04_update_source(self):
        logger.info('======================================================================')
        logger.info('Running update source test case')
        try:
            response = self.source_api_client.update_source()
            self.assertEqual(response['status'], "OK")
            self.assertEqual(response['statusCode'], 200)
            source_result.append({'Test Case': 'update_source', 'Status': 'Pass'})
        except AssertionError as a:
            logger.debug(f'Assertion Error Occured: {a}')
            source_result.append({'Test Case': 'update_source', 'Status': 'Fail'})
        except APIClientError as e:
            logger.exception(f'Error while creating source data: {e}')
            source_result.append({'Test Case': 'update_source', 'Status': 'Fail', 'Error': str(e)})
            raise APIClientError(f'Failed to update source data: {e}')

    def test_05_archive_source(self):
        logger.info('======================================================================')
        logger.info('Running archive source test case')
        try:
            data = self.source_api_client.get_latest_all_source_details()
            latest_id = data[0]
            response = self.source_api_client.archive_source()
            self.assertEqual(response['status'], "OK")
            self.assertGreater(len(response['IdsArchivedNow']), 0)
            self.assertEqual(response['IdsArchivedNow'][0], latest_id)
            source_result.append({'Test Case': 'archive_source', 'Status': 'Pass'})
        except AssertionError as a:
            logger.debug(f'Assertion Error Occured: {a}')
            source_result.append({'Test Case': 'archive_source', 'Status': 'Fail'})
        except APIClientError as e:
            logger.exception(f'Error while archiving source: {e}')
            source_result.append({'Test Case': 'archive_source', 'Status': 'Fail', 'Error': str(e)})
            raise APIClientError(f'Failed to archive source: {e}')

    def test_06_unarchive_source(self):
        logger.info('======================================================================')
        logger.info('Running un-archive source test case')
        try:
            data = self.source_api_client.get_latest_all_source_details()
            latest_id = data[0]
            response = self.source_api_client.unarchive_source()
            logger.debug(json.dumps(response, indent=2))
            self.assertEqual(response['status'], "OK")
            self.assertGreater(len(response['IdsUnArchivedNow']), 0)
            self.assertEqual(response['IdsUnArchivedNow'][0], latest_id)
            source_result.append({'Test Case': 'unarchive_source', 'Status': 'Pass'})
        except AssertionError as a:
            logger.debug(f'Assertion Error Occured: {a}')
            source_result.append({'Test Case': 'unarchive_source', 'Status': 'Fail'})
        except APIClientError as e:
            logger.exception(f'Error while un-archiving source: {e}')
            source_result.append({'Test Case': 'unarchive_source', 'Status': 'Fail', 'Error': str(e)})
            raise APIClientError(f'Failed to unarchive source: {e}')


if __name__ == '__main__':
    unittest.main()




