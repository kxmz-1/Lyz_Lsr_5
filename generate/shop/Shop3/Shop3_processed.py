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
desired_caps['appPackage'] = 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist'
desired_caps['appActivity'] = '.ui.main.SplashActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/btn_skip')))

tid = 'Shop3'
actions = []

btn_skip_button = driver.find_element(MobileBy.ID, 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/btn_skip')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/btn_skip')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
btn_skip_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/fab_new_list')))

fab_new_list_button = driver.find_element(MobileBy.ID, 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/fab_new_list')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/fab_new_list')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
fab_new_list_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/list_name')))

list_name_input = driver.find_element(MobileBy.ID, 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/list_name')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/list_name')
actions.append(Util.compose(attrs, tid, ['send_keys', 'Fruit'], driver.current_package, driver.current_activity, 'gui'))
list_name_input.send_keys('Fruit')

driver.hide_keyboard()

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
