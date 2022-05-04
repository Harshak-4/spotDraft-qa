import pytest
from selenium import webdriver

from config.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.default_directory": "/Users/teamstreamz/Downloads",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
    })

    """Set to True to run in headless mode"""
    options.headless = False
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH, options=options)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.quit()