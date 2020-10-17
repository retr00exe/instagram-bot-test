from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

username = ""
password = ""

driver = webdriver.Chrome(executable_path="/home/retr00exe/Dev/Python/instabot-selenium/chromedriver_linux64")
driver.set_window_size(1920, 1080)
driver.get("https://instagram.com")
sleep(2)

driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
sleep(5)

driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
sleep(5)
driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

while True:
    for i in range(5):
        driver.find_element_by_xpath("//button[text()='Follow']").click()
        sleep(5)
    driver.refresh()
    sleep(20)
