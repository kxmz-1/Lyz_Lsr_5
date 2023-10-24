from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
import time

# Appium服务器地址和连接配置
appium_server = 'http://localhost:4723'
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.stoutner.privacybrowser.standard',
    'appActivity': 'com.stoutner.privacybrowser.activities.MainWebViewActivity',
    'automationName': 'UiAutomator2',
    'noReset': True,
    'forceAppLaunch': True

}

# 连接到Appium服务器
driver = webdriver.Remote(appium_server, desired_caps)

try:
    # 点击URL编辑框
    url_edittext = driver.find_element(MobileBy.ID, 'com.stoutner.privacybrowser.standard:id/url_edittext')
    url_edittext.click()

    # 在URL编辑框中输入URL并按下Enter键
    url_edittext.send_keys('https://www.ics.uci.edu')
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


