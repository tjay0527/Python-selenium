import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "edge"])
def driver(request):
    # browser = request.config.getoption("--browser")
    browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome()
    elif browser == "edge":
        my_driver = webdriver.Edge()
    else:
        raise TypeError(f"Expected 'chrome' or 'edge', but got {browser}")
    my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="edge", help="browser to execute tests (chrome or edge)"
    )