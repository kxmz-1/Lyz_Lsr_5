from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'forceAppLaunch': True,
    'appPackage': '',
    'appActivity': ''
}
desired_caps['appPackage'] = 'me.writeily'
desired_caps['appActivity'] = '.PromptPinActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'me.writeily:id/fab_expand_menu_button')))

fab_expand_menu_button_button = driver.find_element(MobileBy.ID, 'me.writeily:id/fab_expand_menu_button')
fab_expand_menu_button_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'me.writeily:id/create_note')))

create_note_button = driver.find_element(MobileBy.ID, 'me.writeily:id/create_note')
create_note_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'me.writeily:id/edit_note_title')))

edit_note_title_input = driver.find_element(MobileBy.ID, 'me.writeily:id/edit_note_title')
edit_note_title_input.send_keys('Title')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'me.writeily:id/note_content')))

note_content_input = driver.find_element(MobileBy.ID, 'me.writeily:id/note_content')
note_content_input.send_keys('abcde')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.CLASS_NAME, 'android.widget.ImageButton')))

ImageButton_button = driver.find_element(MobileBy.CLASS_NAME, 'android.widget.ImageButton')
ImageButton_button.click()

driver.quit()
