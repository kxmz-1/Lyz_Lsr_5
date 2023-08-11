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
desired_caps['appPackage'] = 'com.moonpi.swiftnotes'
desired_caps['appActivity'] = '.MainActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.moonpi.swiftnotes:id/newNote')))

newNote_button = driver.find_element(MobileBy.ID, 'com.moonpi.swiftnotes:id/newNote')
newNote_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.moonpi.swiftnotes:id/titleEdit')))

titleEdit_input = driver.find_element(MobileBy.ID, 'com.moonpi.swiftnotes:id/titleEdit')
titleEdit_input.send_keys('Title')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.moonpi.swiftnotes:id/bodyEdit')))

bodyEdit_input = driver.find_element(MobileBy.ID, 'com.moonpi.swiftnotes:id/bodyEdit')
bodyEdit_input.send_keys('Note')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.CLASS_NAME, 'android.widget.ImageButton')))

relativeLayoutEdit_button = driver.find_element(MobileBy.CLASS_NAME, 'android.widget.ImageButton')
relativeLayoutEdit_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'android:id/button1')))

button1_button = driver.find_element(MobileBy.ID, 'android:id/button1')
button1_button.click()

driver.quit()
