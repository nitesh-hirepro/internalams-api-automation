import os
import pytest
from utils.logger import setup_logging

def pytest_addoption(parser):
    parser.addoption("--login-server", action="store", default="beta-internalams", help="Server to log into: beta-internalams, internalams, amsin, beta or ams")
    parser.addoption("--sprint-version", action='store', default="111", help="Sprint version, e.g. 193 or 194")
    parser.addoption("--app-name", action='store', default="crpo", help="App-Name header value, e.g. crpo")

def pytest_configure(config):
    # Runs after pytest has created its configuration object, but before the test collection and execution
    # This method (hook) is essentially taking pytest command-line options and putting them into environment variables so the rest of the test code can access them through os.environ"
    option_to_env = {
        'login_server': "LOGIN_SERVER",
        'sprint_version': 'SPRINT_VERSION',
        'app_name': 'APP_NAME'
    }
    for option_name, env_var in option_to_env.items():
        value = config.getoption(option_name)
        if value:
            os.environ[env_var] = value

@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    setup_logging()