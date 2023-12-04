from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import xml.dom.minidom
import os
# Appium连接配置
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'forceAppLaunch': True,
    'appPackage': 'anti.tip',
    'appActivity': '.Tip',
    'noReset' : True
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

tid = 'a51_2'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\a5'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)
# 清除并输入账单金额

bill_input = driver.find_element(MobileBy.ID, 'anti.tip:id/bill')
write(i)
i += 1
bill_input.clear()
bill_input.send_keys('56.6')

# 清除并输入小费百分比
tip_percent_input = driver.find_element(MobileBy.ID, 'anti.tip:id/percent')
write(i)
i += 1
tip_percent_input.clear()
tip_percent_input.send_keys('15')

# 清除并输入人数
people_input = driver.find_element(MobileBy.ID, 'anti.tip:id/people')
write(i)
i += 1
people_input.clear()
people_input.send_keys('4')
driver.hide_keyboard()

write(i)
i += 1
# 等待每个人支付的金额出现
WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ID, 'anti.tip:id/each')))
sleep(5)
write(i)
# 关闭Appium连接
driver.quit()


from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import xml.dom.minidom
import os

# Appium连接配置
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'forceAppLaunch': True,
    'appPackage': 'anti.tip',
    'appActivity': '.Tip',
    "noReset":True
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

tid = 'a51'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\a5'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)

# 清除并输入账单金额
bill_amount_input = driver.find_element(MobileBy.ID, 'anti.tip:id/bill')

write(i)
i += 1
bill_amount_input.clear()
bill_amount_input.send_keys('56.6')

# 清除并输入小费百分比

tip_percent_input = driver.find_element(MobileBy.ID, 'anti.tip:id/percent')
write(i)
i += 1
tip_percent_input.clear()
tip_percent_input.send_keys('15')
driver.hide_keyboard()
write(i)
i += 1
# 等待总金额出现
WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ID, 'anti.tip:id/total')))
write(i)
# 关闭Appium连接
driver.quit()


