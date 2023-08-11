from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from WidgetUtil import WidgetUtil
from Configuration import Config
from Util import Util
import os
import json
import xml.dom.minidom
tid = 'home_testAccount'
actions = []
i = 0

def add_event(attrs, event_type, action):
    global i
    actions.append(Util.compose(attrs, tid, action, driver.current_package, driver.current_activity, event_type))
    write(i)
    i += 1

def write(i):
    ui_hierarchies = driver.page_source
    dom = xml.dom.minidom.parseString(ui_hierarchies)
    ui_hierarchies = dom.toprettyxml()
    file_path = os.path.join(dire, f'hierarchy{i}.xml')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(ui_hierarchies)

path = 'C:\\Users\\11303\\Desktop\\generate\\shop2\\home'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5556',
    'automationName': 'UiAutomator2',
    'forceAppLaunch': True,
    'appPackage': '',
    'appActivity': '',
    'noReset' : False
}
desired_caps['appPackage'] = 'com.contextlogic.home'
desired_caps['appActivity'] = 'com.contextlogic.wish.activity.browse.BrowseActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)


WebDriverWait(driver, 30).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.home:id/sign_in_fragment_email_text')))
event_1_input = driver.find_element(MobileBy.ID, 'com.contextlogic.home:id/sign_in_fragment_email_text')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id',  'com.contextlogic.home:id/sign_in_fragment_email_text', event_1_input)
add_event(attrs, 'gui',  ['send_keys',Config.user_email])
event_1_input.send_keys(Config.user_email)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.home:id/sign_in_fragment_password_text')))

event_2_input = driver.find_element(MobileBy.ID, 'com.contextlogic.home:id/sign_in_fragment_password_text')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id',  'com.contextlogic.home:id/sign_in_fragment_password_text', event_2_input)
add_event(attrs, 'gui',  ['send_keys', Config.email_password])
event_2_input.send_keys(Config.email_password)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.home:id/sign_in_fragment_sign_in_button')))
event_3_button = driver.find_element(MobileBy.ID, 'com.contextlogic.home:id/sign_in_fragment_sign_in_button')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id',  'com.contextlogic.home:id/sign_in_fragment_sign_in_button', event_3_button)
add_event(attrs, 'gui',  ["click"])
event_3_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="Open Menu"]')))
event_4_button = driver.find_element(MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="Open Menu"]')
attrs = WidgetUtil.get_attrs(driver.page_source, 'content-desc',  "Open Menu", event_4_button)
add_event(attrs, 'gui',  ["click"])
event_4_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.home:id/menu_view_profile_arrow')))
event_5_button = driver.find_element(MobileBy.ID, 'com.contextlogic.home:id/menu_view_profile_arrow')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id',  'com.contextlogic.home:id/menu_view_profile_arrow', event_4_button)
add_event(attrs, 'gui',  ["click"])
event_5_button.click()

sleep(5)
write(i)

driver.quit()

json_file_path = os.path.join(dire, f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)


