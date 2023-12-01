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
    'appPackage': 'com.rubenroy.minimaltodo',
    'appActivity': '.MainActivity'
}

# 连接到Appium服务器
driver = webdriver.Remote(appium_server, desired_caps)
i=0

def write(i):
    ui_hierarchies = driver.page_source
    dom = xml.dom.minidom.parseString(ui_hierarchies)
    ui_hierarchies = dom.toprettyxml()
    file_path = os.path.join(dire, f'hierarchy{i}.xml')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(ui_hierarchies)

tid = 'a21'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\a2'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)
try:
    # 查找并点击添加待办事项按钮
    add_button = driver.find_element(MobileBy.ID, 'com.rubenroy.minimaltodo:id/addToDoItemFAB')
    write(i)
    i += 1
    add_button.click()
    time.sleep(5)
    # 查找待办事项标题输入框
    title_input = driver.find_element(MobileBy.ID, 'com.rubenroy.minimaltodo:id/userToDoEditText')
    write(i)
    i += 1
    title_input.click()

    # 在待办事项标题输入框中输入标题
    title_input.send_keys('Sample Todo')

    # 隐藏键盘
    driver.hide_keyboard()

    # 点击确认添加待办事项按钮
    confirm_button = driver.find_element(MobileBy.ID, 'com.rubenroy.minimaltodo:id/makeToDoFloatingActionButton')
    write(i)
    i += 1
    confirm_button.click()

    # 等待特定元素的出现
    time.sleep(2)
    write(i)
    i += 1
    # 验证待办事项是否添加成功
    element = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Sample Todo"]')
    write(i)
    i += 1
except NoSuchElementException as e:
    print("Element not found:", str(e))

finally:
    # 关闭驱动
    driver.quit()
