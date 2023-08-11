from Configuration import Config
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
desired_caps['appPackage'] = 'com.thirdrock.fivemiles'
desired_caps['appActivity'] = 'com.insthub.fivemiles.Activity.GuidePagerActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/sign_up')))

event_0_button = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/sign_up')
event_0_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/login_first_name')))

event_1_input = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/login_first_name')
event_1_input.send_keys(Config.first_name)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/login_last_name')))

event_2_input = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/login_last_name')
event_2_input.send_keys(Config.last_name)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/login_email')))

event_3_input = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/login_email')
event_3_input.send_keys(Config.user_email)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/login_password')))

event_4_input = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/login_password')
event_4_input.send_keys(Config.email_password)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.thirdrock.fivemiles:id/register_register')))

event_5_button = driver.find_element(MobileBy.ID, 'com.thirdrock.fivemiles:id/register_register')
event_5_button.click()

driver.quit()
