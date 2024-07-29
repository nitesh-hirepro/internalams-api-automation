import unittest
from tests.test_output_report import OutputReport
import sys


def main():
    # Discover and load all test cases from the 'tests' directory that match the pattern 'test_*.py'
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir='tests', pattern='test_*.py')

    # Run the test suite
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)

    final_report = OutputReport()
    final_report.output_report()
    final_report.overall_status()

    # Exit with a proper exit code
    sys.exit(not result.wasSuccessful())


if __name__ == '__main__':
    main()

