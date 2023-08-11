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
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "forceAppLaunch": True,
    "appPackage": "",
    "appActivity": ""
}
desired_caps['appPackage'] = 'luankevinferreira.expenses'
desired_caps['appActivity'] = '.MainActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'luankevinferreira.expenses:id/fab')))

tid = os.path.basename(__file__).split('.')[0]
actions = []

fab_button = driver.find_element(MobileBy.ID, 'luankevinferreira.expenses:id/fab')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'luankevinferreira.expenses:id/fab')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
fab_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'luankevinferreira.expenses:id/expense_value')))

expense_value_input = driver.find_element(MobileBy.ID, 'luankevinferreira.expenses:id/expense_value')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'luankevinferreira.expenses:id/expense_value')
actions.append(Util.compose(attrs, tid, ['send_keys_and_hide_keyboard', '3.50'], driver.current_package, driver.current_activity, 'gui'))
expense_value_input.send_keys('3.50')

driver.press_keycode(66)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'luankevinferreira.expenses:id/expense_description')))

expense_description_input = driver.find_element(MobileBy.ID, 'luankevinferreira.expenses:id/expense_description')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'luankevinferreira.expenses:id/expense_description')
actions.append(Util.compose(attrs, tid, ['send_keys_and_hide_keyboard', 'Add a description'], driver.current_package, driver.current_activity, 'gui'))
expense_description_input.send_keys('Add a description')

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'luankevinferreira.expenses:id/date_picker')))

date_picker_button = driver.find_element(MobileBy.ID, 'luankevinferreira.expenses:id/date_picker')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'luankevinferreira.expenses:id/date_picker')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
date_picker_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'android:id/button1')))

button1_button = driver.find_element(MobileBy.ID, 'android:id/button1')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'android:id/button1')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
button1_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'luankevinferreira.expenses:id/save_expense')))

save_expense_button = driver.find_element(MobileBy.ID, 'luankevinferreira.expenses:id/save_expense')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'luankevinferreira.expenses:id/save_expense')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
save_expense_button.click()

driver.quit()

# Save events to JSON file
json_file_path = os.path.join('C:\\Users\\11303\\Desktop\\transfer', f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent = 4)
