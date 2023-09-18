from Configuration import Config
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import json

import WidgetUtil
# local import
from Util import Util

from WidgetUtil import WidgetUtil

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from Configuration import Config

actions = []
tid = "5miles_testMenu"

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'forceAppLaunch': True,
    'appPackage': '',
    'appActivity': ''
}
desired_caps['appPackage'] = 'com.thirdrock.fivemiles'
desired_caps['appActivity'] = 'com.insthub.fivemiles.Activity.GuidePagerActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/sign_in')))

event_0_button = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/sign_in')
attrs = WidgetUtil.get_attrs(driver.page_source, event_0_button)
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
event_0_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/login_email')))

event_1_input = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/login_email')
attrs = WidgetUtil.get_attrs(driver.page_source, event_1_input)
actions.append(Util.compose(attrs, tid, ['send_keys', Config.user_email], driver.current_package, driver.current_activity, 'gui'))
event_1_input.send_keys(Config.user_email)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/login_password')))

event_2_input = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/login_password')
attrs = WidgetUtil.get_attrs(driver.page_source, event_2_input)
actions.append(Util.compose(attrs, tid, ['send_keys', Config.email_password], driver.current_package, driver.current_activity, 'gui'))
event_2_input.send_keys(Config.email_password)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/login_login')))

event_3_button = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/login_login')
attrs = WidgetUtil.get_attrs(driver.page_source, event_3_button)
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
event_3_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/btn_skip')))
event_3_button = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/btn_skip')
attrs = WidgetUtil.get_attrs(driver.page_source, event_3_button)
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
event_3_button.click()

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')))
event_6_button = driver.find_element(MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
attrs = WidgetUtil.get_attrs(driver.page_source, event_6_button)
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
event_6_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.XPATH,
                                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView')))
event_3_button = driver.find_element(MobileBy.XPATH,
                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView')
attrs = WidgetUtil.get_attrs(driver.page_source, event_3_button)
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
event_3_button.click()

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/action_profile')))

event_4_button = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/action_profile')
attrs = WidgetUtil.get_attrs(driver.page_source, event_4_button)
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
event_4_button.click()

driver.quit()



# Save events to JSON file
json_file_path = os.path.join('C:\\Users\\11303\\Desktop\\generate\\shop2\\5miles', f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)
