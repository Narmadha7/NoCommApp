import pytest
from selenium import webdriver


@pytest.fixture()
def fixture_1():
    print("I am fixture method from separate file")
    driver = webdriver.Chrome()
    return driver
