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

# 模拟按键点击操作
driver.find_element(MobileBy.ID, 'douzifly.list:id/fab_add').click()

# 输入待办事项标题
input_element = driver.find_element(MobileBy.ID, 'douzifly.list:id/edit_text')
input_element.clear()
input_element.send_keys('Sample Todo')

# 点击添加按钮
driver.find_element(MobileBy.ID, 'douzifly.list:id/fab_add').click()

# 等待待办事项显示
WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, f"//*[@text='Sample Todo']")))

# 向右滑动
element = driver.find_element(MobileBy.ID, 'douzifly.list:id/txt_thing').click()
# 点击删除按钮
sleep(5)
driver.find_element(MobileBy.ID, 'douzifly.list:id/action_delete').click()

# 等待待办事项消失
WebDriverWait(driver, 10).until(
EC.invisibility_of_element_located((MobileBy.XPATH, f"//*[@text='Sample Todo']")))

driver.quit()
