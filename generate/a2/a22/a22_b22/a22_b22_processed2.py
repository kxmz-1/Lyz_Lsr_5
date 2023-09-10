from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from time import sleep
import xml.dom.minidom
import os

# Appium连接配置
desired_caps = {
'platformName': 'Android',
'deviceName': 'emulator-5554',
'automationName': 'UiAutomator2',
'forceAppLaunch': True,
'appPackage': 'douzifly.list',
'appActivity': '.ui.home.MainActivity'
}

# 连接Appium服务器
driver = webdriver.Remote('http://localhost:4723', desired_caps)
i=0

def write(i):
    ui_hierarchies = driver.page_source
    dom = xml.dom.minidom.parseString(ui_hierarchies)
    ui_hierarchies = dom.toprettyxml()
    file_path = os.path.join(dire, f'hierarchy{i}.xml')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(ui_hierarchies)

tid = 'a22_2'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\a2'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)
# 模拟按键点击操作
write(i)
i += 1
driver.find_element(MobileBy.ID, 'douzifly.list:id/fab_add').click()
write(i)
i += 1
# 输入待办事项标题
input_element = driver.find_element(MobileBy.ID, 'douzifly.list:id/edit_text')
input_element.clear()
input_element.send_keys('Sample Todo')
write(i)
i += 1
# 点击添加按钮
driver.find_element(MobileBy.ID, 'douzifly.list:id/fab_add').click()
write(i)
i += 1
# 等待待办事项显示
WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, f"//*[@text='Sample Todo']")))
write(i)
i += 1
# 向右滑动
element = driver.find_element(MobileBy.ID, 'douzifly.list:id/txt_thing').click()
# 点击删除按钮
sleep(5)
write(i)
i += 1
driver.find_element(MobileBy.ID, 'douzifly.list:id/action_delete').click()
write(i)
i += 1
# 等待待办事项消失
WebDriverWait(driver, 10).until(
EC.invisibility_of_element_located((MobileBy.XPATH, f"//*[@text='Sample Todo']")))
sleep(5)
write(i)
i += 1
driver.quit()
