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
desired_caps['appPackage'] = 'chan.android.app.pocketnote'
desired_caps['appActivity'] = '.MainActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'chan.android.app.pocketnote:id/notes_$_linearlayout_empty')))

tid = 'Note4'
actions = []

linearlayout_empty_button = driver.find_element(MobileBy.ID, 'chan.android.app.pocketnote:id/notes_$_linearlayout_empty')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'chan.android.app.pocketnote:id/notes_$_linearlayout_empty')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
linearlayout_empty_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'chan.android.app.pocketnote:id/editor_$_edittext_title')))

edittext_title_input = driver.find_element(MobileBy.ID, 'chan.android.app.pocketnote:id/editor_$_edittext_title')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'chan.android.app.pocketnote:id/editor_$_edittext_title')
actions.append(Util.compose(attrs, tid, ['send_keys_and_hide_keyboard', 'abc'], driver.current_package, driver.current_activity, 'gui'))
edittext_title_input.send_keys('abc')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'chan.android.app.pocketnote:id/editor_$_note_editor')))

note_editor_input = driver.find_element(MobileBy.ID, 'chan.android.app.pocketnote:id/editor_$_note_editor')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'chan.android.app.pocketnote:id/editor_$_note_editor')
actions.append(Util.compose(attrs, tid, ['send_keys_and_hide_keyboard', 'abc'], driver.current_package, driver.current_activity, 'gui'))
note_editor_input.send_keys('abc')

driver.hide_keyboard()

driver.quit()

# Save events to JSON file
json_file_path = os.path.join('C:\\Users\\11303\\Desktop\\transfer', f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)
