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
    'appPackage': 'kdk.android.simplydo',
    'appActivity': '.SimplyDoActivity',
    'noReset': True
}

# 连接Appium服务器
driver = webdriver.Remote('http://localhost:4723', desired_caps)
i = 0

def write(i):
    ui_hierarchies = driver.page_source
    dom = xml.dom.minidom.parseString(ui_hierarchies)
    ui_hierarchies = dom.toprettyxml()
    file_path = os.path.join(dire, f'hierarchy{i}.xml')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(ui_hierarchies)

tid = 'a24_2'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\a2'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)

# 输入新列表名称
input_element = driver.find_element(MobileBy.ID, 'kdk.android.simplydo:id/AddListEditText')
write(i)
i += 1
input_element.clear()
input_element.send_keys('Sample Todo')

# 点击添加按钮
write(i)
i += 1
driver.find_element(MobileBy.ID, 'kdk.android.simplydo:id/AddListButton').click()
write(i)
i += 1
# 等待列表显示
WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, "//*[@text='Sample Todo']")))
write(i)
i += 1
# 长按待办事项
element = driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='Sample Todo']")
action = TouchAction(driver)
action.long_press(element).perform()
write(i)
i += 1
# 点击删除选项
sleep(5)
driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]').click()
sleep(5)
write(i)
i += 1
# 点击确认删除按钮
driver.find_element(MobileBy.ID, 'android:id/button1').click()
write(i)
i += 1
# 等待待办事项消失
WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((MobileBy.XPATH, "//*[@text='Sample Todo']")))
write(i)
i += 1
# 关闭Appium连接
driver.quit()