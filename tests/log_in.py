import pytest
from selenium import webdriver


@pytest.fixture()
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    user_input = driver.find_element_by_name("username")
    user_input.clear()
    user_input.send_keys("admin")
    password_input = driver.find_element_by_name("password")
    password_input.clear()
    password_input.send_keys("admin")
    driver.find_element_by_name("login").click()


