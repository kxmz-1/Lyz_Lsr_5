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
desired_caps['appPackage'] = 'pl.com.andrzejgrzyb.shoppinglist'
desired_caps['appActivity'] = '.MainActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/fab')))

tid = 'Shop1'
actions = []

fab_button = driver.find_element(MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/fab')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'pl.com.andrzejgrzyb.shoppinglist:id/fab')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
fab_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/shoppingListNameEditText')))

shoppingListName_input = driver.find_element(MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/shoppingListNameEditText')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'pl.com.andrzejgrzyb.shoppinglist:id/shoppingListNameEditText')
actions.append(Util.compose(attrs, tid, ['send_keys_and_hide_keyboard', 'Shopping list name'], driver.current_package, driver.current_activity, 'gui'))
shoppingListName_input.send_keys('Shopping list name')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/shoppingListDescriptionEditText')))

shoppingListDescription_input = driver.find_element(MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/shoppingListDescriptionEditText')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'pl.com.andrzejgrzyb.shoppinglist:id/shoppingListDescriptionEditText')
actions.append(Util.compose(attrs, tid, ['send_keys_and_hide_keyboard', 'Description'], driver.current_package, driver.current_activity, 'gui'))
shoppingListDescription_input.send_keys('Description')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/addShoppingListButton')))

addShoppingList_button = driver.find_element(MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/addShoppingListButton')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'pl.com.andrzejgrzyb.shoppinglist:id/addShoppingListButton')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
addShoppingList_button.click()

driver.quit()

# Save events to JSON file
json_file_path = os.path.join('C:\\Users\\11303\\Desktop\\transfer', f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)
