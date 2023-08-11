from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import xml.dom.minidom

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'forceAppLaunch': True,
    'appPackage': '',
    'appActivity': '',
    'noReset' : True
}
desired_caps['appPackage'] = 'com.kvannli.simonkvannli.dailybudget'
desired_caps['appActivity'] = '.MainActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)
i=0

def write(i):
    ui_hierarchies = driver.page_source
    dom = xml.dom.minidom.parseString(ui_hierarchies)
    ui_hierarchies = dom.toprettyxml()
    file_path = os.path.join(dire, f'hierarchy{i}.xml')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(ui_hierarchies)

tid = 'Expense3'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\Expense'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.CLASS_NAME, 'android.widget.ImageButton')))
write(i)
i += 1
ImageButton_button = driver.find_element(MobileBy.CLASS_NAME, 'android.widget.ImageButton')
ImageButton_button.click()

class_button = driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='INCOME']")
write(i)
i += 1
class_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/editText')))
write(i)
i += 1
editText_input = driver.find_element(MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/editText')
editText_input.send_keys('Name')
driver.hide_keyboard()


WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/editText2')))
write(i)
i += 1
editText2_input = driver.find_element(MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/editText2')
editText2_input.send_keys(80)
driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/button2')))
write(i)
i += 1
button2_button = driver.find_element(MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/button2')
button2_button.click()

sleep(10)
write(i)

driver.quit()