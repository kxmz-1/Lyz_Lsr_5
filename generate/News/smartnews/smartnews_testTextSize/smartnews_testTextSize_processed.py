from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import json
from Util import Util
from WidgetUtil import WidgetUtil
import os
import json
import xml.dom.minidom

tid = 'smartnews_testTextSize'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\News\\smartnews'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'forceAppLaunch': True,
    'appPackage': 'jp.gocro.smartnews.android',
    'appActivity': 'activity.SmartNewsActivity',
    'noReset': True
}

driver = webdriver.Remote('http://localhost:4723', desired_caps)
i = 0

def write(i):
    ui_hierarchies = driver.page_source
    dom = xml.dom.minidom.parseString(ui_hierarchies)
    ui_hierarchies = dom.toprettyxml()
    file_path = os.path.join(dire, f'hierarchy{i}.xml')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(ui_hierarchies)

actions = []

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'jp.gocro.smartnews.android:id/settingButton')))
write(i)
i += 1
# Event 0: Click on 'settingButton'
event_0_button = driver.find_element(MobileBy.ID, 'jp.gocro.smartnews.android:id/settingButton')
attrs_0 = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'jp.gocro.smartnews.android:id/settingButton')
action_0 = Util.compose(attrs_0, tid, ['click'], driver.current_package, driver.current_activity, 'gui')
actions.append(action_0)
event_0_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[3]')))
write(i)
i += 1
# Event 1: Click on specific element
event_1_button = driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[3]')
attrs_1 = WidgetUtil.get_attrs(driver.page_source, 'index', 3)
action_1 = Util.compose(attrs_1, tid, ['click'], driver.current_package, driver.current_activity, 'gui')
actions.append(action_1)
event_1_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'android:id/text1')))
write(i)
i += 1
# Event 2: Click on 'android:id/text1'
event_2_button = driver.find_element(MobileBy.ID, 'android:id/text1')
attrs_2 = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'android:id/text1')
action_2 = Util.compose(attrs_2, tid, ['click'], driver.current_package, driver.current_activity, 'gui')
actions.append(action_2)
event_2_button.click()

sleep(5)
write(i)
i += 1
driver.quit()

# Save events to JSON file
json_file_path = os.path.join(dire, f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)

