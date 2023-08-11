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
desired_caps['appPackage'] = 'com.kvannli.simonkvannli.dailybudget'
desired_caps['appActivity'] = '.MainActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.CLASS_NAME, 'android.widget.ImageButton')))

tid = "Expanse3"
actions = []

ImageButton_button = driver.find_element(MobileBy.CLASS_NAME, 'android.widget.ImageButton')
attrs = WidgetUtil.get_attrs(driver.page_source, 'class', 'android.widget.ImageButton')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
ImageButton_button.click()

sleep(10)

class_button = driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='INCOME']")
attrs = WidgetUtil.get_attrs(driver.page_source, 'text', "INCOME")
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
class_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/editText')))

editText_input = driver.find_element(MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/editText')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.kvannli.simonkvannli.dailybudget:id/editText')
actions.append(Util.compose(attrs, tid, ['send_keys_and_hide_keyboard', 'Name'], driver.current_package, driver.current_activity, 'gui'))
editText_input.send_keys('Name')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/editText2')))

editText2_input = driver.find_element(MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/editText2')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.kvannli.simonkvannli.dailybudget:id/editText2')
actions.append(Util.compose(attrs, tid, ['send_keys_and_hide_keyboard', 80], driver.current_package, driver.current_activity, 'gui'))
editText2_input.send_keys(80)

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/button2')))

button2_button = driver.find_element(MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/button2')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.kvannli.simonkvannli.dailybudget:id/button2')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
button2_button.click()

driver.quit()

# Save events to JSON file
json_file_path = os.path.join('C:\\Users\\11303\\Desktop\\transfer', f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)
