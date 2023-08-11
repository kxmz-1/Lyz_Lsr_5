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
desired_caps['appPackage'] = 'me.writeily'
desired_caps['appActivity'] = '.PromptPinActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)
i=0

def write(i):
    ui_hierarchies = driver.page_source
    dom = xml.dom.minidom.parseString(ui_hierarchies)
    ui_hierarchies = dom.toprettyxml()
    file_path = os.path.join(dire, f'hierarchy{i}.xml')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(ui_hierarchies)

tid = 'Note3'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\Note'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'me.writeily:id/fab_expand_menu_button')))
write(i)
i += 1
fab_expand_menu_button_button = driver.find_element(MobileBy.ID, 'me.writeily:id/fab_expand_menu_button')
fab_expand_menu_button_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'me.writeily:id/create_note')))
write(i)
i += 1
create_note_button = driver.find_element(MobileBy.ID, 'me.writeily:id/create_note')
create_note_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'me.writeily:id/edit_note_title')))
write(i)
i += 1
edit_note_title_input = driver.find_element(MobileBy.ID, 'me.writeily:id/edit_note_title')
edit_note_title_input.send_keys('Title')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'me.writeily:id/note_content')))
write(i)
i += 1
note_content_input = driver.find_element(MobileBy.ID, 'me.writeily:id/note_content')
note_content_input.send_keys('abcde')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.CLASS_NAME, 'android.widget.ImageButton')))
write(i)
i += 1
ImageButton_button = driver.find_element(MobileBy.CLASS_NAME, 'android.widget.ImageButton')
ImageButton_button.click()

sleep(5)
write(i)
driver.quit()


