from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <command>")
    print("Available commands: 0(punch-in), 1(punch-out)")
    sys.exit(1)

command = sys.argv[1]
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--headless")

chromedriver_path = './chromedriver'  # 将此路径替换为Chromedriver的实际路径
service = webdriver.chrome.service.Service(chromedriver_path)

driver = webdriver.Chrome(options=options)

driver.get(
    "https://scsrwd.azurewebsites.net/Login.aspx?CompanyID=H26DF58F60UG4G81C52CFDP4")

username_field = driver.find_element(by=By.ID, value='FormLayout_edtUserID_I')
username_field.send_keys("__USERNAME__")

password_field = driver.find_element(
    by=By.ID, value='FormLayout_edtPassword_I')
password_field.send_keys("__PASSWORD__")
password_field.send_keys(Keys.RETURN)

time.sleep(5)

if command == "0":
    btn_xpth = '//*[@id="BtnWork"]'
elif command == "1":
    btn_xpth = '//*[@id="BtnOffWork"]'
else:
    print("Unknown command:", command)

try:
    driver.switch_to.frame("PageContent_FrameContent")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, btn_xpth))
    )
    element.click()

finally:
    time.sleep(2)

driver.switch_to.default_content()

try:
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "popupHelper_CIF-1")))
    popup_window = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="lbl_SwipeMessage0"]'))
    )
    popup_text = popup_window.text
    file_name = "punch-in.log"
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(popup_text + "\n")
finally:
    time.sleep(2)

driver.switch_to.default_content()

driver.quit()
