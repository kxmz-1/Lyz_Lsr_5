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
    'appPackage': 'com.tleapps.simpletipcalculator',
    'appActivity': '.MainActivity'
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

tid = 'a53_2'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\a5'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)


# 点击"Accept"按钮
accept_button = driver.find_element(MobileBy.ID, 'android:id/button1')
write(i)
i += 1
accept_button.click()

# 清除并输入账单金额
bill_input = driver.find_element(MobileBy.ID, 'com.tleapps.simpletipcalculator:id/editTextBill')
write(i)
i += 1
bill_input.clear()
bill_input.send_keys('56.6')

# 清除并输入小费百分比
tip_percent_input = driver.find_element(MobileBy.ID, 'com.tleapps.simpletipcalculator:id/editTextTip')
write(i)
i += 1
tip_percent_input.clear()
tip_percent_input.send_keys('15')

# 清除并输入分账人数
split_input = driver.find_element(MobileBy.ID, 'com.tleapps.simpletipcalculator:id/editTextSplit')
write(i)
i += 1
split_input.clear()
split_input.send_keys('4')
driver.hide_keyboard()

# 点击"Calculate"按钮
calculate_button = driver.find_element(MobileBy.ID, 'com.tleapps.simpletipcalculator:id/buttonCalculate')
write(i)
i += 1
calculate_button.click()
write(i)
i += 1
# 等待每人支付金额出现
WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ID, 'com.tleapps.simpletipcalculator:id/textViewTotalPerPerson')))
write(i)
# 关闭Appium连接
driver.quit()