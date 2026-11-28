import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-features=HttpsFirstBalancedModeAutoEnable')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()


def test_cart_added_item(driver):
    driver.get("http://testshop.qa-practice.com/")
    first_product = driver.find_element(By.CSS_SELECTOR, '.oe_product_image_link')
    ActionChains(driver).key_down(Keys.COMMAND).click(first_product).key_up(Keys.COMMAND).perform()
    WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
    main_tab = driver.window_handles[0]
    product_tab = driver.window_handles[1]
    driver.switch_to.window(product_tab)
    product_name = driver.find_element(By.TAG_NAME, 'h1').text
    driver.find_element(By.ID, 'add_to_cart').click()
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Continue Shopping']]"))
    )
    continue_button.click()
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.my_cart_quantity'), '1')
    )
    driver.close()
    driver.switch_to.window(main_tab)
    driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/cart"]').click()
    cart_item = driver.find_element(By.CSS_SELECTOR, '#cart_products h6')
    assert product_name in cart_item.text


def test_popup_over_hovering(driver):
    driver.get("http://testshop.qa-practice.com/")
    product_image = driver.find_element(By.CSS_SELECTOR, '.oe_product_image')
    product_name = driver.find_element(By.CSS_SELECTOR, '.o_wsale_products_item_title a').text
    cart_button = driver.find_element(By.CSS_SELECTOR, '.o_wsale_product_btn a')
    ActionChains(driver).move_to_element(product_image).perform()
    WebDriverWait(driver, 5).until(EC.visibility_of(cart_button))
    cart_button.click()
    popup_product = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal .product-name'))
    )
    assert product_name in popup_product.text
