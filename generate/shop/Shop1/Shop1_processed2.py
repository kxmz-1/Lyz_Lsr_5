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
desired_caps['appPackage'] = 'pl.com.andrzejgrzyb.shoppinglist'
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

tid = 'Shop1'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\shop'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/fab')))
write(i)
i += 1
fab_button = driver.find_element(MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/fab')
fab_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/shoppingListNameEditText')))
write(i)
i += 1
shoppingListName_input = driver.find_element(MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/shoppingListNameEditText')
shoppingListName_input.send_keys('Shopping list name')

driver.hide_keyboard()
write(i)
i += 1
WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/shoppingListDescriptionEditText')))

shoppingListDescription_input = driver.find_element(MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/shoppingListDescriptionEditText')
shoppingListDescription_input.send_keys('Description')

driver.hide_keyboard()
write(i)
i += 1
WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/addShoppingListButton')))

addShoppingList_button = driver.find_element(MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/addShoppingListButton')
addShoppingList_button.click()

sleep(5)
write(i)
driver.quit()
