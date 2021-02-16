
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
# Replace below path with the absolute path of the \
#chromedriver in your computer
#WebDriver driver = new FirefoxDriver();
driver = webdriver.Firefox(executable_path ='/root/Desktop/geckodriver')
#x-special/nautilus-clipboard
#copy
#file:///root/Desktop/geckodriver

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600) 
print("confirmed1")
  
target = '"Enter contact"'
print("confirmed2")
  
# Replace the below string with your own message 
string = "#enter message"
print("confirmed3")
  
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located(( By.XPATH, x_arg))) 
group_title.click() 
print("confirmed4")
inp_xpath = '//div[@class="_3FRCZ copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]'
print("confirmed5")
input_box = wait.until(EC.presence_of_element_located(( 
    By.XPATH, inp_xpath))) 
print("confirmed6")
for i in range(100): 
    input_box.send_keys(string + Keys.ENTER) 
    time.sleep(1) 



