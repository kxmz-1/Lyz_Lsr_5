from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import json

# local import
from Util import Util
from WidgetUtil import WidgetUtil

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'forceAppLaunch': True,
    'appPackage': '',
    'appActivity': ''
}
desired_caps['appPackage'] = 'com.moonpi.swiftnotes'
desired_caps['appActivity'] = '.MainActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.moonpi.swiftnotes:id/newNote')))

tid = "Note2"
actions = []

newNote_button = driver.find_element(MobileBy.ID, 'com.moonpi.swiftnotes:id/newNote')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.moonpi.swiftnotes:id/newNote')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
newNote_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.moonpi.swiftnotes:id/titleEdit')))

titleEdit_input = driver.find_element(MobileBy.ID, 'com.moonpi.swiftnotes:id/titleEdit')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.moonpi.swiftnotes:id/titleEdit')
actions.append(Util.compose(attrs, tid, ['send_keys_and_hide_keyboard', 'Title'], driver.current_package, driver.current_activity, 'gui'))
titleEdit_input.send_keys('Title')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.moonpi.swiftnotes:id/bodyEdit')))

bodyEdit_input = driver.find_element(MobileBy.ID, 'com.moonpi.swiftnotes:id/bodyEdit')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.moonpi.swiftnotes:id/bodyEdit')
actions.append(Util.compose(attrs, tid, ['send_keys_and_hide_keyboard', 'Note'], driver.current_package, driver.current_activity, 'gui'))
bodyEdit_input.send_keys('Note')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.CLASS_NAME, 'android.widget.ImageButton')))

relativeLayoutEdit_button = driver.find_element(MobileBy.CLASS_NAME, 'android.widget.ImageButton')
attrs = WidgetUtil.get_attrs(driver.page_source, 'class', 'android.widget.ImageButton')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
relativeLayoutEdit_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'android:id/button1')))

button1_button = driver.find_element(MobileBy.ID, 'android:id/button1')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'android:id/button1')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
button1_button.click()

driver.quit()

# Save events to JSON file
json_file_path = os.path.join('C:\\Users\\11303\\Desktop\\transfer', f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)
