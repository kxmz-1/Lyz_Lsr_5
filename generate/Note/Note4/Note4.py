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
desired_caps['appPackage'] = 'chan.android.app.pocketnote'
desired_caps['appActivity'] = '.MainActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'chan.android.app.pocketnote:id/notes_$_linearlayout_empty')))

linearlayout_empty_button = driver.find_element(MobileBy.ID, 'chan.android.app.pocketnote:id/notes_$_linearlayout_empty')
linearlayout_empty_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'chan.android.app.pocketnote:id/editor_$_edittext_title')))

edittext_title_input = driver.find_element(MobileBy.ID, 'chan.android.app.pocketnote:id/editor_$_edittext_title')
edittext_title_input.send_keys('abc')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'chan.android.app.pocketnote:id/editor_$_note_editor')))

note_editor_input = driver.find_element(MobileBy.ID, 'chan.android.app.pocketnote:id/editor_$_note_editor')
note_editor_input.send_keys('abc')

driver.hide_keyboard()

driver.quit()
