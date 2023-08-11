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
desired_caps['appPackage'] = 'com.kvannli.simonkvannli.dailybudget'
desired_caps['appActivity'] = '.MainActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.CLASS_NAME, 'android.widget.ImageButton')))

ImageButton_button = driver.find_element(MobileBy.CLASS_NAME, 'android.widget.ImageButton')
ImageButton_button.click()

class_button = driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='INCOME']")
class_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/editText')))

editText_input = driver.find_element(MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/editText')
editText_input.send_keys('Name')

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/editText2')))

editText2_input = driver.find_element(MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/editText2')
editText2_input.send_keys(80)

driver.hide_keyboard()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/button2')))

button2_button = driver.find_element(MobileBy.ID, 'com.kvannli.simonkvannli.dailybudget:id/button2')
button2_button.click()

driver.quit()

