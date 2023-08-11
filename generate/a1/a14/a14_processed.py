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
    'forceAppLaunch': True,
    'appPackage': 'de.baumann.browser',
    'appActivity': '.Activity.BrowserActivity',
    'noReset' : True
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

tid = 'a14'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\a1'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)
# 连接到Appium服务器
driver = webdriver.Remote(appium_server, desired_caps)


try:

    # 点击URL输入框
    url_input = driver.find_element(MobileBy.ID, 'de.baumann.browser:id/main_omnibox_input')
    write(i)
    i += 1
    url_input.click()

    # 在URL输入框中输入URL并按下Enter键
    url_input.send_keys('https://www.ics.uci.edu')
    driver.press_keycode(66)  # Enter键的键码是66

    # 等待特定元素的出现
    time.sleep(10)
    write(i)
    i += 1
    # 查找特定元素
    element = driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="UCI Donald Bren School of Information and Computer Sciences - logo"]')
    # 执行特定操作
    write(i)
    i += 1
except NoSuchElementException as e:
    print("Element not found:", str(e))

finally:
    # 关闭驱动
    driver.quit()
