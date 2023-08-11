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
tid = '5miles_testAccount'
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

path = 'C:\\Users\\11303\\Desktop\\generate\\shop2\\5miles'
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
desired_caps['appPackage'] = 'com.thirdrock.fivemiles'
desired_caps['appActivity'] = 'com.insthub.fivemiles.Activity.GuidePagerActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/sign_in')))

event_0_button = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/sign_in')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.thirdrock.fivemiles:id/sign_in', event_0_button)
add_event(attrs, 'gui', ['click'])
event_0_button.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/login_email')))
event_1_input = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/login_email')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.thirdrock.fivemiles:id/login_email', event_1_input)
add_event(attrs, 'gui', ['send_keys', Config.user_email])
event_1_input.send_keys(Config.user_email)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/login_password')))
event_2_input = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/login_password')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.thirdrock.fivemiles:id/login_password', event_2_input)
add_event(attrs, 'gui', ['send_keys', Config.email_password])
event_2_input.send_keys(Config.email_password)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/login_login')))
event_3_button = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/login_login')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.thirdrock.fivemiles:id/login_login', event_3_button)
add_event(attrs, 'gui', ['click'])
event_3_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/btn_skip')))
event_3_button = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/btn_skip')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.thirdrock.fivemiles:id/btn_skip', event_3_button)
add_event(attrs, 'gui', ['click'])
event_3_button.click()

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')))
event_6_button = driver.find_element(MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
attrs = WidgetUtil.get_attrs(driver.page_source, 'content-desc', 'Navigate up', event_6_button)
add_event(attrs, 'gui', ['click'])
event_6_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.XPATH,
                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView')))
event_3_button = driver.find_element(MobileBy.XPATH,
                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.thirdrock.fivemiles:id/close', event_3_button)
add_event(attrs, 'gui', ['click'])
event_3_button.click()

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/action_profile')))

event_4_button = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/action_profile')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.thirdrock.fivemiles:id/action_profile', event_4_button)
add_event(attrs, 'gui', ['click'])
event_4_button.click()

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/profile_edit_profile')))
event_5_button = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/profile_edit_profile')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id',  'com.thirdrock.fivemiles:id/profile_edit_profile', event_5_button)
add_event(attrs, 'gui', ['click'])
event_5_button.click()
sleep(5)
write(i)

driver.quit()

json_file_path = os.path.join(dire, f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)


