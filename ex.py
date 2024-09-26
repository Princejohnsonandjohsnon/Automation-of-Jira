import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/frames")
driver.maximize_window()
driver.implicitly_wait(10)
frameElement=driver.find_element(By.XPATH,"//iframe[@id='frame2']")
driver.switch_to.frame(frameElement)

driver.implicitly_wait(10)
value=driver.find_element(By.XPATH,"").text
print('text is',value)


driver.implicitly_wait(10)

driver.get_screenshot_as_file("prince.png")
driver.close()
