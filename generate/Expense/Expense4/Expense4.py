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
desired_caps['appPackage'] = 'com.blogspot.e_kanivets.moneytracker'
desired_caps['appActivity'] = '.activity.record.MainActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/btn_add_income')))

btn_add_income_button = driver.find_element(MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/btn_add_income')
btn_add_income_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_done')))

action_done_button = driver.find_element(MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_done')
action_done_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/et_price')))

et_price_input = driver.find_element(MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/et_price')
et_price_input.send_keys('30')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_done')))

action_done_button = driver.find_element(MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_done')
action_done_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/et_title')))

et_title_input = driver.find_element(MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/et_title')
et_title_input.send_keys('水果')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/et_category')))

et_category_input = driver.find_element(MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/et_category')
et_category_input.send_keys('饮食')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_done')))

action_done_button = driver.find_element(MobileBy.ID, 'com.blogspot.e_kanivets.moneytracker:id/action_done')
action_done_button.click()

driver.quit()
