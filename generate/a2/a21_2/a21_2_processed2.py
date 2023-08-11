from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xml.dom.minidom
import os
# Appium服务器地址和连接配置
appium_server = 'http://localhost:4723'
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'forceAppLaunch': True,
    'appPackage': 'com.rubenroy.minimaltodo',
    'appActivity': '.MainActivity'
}

# 连接到Appium服务器
driver = webdriver.Remote(appium_server, desired_caps)
i = 0

def write(i):
    ui_hierarchies = driver.page_source
    dom = xml.dom.minidom.parseString(ui_hierarchies)
    ui_hierarchies = dom.toprettyxml()
    file_path = os.path.join(dire, f'hierarchy{i}.xml')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(ui_hierarchies)

tid = 'a21_2'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\a2'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)

try:
    # 查找并点击添加按钮
    add_button = driver.find_element(MobileBy.ID, 'com.rubenroy.minimaltodo:id/addToDoItemFAB')
    write(i)
    i += 1
    add_button.click()
    time.sleep(2)
    # 查找项目标题输入框
    title_input = driver.find_element(MobileBy.ID, 'com.rubenroy.minimaltodo:id/userToDoEditText')
    write(i)
    i += 1
    title_input.click()

    # 在项目标题输入框中输入项目名
    title_input.send_keys('Sample Todo')

    # 隐藏键盘
    driver.hide_keyboard()

    # 点击确认添加按钮
    confirm_button = driver.find_element(MobileBy.ID, 'com.rubenroy.minimaltodo:id/makeToDoFloatingActionButton')
    write(i)
    i += 1
    confirm_button.click()
    # 等待特定文本的出现
    time.sleep(2)
    write(i)
    i += 1
    element = driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='Sample Todo']")
    write(i)
    i += 1
    start_x = element.location['x'] + element.size['width'] // 2  # 按键的右边缘
    start_y = element.location['y'] + element.size['height'] // 2  # 按键的中心点
    end_x = start_x - 700  # 向左滑动500像素
    end_y = start_y
    driver.swipe(start_x, start_y, end_x, end_y)
    write(i)
    i += 1
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((MobileBy.XPATH, f"//*[@text='Sample Todo']")))
    write(i)
    i += 1

except NoSuchElementException as e:
    print("Element not found:", str(e))


