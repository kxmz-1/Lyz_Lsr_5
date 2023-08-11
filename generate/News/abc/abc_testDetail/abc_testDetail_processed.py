from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import json
import xml.dom.minidom

# local import
from Util import Util
from WidgetUtil import WidgetUtil

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'forceAppLaunch': True,
    'appPackage': '',
    'appActivity': '',
    'noReset': True
}
desired_caps['appPackage'] = 'com.abc.abcnews'
desired_caps['appActivity'] = '.ui.StartActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)
driver.implicitly_wait(10)

tid = 'abc_testDetail'
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

path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\News\\abc'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.CLASS_NAME, 'android.widget.ImageButton')))
event_0_button = driver.find_element(MobileBy.CLASS_NAME, 'android.widget.ImageButton')
attrs = WidgetUtil.get_attrs(driver.page_source, 'class', 'android.widget.ImageButton')
add_event(attrs, 'gui', ['click'])
event_0_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.abc.abcnews:id/drawer_search')))
event_1_input = driver.find_element(MobileBy.ID, 'com.abc.abcnews:id/drawer_search')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.abc.abcnews:id/drawer_search')

add_event(attrs, 'gui', ['send_keys_and_enter','sanders feels the heatn'])
event_1_input.click()
sleep(5)
event_1_input.send_keys('sanders feels the heatn')
driver.execute_script("mobile: performEditorAction", {"action": "search"})


WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]')))
event_2_button = driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]')
print(driver.page_source)
attrs = WidgetUtil.get_attrs(driver.page_source, 'index', '0','android.widget.LinearLayout')
add_event(attrs, 'gui', ['click'])
event_2_button.click()


sleep(10)
write(i)

driver.quit()

json_file_path = os.path.join(dire, f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)
