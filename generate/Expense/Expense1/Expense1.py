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
desired_caps['appPackage'] = 'com.benoitletondor.easybudgetapp'
desired_caps['appActivity'] = '.view.MainActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/onboarding_screen1_next_button')))

onboarding_screen1_next_button_button = driver.find_element(MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/onboarding_screen1_next_button')
onboarding_screen1_next_button_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/onboarding_screen2_next_button')))

onboarding_screen2_next_button_button = driver.find_element(MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/onboarding_screen2_next_button')
onboarding_screen2_next_button_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/onboarding_screen3_next_button')))

onboarding_screen3_next_button_button = driver.find_element(MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/onboarding_screen3_next_button')
onboarding_screen3_next_button_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/onboarding_screen4_next_button')))

onboarding_screen4_next_button_button = driver.find_element(MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/onboarding_screen4_next_button')
onboarding_screen4_next_button_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/fab_expand_menu_button')))

fab_expand_menu_button_button = driver.find_element(MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/fab_expand_menu_button')
fab_expand_menu_button_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/fab_new_expense')))

fab_new_expense_button = driver.find_element(MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/fab_new_expense')
fab_new_expense_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/description_edittext')))

description_edittext_input = driver.find_element(MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/description_edittext')
description_edittext_input.send_keys('Food')

driver.press_keycode(66)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/amount_edittext')))

amount_edittext_input = driver.find_element(MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/amount_edittext')
amount_edittext_input.send_keys('50')

driver.press_keycode(66)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/save_expense_fab')))

save_expense_fab_button = driver.find_element(MobileBy.ID, 'com.benoitletondor.easybudgetapp:id/save_expense_fab')
save_expense_fab_button.click()

driver.quit()
