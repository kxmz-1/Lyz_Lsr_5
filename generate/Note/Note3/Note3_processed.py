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
desired_caps['appPackage'] = 'me.writeily'
desired_caps['appActivity'] = '.PromptPinActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'me.writeily:id/fab_expand_menu_button')))

tid = 'Note3'
actions = []

fab_expand_menu_button_button = driver.find_element(MobileBy.ID, 'me.writeily:id/fab_expand_menu_button')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'me.writeily:id/fab_expand_menu_button')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
fab_expand_menu_button_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'me.writeily:id/create_note')))

create_note_button = driver.find_element(MobileBy.ID, 'me.writeily:id/create_note')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'me.writeily:id/create_note')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
create_note_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'me.writeily:id/edit_note_title')))

edit_note_title_input = driver.find_element(MobileBy.ID, 'me.writeily:id/edit_note_title')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'me.writeily:id/edit_note_title')
actions.append(Util.compose(attrs, tid, ['send_keys_and_hide_keyboard', 'Title'], driver.current_package, driver.current_activity, 'gui'))
edit_note_title_input.send_keys('Title')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'me.writeily:id/note_content')))

note_content_input = driver.find_element(MobileBy.ID, 'me.writeily:id/note_content')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'me.writeily:id/note_content')
actions.append(Util.compose(attrs, tid, ['send_keys_and_hide_keyboard', 'abcde'], driver.current_package, driver.current_activity, 'gui'))
note_content_input.send_keys('abcde')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.CLASS_NAME, 'android.widget.ImageButton')))

ImageButton_button = driver.find_element(MobileBy.CLASS_NAME, 'android.widget.ImageButton')
attrs = WidgetUtil.get_attrs(driver.page_source, 'class', 'android.widget.ImageButton')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
ImageButton_button.click()

driver.quit()

# Save events to JSON file
json_file_path = os.path.join('C:\\Users\\11303\\Desktop\\transfer', f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)
