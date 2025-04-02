from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from tests.test_impact import TestImpact
from tests.test_source import TestSource

impact_tests = TestLoader().loadTestsFromTestCase(TestImpact)
source_tests = TestLoader().loadTestsFromTestCase(TestSource)

suite = TestSuite([impact_tests, source_tests])

runner = HTMLTestRunner(
    output = 'reports/html_reports',
    combine_reports = True,
    report_name = "api_automation_report",
    add_timestamp = True,
    report_title = 'Internalams',
    open_in_browser = True
)

runner.run(suite)
