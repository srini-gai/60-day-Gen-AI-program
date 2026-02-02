from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as webdriverwait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://the-internet.herokuapp.com")
print(driver.title)

'''driver.back()
driver.forward()
driver.refresh()'''

#finding elements
element = driver.find_element("link text", "A/B Testing")

wait = webdriverwait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "A/B Testing")))

#interacting with elements
element.click() #navigates to A/B Testing page
element.send_keys("test") #types test in the input box
element.clear() #clears the input box

#Screenshots

driver.save_screenshot("screenshot.png")

#demo

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Edge browser
driver = webdriver.Edge()
driver.get("https://the-internet.herokuapp.com")
driver.maximize_window()

wait = WebDriverWait(driver, 10)  # 10 seconds timeout

print("Page title:", driver.title)

# 1️⃣ Test Login Feature
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Form Authentication"))).click()
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("tomsmith")
wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("SuperSecretPassword!")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.radius"))).click()
message = wait.until(EC.presence_of_element_located((By.ID, "flash"))).text
print("Login message:", message)
driver.back()

# 2️⃣ Test Dropdown Feature
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Dropdown"))).click()
dropdown = wait.until(EC.presence_of_element_located((By.ID, "dropdown")))
dropdown.click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='2']"))).click()
print("Dropdown option selected")
driver.back()

# 3️⃣ Test Checkboxes Feature
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Checkboxes"))).click()
checkboxes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox']")))
for box in checkboxes:
    if not box.is_selected():
        box.click()
print("Checkboxes selected")
driver.back()

# 4️⃣ Test File Upload Feature
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "File Upload"))).click()
upload_input = wait.until(EC.presence_of_element_located((By.ID, "file-upload")))
upload_input.send_keys("C:\\Windows\\System32\\drivers\\etc\\hosts")  # replace with a valid file path
wait.until(EC.element_to_be_clickable((By.ID, "file-submit"))).click()
print("File upload test done")
driver.back()

# 5️⃣ Test JavaScript Alerts
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "JavaScript Alerts"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Alert']"))).click()
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()
print("Alert handled successfully")

# Close browser
driver.quit()