from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
import time
import xml.dom.minidom
import os
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
driver = webdriver.Remote(appium_server, desired_caps)
i=0

def write(i):
    ui_hierarchies = driver.page_source
    dom = xml.dom.minidom.parseString(ui_hierarchies)
    ui_hierarchies = dom.toprettyxml()
    file_path = os.path.join(dire, f'hierarchy{i}.xml')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(ui_hierarchies)

tid = 'a24'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\a2'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)
try:

    # 查找列表名称输入框
    name_input = driver.find_element(MobileBy.ID, 'kdk.android.simplydo:id/AddListEditText')
    write(i)
    i += 1
    name_input.click()
    name_input.send_keys('Sample Todo')
    driver.hide_keyboard()

    # 点击确认添加列表按钮
    confirm_button = driver.find_element(MobileBy.ID, 'kdk.android.simplydo:id/AddListButton')
    write(i)
    i += 1
    confirm_button.click()

    # 等待特定元素的出现
    time.sleep(2)
    write(i)
    i += 1
    # 验证列表是否添加成功
    element = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Sample Todo"]')
    write(i)
    i += 1
except NoSuchElementException as e:
    print("Element not found:", str(e))

finally:
    # 关闭驱动
    driver.quit()
