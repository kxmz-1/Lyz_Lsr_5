from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import xml.dom.minidom
import os

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "forceAppLaunch": True,
    "appPackage": "",
    "appActivity": ""
}
desired_caps['appPackage'] = 'luankevinferreira.expenses'
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

tid = 'Expense2'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\Expense'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'luankevinferreira.expenses:id/fab')))

write(i)
i += 1
fab_button = driver.find_element(MobileBy.ID, 'luankevinferreira.expenses:id/fab')
fab_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'luankevinferreira.expenses:id/expense_value')))
write(i)
i += 1
expense_value_input = driver.find_element(MobileBy.ID, 'luankevinferreira.expenses:id/expense_value')
expense_value_input.send_keys('3.50')
driver.press_keycode(66)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'luankevinferreira.expenses:id/expense_description')))
write(i)
i += 1
expense_description_input = driver.find_element(MobileBy.ID, 'luankevinferreira.expenses:id/expense_description')
expense_description_input.send_keys('Fruit')

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'luankevinferreira.expenses:id/date_picker')))
write(i)
i += 1
date_picker_button = driver.find_element(MobileBy.ID, 'luankevinferreira.expenses:id/date_picker')
date_picker_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'android:id/button1')))
write(i)
i += 1
button1_button = driver.find_element(MobileBy.ID, 'android:id/button1')
button1_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'luankevinferreira.expenses:id/save_expense')))
write(i)
i += 1
save_expense_button = driver.find_element(MobileBy.ID, 'luankevinferreira.expenses:id/save_expense')
save_expense_button.click()

sleep(10)
write(i)
driver.quit()
