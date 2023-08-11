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
desired_caps['appPackage'] = 'chan.android.app.pocketnote'
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

tid = 'Note4'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\Note'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'chan.android.app.pocketnote:id/notes_$_linearlayout_empty')))
write(i)
i += 1
linearlayout_empty_button = driver.find_element(MobileBy.ID, 'chan.android.app.pocketnote:id/notes_$_linearlayout_empty')
linearlayout_empty_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'chan.android.app.pocketnote:id/editor_$_edittext_title')))
write(i)
i += 1
edittext_title_input = driver.find_element(MobileBy.ID, 'chan.android.app.pocketnote:id/editor_$_edittext_title')
edittext_title_input.send_keys('abc')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'chan.android.app.pocketnote:id/editor_$_note_editor')))
write(i)
i += 1
note_editor_input = driver.find_element(MobileBy.ID, 'chan.android.app.pocketnote:id/editor_$_note_editor')
note_editor_input.send_keys('abc')

driver.hide_keyboard()

sleep(5)
write(i)

driver.quit()



