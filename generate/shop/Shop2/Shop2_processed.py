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
desired_caps['appPackage'] = 'br.com.activity'
desired_caps['appActivity'] = 'br.com.vansact.MainApp'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'br.com.activity:id/action_add')))

tid = 'Shop2'
actions = []

action_add_button = driver.find_element(MobileBy.ID, 'br.com.activity:id/action_add')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'br.com.activity:id/action_add')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
action_add_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.CLASS_NAME, 'android.widget.EditText')))

EditText_button = driver.find_element(MobileBy.CLASS_NAME, 'android.widget.EditText')
attrs = WidgetUtil.get_attrs(driver.page_source, 'class', 'android.widget.EditText')
actions.append(Util.compose(attrs, tid, ['send_keys', 'Title'], driver.current_package, driver.current_activity, 'gui'))
EditText_button.send_keys('Title')

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'android:id/button1')))

button1_button = driver.find_element(MobileBy.ID, 'android:id/button1')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'android:id/button1')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
button1_button.click()

driver.quit()

# Save events to JSON file
json_file_path = os.path.join('C:\\Users\\11303\\Desktop\\generate\\shop\\Shop2', f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)
