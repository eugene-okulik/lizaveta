from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.qa-practice.com/elements/input/simple")
search_field = driver.find_element(By.ID, "id_text_string")
search_field.send_keys("GTA")
search_field.send_keys(Keys.ENTER)
search_result = driver.find_element(By.ID, "result-text")
print(search_result.text)
driver.quit()
