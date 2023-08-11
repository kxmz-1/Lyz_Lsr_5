from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import json
import xml.dom.minidom

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'forceAppLaunch': True,
    'appPackage': '',
    'appActivity': ''
}
desired_caps['appPackage'] = 'com.blogspot.e_kanivets.moneytracker'
desired_caps['appActivity'] = '.activity.record.MainActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)
driver.implicitly_wait(10)

tid = 'Expense4'
actions = []
i = 0

def write(i):
    ui_hierarchies = driver.page_source
    dom = xml.dom.minidom.parseString(ui_hierarchies)
    ui_hierarchies = dom.toprettyxml()
    file_path = os.path.join(dire, f'hierarchy{i}.xml')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(ui_hierarchies)

path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\Expense'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/btn_add_income')))
write(i)
i += 1
btn_add_income_button = driver.find_element(MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/btn_add_income')
btn_add_income_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_done')))
write(i)
i += 1
action_done_button = driver.find_element(MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_done')
action_done_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/et_price')))
write(i)
i += 1
et_price_input = driver.find_element(MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/et_price')
et_price_input.send_keys('30')
driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_done')))
write(i)
i += 1
action_done_button = driver.find_element(MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_done')
action_done_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/et_title')))
write(i)
i += 1
et_title_input = driver.find_element(MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/et_title')
et_title_input.send_keys('水果')
driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/et_category')))
write(i)
i += 1
et_category_input = driver.find_element(MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/et_category')
et_category_input.send_keys('饮食')
driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_done')))
write(i)
i += 1
action_done_button = driver.find_element(MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_done')
action_done_button.click()

sleep(10)
write(i)
driver.quit()

# Save events to JSON file
json_file_path = os.path.join('C:\\Users\\11303\\Desktop\\transfer', f'{tid}.json')
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(actions, file, ensure_ascii=False, indent=4)
