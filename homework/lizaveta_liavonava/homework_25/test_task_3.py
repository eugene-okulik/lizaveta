import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


def test_language_submit(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    select_language = Select(driver.find_element(By.ID, "id_choose_language"))
    language = 'Python'
    select_language.select_by_visible_text(language)
    submit_button = driver.find_element(By.ID, "submit-id-submit")
    submit_button.click()
    submit_result = driver.find_element(By.ID, "result-text")
    assert submit_result.text == language


def test_hello_world(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_button = driver.find_element(By.CSS_SELECTOR, '#start button')
    start_button.click()
    final_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'finish'))
    )
    assert final_text.text == 'Hello World!'
