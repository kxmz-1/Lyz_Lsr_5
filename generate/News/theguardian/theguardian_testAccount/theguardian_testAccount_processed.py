from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from WidgetUtil import WidgetUtil
from Util import Util
import os
import json
import xml.dom.minidom
tid = 'theguardian_testAccount'
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

path = 'C:\\Users\\11303\\Desktop\\generate\\News\\theguardian'
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
    'noReset' : True
}
desired_caps['appPackage'] = 'com.guardian'
desired_caps['appActivity'] = '.feature.stream.NewHomeActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)



WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.guardian:id/fabHome')))
event_0_button = driver.find_element(MobileBy.ID, 'com.guardian:id/fabHome')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.guardian:id/fabHome', event_0_button)
add_event(attrs, 'gui', ['click'])
event_0_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.guardian:id/nav_drawer_profile_button')))
event_1_button = driver.find_element(MobileBy.ID, 'com.guardian:id/nav_drawer_profile_button')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.guardian:id/nav_drawer_profile_button', event_1_button)
add_event(attrs, 'gui', ['click'])
event_1_button.click()

sleep(5)
write(i)
driver.quit()
json_file_path = os.path.join(dire, f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)


