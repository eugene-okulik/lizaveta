from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.execute_script("document.querySelector('footer').remove();")
# first name
first_name = driver.find_element(By.ID, "firstName")
first_name.send_keys('Liza')
# last name
last_name = driver.find_element(By.ID, "lastName")
last_name.send_keys('Liav')
# email
email = driver.find_element(By.ID, "userEmail")
email.send_keys('emailemail@duch.com')
# mobile
mobile = driver.find_element(By.ID, "userNumber")
mobile.send_keys('1234567891')
# address
current_address = driver.find_element(By.ID, "currentAddress")
current_address.send_keys('Black St 34/1')
# gender
gender = driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-2"]')
gender.click()
# date of birth
driver.find_element(By.ID, "dateOfBirthInput").click()
calendar_month = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
calendar_month.select_by_visible_text('May')
calendar_year = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
calendar_year.select_by_visible_text('1995')
driver.find_element(By.CSS_SELECTOR, '.react-datepicker__day--015:not(.react-datepicker__day--outside-month)').click()
WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.CLASS_NAME, "react-datepicker__month-container"))
)
# subjects
subjects = driver.find_element(By.ID, "subjectsInput")
subjects.send_keys('Maths')
subjects.send_keys(Keys.ENTER)
# hobbies
hobbies = driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]')
hobbies.click()
# state and city
state = driver.find_element(By.CSS_SELECTOR, "#state input")
state.send_keys('NCR')
state.send_keys(Keys.ENTER)
city = driver.find_element(By.CSS_SELECTOR, "#city input")
city.send_keys('Delhi')
city.send_keys(Keys.ENTER)
# submit
submit = driver.find_element(By.ID, "submit")
submit.click()
final_form = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
)
print(final_form.text)
driver.quit()
