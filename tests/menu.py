import pytest
from selenium import webdriver


@pytest.fixture()
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_menu(driver):
    driver.get("http://localhost/litecart/admin/")
    user_input = driver.find_element_by_name("username")
    user_input.clear()
    user_input.send_keys("admin")
    password_input = driver.find_element_by_name("password")
    password_input.clear()
    password_input.send_keys("admin")
    driver.find_element_by_name("login").click()
    menu = driver.find_element_by_id("box-apps-menu")
    elements = menu.find_elements_by_css_selector("li")
    for tab in range(1, len(elements)+1):
        main_link = driver.find_element_by_css_selector('#app-:nth-child(%d)' % tab)
        main_link.click()
        selected_tab = driver.find_element_by_class_name('selected')
        sub_tab = selected_tab.find_elements_by_css_selector('li')
        for a in range(1, len(sub_tab)+1):
            sub_link = driver.find_element_by_css_selector('.docs :nth-child(%d)' % a)
            sub_link.click()
            h1 = driver.find_element_by_tag_name('h1')
            print("h1 text: " + h1.text)
            tab += 1
