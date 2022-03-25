from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
browser = webdriver.Firefox()
browser.get('https://play2048.co/')
htmlElem = browser.find_element_by_tag_name('html')
while True:
    try:
        htmlElem2 = browser.find_element_by_class_name('retry-button')
        htmlElem = browser.find_element_by_class_name('score-container')
        print('Your score was: ' + htmlElem.text)

        htmlElem2.click()

    except ElementNotInteractableException:
        htmlElem = browser.find_element_by_tag_name('html')
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)

