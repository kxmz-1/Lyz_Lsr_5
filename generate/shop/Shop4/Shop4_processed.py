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
desired_caps['appPackage'] = 'org.openintents.shopping'
desired_caps['appActivity'] = '.ShoppingActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.CLASS_NAME, 'android.widget.ImageButton')))

tid = 'Shop4'
actions = []

ImageButton_button = driver.find_element(MobileBy.CLASS_NAME, 'android.widget.ImageButton')
attrs = WidgetUtil.get_attrs(driver.page_source, 'class', 'android.widget.ImageButton')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
ImageButton_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.TextView[@text='新列表']")))

title_button = driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='新列表']")
attrs = WidgetUtil.get_attrs(driver.page_source, 'text', '新列表')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
title_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'org.openintents.shopping:id/edittext')))

edittext_input = driver.find_element(MobileBy.ID, 'org.openintents.shopping:id/edittext')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'org.openintents.shopping:id/edittext')
actions.append(Util.compose(attrs, tid, ['send_keys', 'wishlist family list'], driver.current_package, driver.current_activity, 'gui'))
edittext_input.send_keys('wishlist family list')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'android:id/button1')))

button1_button = driver.find_element(MobileBy.ID, 'android:id/button1')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'android:id/button1')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
button1_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, "android:id/text1")))

button = driver.find_element(MobileBy.ID, "android:id/text1")
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'android:id/text1')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
button.click()

sleep(5)
element_text = '我的购物列表'
element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                              'new UiSelector().text("{}")'.format(element_text))
attrs = WidgetUtil.get_attrs(driver.page_source, 'text', '我的购物列表')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
# 进行操作或断言
element.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'org.openintents.shopping:id/button_add_item')))

button_add_item_button = driver.find_element(MobileBy.ID, 'org.openintents.shopping:id/button_add_item')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'org.openintents.shopping:id/button_add_item')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
button_add_item_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'org.openintents.shopping:id/button1')))

button1_button = driver.find_element(MobileBy.ID, 'org.openintents.shopping:id/button1')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'org.openintents.shopping:id/button1')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
button1_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'org.openintents.shopping:id/autocomplete_add_item')))

autocomplete_add_item_input = driver.find_element(MobileBy.ID, 'org.openintents.shopping:id/autocomplete_add_item')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'org.openintents.shopping:id/autocomplete_add_item')
actions.append(Util.compose(attrs, tid, ['send_keys', '123'], driver.current_package, driver.current_activity, 'gui'))
autocomplete_add_item_input.send_keys('123')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'org.openintents.shopping:id/button_add_item')))

button_add_item_button = driver.find_element(MobileBy.ID, 'org.openintents.shopping:id/button_add_item')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'org.openintents.shopping:id/button_add_item')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
button_add_item_button.click()

driver.quit()

# Save events to JSON file
json_file_path = os.path.join('C:\\Users\\11303\\Desktop\\transfer', f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)
