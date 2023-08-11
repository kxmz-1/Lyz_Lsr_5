from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

tid = 'abc_testAbout'
actions = []
def add_event(attrs, event_type, action):
    global i
    actions.append(Util.compose(attrs, tid, action, driver.current_package, driver.current_activity, event_type))
    write(i)
    i += 1
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'forceAppLaunch': True,
    'appPackage': '',
    'appActivity': ''
}
desired_caps['appPackage'] = 'com.usatoday.android.news'
desired_caps['appActivity'] = 'com.gannett.android.news.ActivityLoading'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.usatoday.android.news:id/settings_gear')))
event_0_button = driver.find_element(MobileBy.ID, 'com.usatoday.android.news:id/settings_gear')
attrs = WidgetUtil.get_attrs(driver.page_source, 'resource-id', 'com.usatoday.android.news:id/settings_gear', event_0_button)
add_event(attrs, 'gui', ['click'])
event_0_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.usatoday.android.news:id/preference_layout')))
event_1_button = driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[7]')
attrs = WidgetUtil.get_attrs(driver.page_source, 'index', 0, event_1_button)
add_event(attrs, 'gui', ['click'])
event_1_button.click()


sleep(10)
write(i)

driver.quit()
json_file_path = os.path.join(dire, f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)