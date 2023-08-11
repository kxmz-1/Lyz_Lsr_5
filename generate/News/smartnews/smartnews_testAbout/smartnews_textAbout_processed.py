from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import json
import xml.dom.minidom
from Util import Util
from WidgetUtil import WidgetUtil

tid = 'smartnews_testAbout'
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

# Event 0: Click on 'settingButton'
sleep(10)
write(i)
i += 1
event_0_button = driver.find_element(MobileBy.ID, 'jp.gocro.smartnews.android:id/settingButton')
event_0_attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'jp.gocro.smartnews.android:id/settingButton')
actions.append(Util.compose(event_0_attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
event_0_button.click()

# Function for swipe down
def swipe_down():
    global i
    write(i)
    i += 1
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    start_x = width // 2
    start_y = height // 2
    end_x = width // 2
    end_y = 0
    driver.swipe(start_x, start_y, end_x, end_y)
    swipe_attrs = {
        "action": ["swipe"],
        "event_type": "gui",
        "tid": tid,
        "package": driver.current_package,
        "activity": driver.current_activity
    }
    actions.append(swipe_attrs)

# Swipe down three times
for _ in range(1):
    swipe_down()
    # Save XML hierarchy file

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[7]')))
write(i)
i += 1
# Event 1: Click on a specific element
event_1_button = driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[7]")
event_1_attrs = WidgetUtil.get_attrs(driver.page_source, 'index',8)
actions.append(Util.compose(event_1_attrs, tid, ['click'], driver.current_package, driver.current_activity, 'gui'))
event_1_button.click()
sleep(5)
write(i)
i += 1
driver.quit()

# Save events to JSON file
json_file_path = os.path.join(dire, f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)

