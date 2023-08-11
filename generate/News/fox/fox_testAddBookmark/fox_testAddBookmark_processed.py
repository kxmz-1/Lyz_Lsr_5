from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import xml.dom.minidom
import os
import json

# local import
from Util import Util
from WidgetUtil import WidgetUtil
def write(i):
    ui_hierarchies = driver.page_source
    dom = xml.dom.minidom.parseString(ui_hierarchies)
    ui_hierarchies = dom.toprettyxml()
    file_path = os.path.join(dire, f'hierarchy{i}.xml')
    i += 1
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(ui_hierarchies)
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\News\\fox'
tid = 'fox_testAddBookmark'
i = 0
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'forceAppLaunch': True,
    'appPackage': '',
    'appActivity': '',
    'noReset' : True
}
desired_caps['appPackage'] = 'com.foxnews.android'
desired_caps['appActivity'] = '.corenav.StartActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.foxnews.android:id/big_top_item_container')))

tid = 'fox_testSave'
actions = []

write(i)
i+=1

event_0_button = driver.find_element(MobileBy.ID, 'com.foxnews.android:id/big_top_item_container')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.foxnews.android:id/big_top_item_container')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
event_0_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.foxnews.android:id/save')))

write(i)
i+=1
event_1_button = driver.find_element(MobileBy.ID, 'com.foxnews.android:id/save')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.foxnews.android:id/save')
actions.append(Util.compose(attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
event_1_button.click()
sleep(5)

write(i)
i+=1
driver.quit()

# Save actions to JSON file
json_file_path = os.path.join(dire, f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)
