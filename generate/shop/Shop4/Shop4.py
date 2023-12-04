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
desired_caps['appPackage'] = 'org.openintents.shopping'
desired_caps['appActivity'] = '.ShoppingActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.CLASS_NAME, 'android.widget.ImageButton')))

ImageButton_button = driver.find_element(MobileBy.CLASS_NAME, 'android.widget.ImageButton')
ImageButton_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.XPATH,  "//android.widget.TextView[@text='新列表']")))

title_button = driver.find_element(MobileBy.XPATH,  "//android.widget.TextView[@text='新列表']")
title_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'org.openintents.shopping:id/edittext')))

edittext_input = driver.find_element(MobileBy.ID, 'org.openintents.shopping:id/edittext')
edittext_input.send_keys('wishlist family list')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'android:id/button1')))

button1_button = driver.find_element(MobileBy.ID, 'android:id/button1')
button1_button.click()

driver.quit()
