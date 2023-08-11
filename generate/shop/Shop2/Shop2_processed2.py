from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import xml.dom.minidom
import os

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'forceAppLaunch': True,
    'appPackage': '',
    'appActivity': ''
}
desired_caps['appPackage'] = 'br.com.activity'
desired_caps['appActivity'] = 'br.com.vansact.MainApp'

driver = webdriver.Remote('http://localhost:4723', desired_caps)
i=0

def write(i):
    ui_hierarchies = driver.page_source
    dom = xml.dom.minidom.parseString(ui_hierarchies)
    ui_hierarchies = dom.toprettyxml()
    file_path = os.path.join(dire, f'hierarchy{i}.xml')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(ui_hierarchies)

tid = 'Shop2'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\shop'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'br.com.activity:id/action_add')))
write(i)
i += 1
action_add_button = driver.find_element(MobileBy.ID, 'br.com.activity:id/action_add')
action_add_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.CLASS_NAME, 'android.widget.EditText')))
write(i)
i += 1
EditText_button = driver.find_element(MobileBy.CLASS_NAME, 'android.widget.EditText')
EditText_button.send_keys('Title')

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'android:id/button1')))
write(i)
i += 1
button1_button = driver.find_element(MobileBy.ID, 'android:id/button1')
button1_button.click()

sleep(5)
write(i)

driver.quit()