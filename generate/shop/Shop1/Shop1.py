from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

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

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/fab')))

fab_button = driver.find_element(MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/fab')
fab_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/shoppingListNameEditText')))

shoppingListName_input = driver.find_element(MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/shoppingListNameEditText')
shoppingListName_input.send_keys('Shopping list name')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/shoppingListDescriptionEditText')))

shoppingListDescription_input = driver.find_element(MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/shoppingListDescriptionEditText')
shoppingListDescription_input.send_keys('Description')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/addShoppingListButton')))

addShoppingList_button = driver.find_element(MobileBy.ID, 'pl.com.andrzejgrzyb.shoppinglist:id/addShoppingListButton')
addShoppingList_button.click()

driver.quit()
