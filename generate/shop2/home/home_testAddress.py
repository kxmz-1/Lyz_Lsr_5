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
desired_caps['appPackage'] = 'com.contextlogic.home'
desired_caps['appActivity'] = 'com.contextlogic.wish.activity.browse.BrowseActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.home:id/sign_in_fragment_email_text')))

event_1_input = driver.find_element(MobileBy.ID, 'com.contextlogic.home:id/sign_in_fragment_email_text')
event_1_input.send_keys(Config.user_email)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.home:id/sign_in_fragment_password_text')))

event_2_input = driver.find_element(MobileBy.ID, 'com.contextlogic.home:id/sign_in_fragment_password_text')
event_2_input.send_keys(Config.email_password)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.home:id/sign_in_fragment_sign_in_button')))

event_3_button = driver.find_element(MobileBy.ID, 'com.contextlogic.home:id/sign_in_fragment_sign_in_button')
event_3_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="Open Menu"]')))

event_4_button = driver.find_element(MobileBy.XPATH, '//android.widget.ImageButton[@content-desc="Open Menu"]')
event_4_button.click()

driver.swipe(130, 1262, 130, 460)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[13]/android.widget.LinearLayout')))

event_5_button = driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[13]/android.widget.LinearLayout')
event_5_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text="Manage Addresses"]')))

event_6_button = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Manage Addresses"]')
event_6_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.home:id/address_book_footer_text')))

event_7_button = driver.find_element(MobileBy.ID, 'com.contextlogic.home:id/address_book_footer_text')
event_7_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.home:id/shipping_address_form_street_address_text')))

event_8_input = driver.find_element(MobileBy.ID, 'com.contextlogic.home:id/shipping_address_form_street_address_text')
event_8_input.send_keys('aaa')

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.home:id/shipping_address_form_country_spinner')))

event_9_button = driver.find_element(MobileBy.ID, 'com.contextlogic.home:id/shipping_address_form_country_spinner')
event_9_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]')))

event_10_button = driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]')
event_10_button.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.home:id/shipping_address_form_city_text')))

event_11_input = driver.find_element(MobileBy.ID, 'com.contextlogic.home:id/shipping_address_form_city_text')
event_11_input.send_keys('bbb')

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.home:id/shipping_address_form_zip_postal_text')))

event_12_input = driver.find_element(MobileBy.ID, 'com.contextlogic.home:id/shipping_address_form_zip_postal_text')
event_12_input.send_keys('90020')

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.home:id/shipping_address_form_phone_text')))

event_13_input = driver.find_element(MobileBy.ID, 'com.contextlogic.home:id/shipping_address_form_phone_text')
event_13_input.send_keys('1234567890')

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'com.contextlogic.home:id/cart_fragment_cart_shipping_floating_done_button')))

event_14_button = driver.find_element(MobileBy.ID, 'com.contextlogic.home:id/cart_fragment_cart_shipping_floating_done_button')
event_14_button.click()

driver.quit()
