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
    'appPackage': 'org.secuso.privacyfriendlytodolist',
    'appActivity': '.view.SplashActivity'
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

tid = 'a23'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\a2'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)
# 点击Skip按钮
skip_button = driver.find_element(MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/btn_skip')
write(i)
i += 1
skip_button.click()
sleep(5)
# 点击新任务按钮
new_task_button = driver.find_element(MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/fab_new_task')
write(i)
i += 1
new_task_button.click()
sleep(5)
# 输入任务名称并隐藏键盘
task_name_input = driver.find_element(MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/et_new_task_name')
task_name_input.send_keys('Sample Todo')
driver.hide_keyboard()

# 点击确认按钮
ok_button = driver.find_element(MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/bt_new_task_ok')
write(i)
i += 1
ok_button.click()
write(i)
i += 1
# 等待任务出现
WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.TextView[@text='Sample Todo']")))
write(i)
# 关闭Appium连接
driver.quit()
