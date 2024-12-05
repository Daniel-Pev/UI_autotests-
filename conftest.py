import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--lang=en")
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")  # open Browser in maximized mode
    options.add_argument("--disable-infobars")  # disabling infobars
    options.add_argument("--disable-extensions")  # disabling extensions
    options.add_argument("--disable-gpu")  # applicable to windows os only
    options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
    options.add_argument("--disable-search-engine-choice-screen")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
