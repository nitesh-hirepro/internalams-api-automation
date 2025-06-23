import pytest
import logging
import os
import pandas as pd
from datetime import datetime
from utils.read_excel import ExcelRead
from utils.data_loader import DataLoader
from client.resume_extractor_api_client import ResumeExtractorAPIClient
from utils.write_excel import ExcelReport
from utils.input_path import input_paths, generic_input_path
from utils.output_path import output_paths

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestResumeExtractor:
    @pytest.fixture(scope="class")
    def setup(self):
        # Prepare all clients and data
        excel_reader = ExcelRead()
        data_loader = DataLoader()
        extractor = ResumeExtractorAPIClient()
        return excel_reader, data_loader, extractor

    def test_resume_extraction(self, setup):
        excel_reader, data_loader, extractor = setup
        results = []
        # report_path = None
        try:
            # 1. Read input Excel
            input_file = input_paths['resume_extractor_input_sheet']
            data_2d = excel_reader.read_xlsx(input_file, 0)
            logger.info(f"Read {len(data_2d)-1} data rows from input sheet.")
            if len(data_2d) <= 1:
                pytest.skip("No data rows in input sheet.")

            # 2. Login
            login_data = data_loader.load_login_data()
            extractor.login(login_data)
            logger.info("Login successful.")

            # 3. Loop over all rows (skip header)
            try:
                for row in data_2d[1:]:
                    try:
                        file_name = row[0]
                        full_file_path = generic_input_path + 'resumes/' + file_name
                        extracted = extractor.extract_personal_details(full_file_path)
                        results.append({
                            'File Name': file_name,
                            'Expected Name': row[8],
                            'Extracted Name': extracted.get('Name', ''),
                            'Expected Email': row[9],
                            'Extracted Email': extracted.get('Email', ''),
                            'Expected Mobile': row[10],
                            'Extracted Mobile': extracted.get('Mobile', ''),
                            'Expected Location': row[11],
                            'Extracted Location': extracted.get('Location', ''),
                            'Expected Experience': row[13],
                            'Extracted Experience': extracted.get('Experience', ''),
                            'Expected Company': row[14],
                            'Extracted Company': extracted.get('Company', ''),
                        })
                        logger.info(f"Processed: {file_name}")
                    except Exception as e:
                        logger.error(f"Error processing row: {e}")
                        continue
            except KeyboardInterrupt:
                logger.warning("Script interrupted by user. Generating report for processed rows so far.")

        except Exception as e:
            logger.error(f"Test failed: {e}")
            assert False, f"Test failed: {e}"
        finally:
            # 4. Write Excel report for all processed rows so far
            if results:
                df = pd.DataFrame(results)
                # Build styler (only for default formatting, not for coloring)
                styled_df = df.style
                report_path = output_paths.get('resume_extractor_report')
                excel_report = ExcelReport(report_path)
                styled_df.to_excel(excel_report.writer, index=False, sheet_name='Report')
                excel_report.writer.close()

                # Post-process with openpyxl for header and extracted columns coloring
                from utils.openpyxl_postprocess import postprocess_resume_report
                postprocess_resume_report(report_path)
                logger.info(f"Report generated: {report_path}")
            else:
                logger.warning("No results to report.")
