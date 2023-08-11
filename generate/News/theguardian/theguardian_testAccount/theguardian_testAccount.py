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
desired_caps['appPackage'] = 'com.guardian'
desired_caps['appActivity'] = '.feature.stream.NewHomeActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.guardian:id/fabHome')))

event_0_button = driver.find_element(MobileBy.ID, 'com.guardian:id/fabHome')
event_0_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.guardian:id/nav_drawer_profile_button')))

event_1_button = driver.find_element(MobileBy.ID, 'com.guardian:id/nav_drawer_profile_button')
event_1_button.click()

driver.quit()