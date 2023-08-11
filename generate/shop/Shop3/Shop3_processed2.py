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
desired_caps['appPackage'] = 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist'
desired_caps['appActivity'] = '.ui.main.SplashActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)
i = 0

def write(i):
    ui_hierarchies = driver.page_source
    dom = xml.dom.minidom.parseString(ui_hierarchies)
    ui_hierarchies = dom.toprettyxml()
    file_path = os.path.join(dire, f'hierarchy{i}.xml')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(ui_hierarchies)

tid = 'Shop3'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\shop'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/btn_skip')))
write(i)
i += 1
btn_skip_button = driver.find_element(MobileBy.ID, 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/btn_skip')
btn_skip_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/fab_new_list')))
write(i)
i += 1
fab_new_list_button = driver.find_element(MobileBy.ID, 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/fab_new_list')
fab_new_list_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/list_name')))
write(i)
i += 1
list_name_input = driver.find_element(MobileBy.ID, 'privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/list_name')
list_name_input.send_keys('Fruit')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'android:id/button1')))
write(i)
i += 1
button1_button = driver.find_element(MobileBy.ID, 'android:id/button1')
button1_button.click()

sleep(5)
write(i)
driver.quit()



