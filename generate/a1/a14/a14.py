from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
import time

# Appium服务器地址和连接配置
appium_server = 'http://localhost:4723/wd/hub'
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'noReset': True,
    'forceAppLaunch': True,
    'appPackage': 'de.baumann.browser',
    'appActivity': '.Activity.BrowserActivity'
}

# 连接到Appium服务器
driver = webdriver.Remote(appium_server, desired_caps)

try:
    # 点击确认按钮
    confirm_button = driver.find_element(MobileBy.ID, 'de.baumann.browser:id/floatButton_ok')
    confirm_button.click()

    # 点击URL输入框
    url_input = driver.find_element(MobileBy.ID, 'de.baumann.browser:id/main_omnibox_input')
    url_input.click()

    # 在URL输入框中输入URL并按下Enter键
    url_input.send_keys('https://www.ics.uci.edu')
    driver.press_keycode(66)  # Enter键的键码是66

    # 等待特定元素的出现
    time.sleep(10)

    # 查找特定元素
    element = driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]')
    # 执行特定操作

except NoSuchElementException as e:
    print("Element not found:", str(e))

finally:
    # 关闭驱动
    driver.quit()
