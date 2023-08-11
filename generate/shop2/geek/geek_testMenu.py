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
desired_caps['appPackage'] = 'com.contextlogic.geek'
desired_caps['appActivity'] = 'com.contextlogic.wish.activity.browse.BrowseActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.geek:id/login_fragment_sign_in_button')))

event_0_button = driver.find_element(MobileBy.ID, 'com.contextlogic.geek:id/login_fragment_sign_in_button')
event_0_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.geek:id/sign_in_fragment_email_text')))

event_1_input = driver.find_element(MobileBy.ID, 'com.contextlogic.geek:id/sign_in_fragment_email_text')
event_1_input.send_keys(Config.user_email)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.geek:id/sign_in_fragment_password_text')))

event_2_input = driver.find_element(MobileBy.ID, 'com.contextlogic.geek:id/sign_in_fragment_password_text')
event_2_input.send_keys(Config.email_password)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.geek:id/sign_in_fragment_sign_in_button')))

event_3_button = driver.find_element(MobileBy.ID, 'com.contextlogic.geek:id/sign_in_fragment_sign_in_button')
event_3_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="Open Menu"]')))

event_4_button = driver.find_element(MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="Open Menu"]')
event_4_button.click()

driver.quit()
