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
    'appPackage': 'kdk.android.simplydo',
    'appActivity': '.SimplyDoActivity'
}

# 连接到Appium服务器
driver = webdriver.Remote(appium_server, desired_caps)

try:
    # 查找并点击添加列表按钮
    add_list_button = driver.find_element(MobileBy.ID, 'kdk.android.simplydo:id/AddListButton')
    add_list_button.click()

    # 查找列表名称输入框
    name_input = driver.find_element(MobileBy.ID, 'kdk.android.simplydo:id/AddListEditText')
    name_input.click()

    # 在列表名称输入框中输入列表名
    name_input.send_keys('Sample Todo')

    # 隐藏键盘
    driver.hide_keyboard()

    # 点击确认添加列表按钮
    confirm_button = driver.find_element(MobileBy.ID, 'kdk.android.simplydo:id/AddListButton')
    confirm_button.click()

    # 等待特定元素的出现
    time.sleep(2)

    # 验证列表是否添加成功
    element = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Sample Todo"]')

except NoSuchElementException as e:
    print("Element not found:", str(e))

finally:
    # 关闭驱动
    driver.quit()
