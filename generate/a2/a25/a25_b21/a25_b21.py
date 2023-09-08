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
    'automationName': 'UiAutomator2',
    'noReset': True,
    'forceAppLaunch': True,
    'appPackage': 'com.woefe.shoppinglist',
    'appActivity': '.activity.MainActivity'
}

# 连接到Appium服务器
driver = webdriver.Remote(appium_server, desired_caps)

try:
    # 查找并点击添加按钮
    add_button = driver.find_element(MobileBy.ID, 'com.woefe.shoppinglist:id/fab_add')
    add_button.click()

    # 查找新项目描述输入框
    description_input = driver.find_element(MobileBy.ID, 'com.woefe.shoppinglist:id/new_item_description')
    description_input.click()

    # 在新项目描述输入框中输入项目名
    description_input.send_keys('Sample Todo')

    # 隐藏键盘
    driver.hide_keyboard()

    # 点击确认添加按钮
    confirm_button = driver.find_element(MobileBy.ID, 'com.woefe.shoppinglist:id/button_add_new_item')
    confirm_button.click()

    # 等待特定元素的出现
    time.sleep(2)

    # 验证项目是否添加成功
    element = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Sample Todo"]')

except NoSuchElementException as e:
    print("Element not found:", str(e))

finally:
    # 关闭驱动
    driver.quit()
