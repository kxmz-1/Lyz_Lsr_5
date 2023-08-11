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
desired_caps['appPackage'] = 'com.benoitletondor.easybudgetapp'
desired_caps['appActivity'] = '.view.MainActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/onboarding_screen1_next_button')))

tid = os.path.basename(__file__).split('.')[0]
actions = []

onboarding_screen1_next_button_button = driver.find_element(MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/onboarding_screen1_next_button')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.benoitletondor.easybudgetapp:id/onboarding_screen1_next_button')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
onboarding_screen1_next_button_button.click()

onboarding_screen2_next_button_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/onboarding_screen2_next_button')))
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.benoitletondor.easybudgetapp:id/onboarding_screen2_next_button')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
onboarding_screen2_next_button_button.click()

onboarding_screen3_next_button_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/onboarding_screen3_next_button')))
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.benoitletondor.easybudgetapp:id/onboarding_screen3_next_button')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
onboarding_screen3_next_button_button.click()

onboarding_screen4_next_button_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/onboarding_screen4_next_button')))
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.benoitletondor.easybudgetapp:id/onboarding_screen4_next_button')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
onboarding_screen4_next_button_button.click()

fab_expand_menu_button_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/fab_expand_menu_button')))
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.benoitletondor.easybudgetapp:id/fab_expand_menu_button')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
fab_expand_menu_button_button.click()

fab_new_expense_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/fab_new_expense')))
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.benoitletondor.easybudgetapp:id/fab_new_expense')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
fab_new_expense_button.click()

description_edittext_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/description_edittext')))
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.benoitletondor.easybudgetapp:id/description_edittext')
actions.append(Util.compose(attrs, tid, ['send_keys_and_hide_keyboard', 'Food'], driver.current_package, driver.current_activity, 'gui'))
description_edittext_input.send_keys('Food')

driver.press_keycode(66)

amount_edittext_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/amount_edittext')))
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.benoitletondor.easybudgetapp:id/amount_edittext')
actions.append(Util.compose(attrs, tid, ['send_keys_and_hide_keyboard', '50'], driver.current_package, driver.current_activity, 'gui'))
amount_edittext_input.send_keys('50')

driver.press_keycode(66)

save_expense_fab_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/save_expense_fab')))
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.benoitletondor.easybudgetapp:id/save_expense_fab')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
save_expense_fab_button.click()

driver.quit()

# Save events to JSON file
json_file_path = os.path.join('C:\\Users\\11303\\Desktop\\transfer', f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)
