from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get('https://play2048.co/')
flag = True
while flag:
    try:
        htmlElem2 = browser.find_element(By.CLASS_NAME,'retry-button')
        htmlElem = browser.find_element(By.CLASS_NAME,'score-container')
        print('Your score was: ' + htmlElem.text)     
        htmlElem2.click()        
        flag = False

    except ElementNotInteractableException:
        htmlElem = browser.find_element(By.TAG_NAME,'html')
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)
