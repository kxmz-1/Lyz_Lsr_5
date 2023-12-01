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
    'appPackage': 'com.woefe.shoppinglist',
    'appActivity': '.activity.MainActivity'
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

tid = 'a25_2'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\a2'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)
# 点击添加按钮
write(i)
i += 1
driver.find_element(MobileBy.ID, 'com.woefe.shoppinglist:id/fab_add').click()

# 输入待办事项描述
input_element = driver.find_element(MobileBy.ID, 'com.woefe.shoppinglist:id/new_item_description')
write(i)
i += 1
input_element.clear()
input_element.send_keys('Sample Todo')
driver.hide_keyboard()
write(i)
i += 1
# 点击完成按钮
driver.find_element(MobileBy.ID, 'com.woefe.shoppinglist:id/button_add_new_item').click()
write(i)
i += 1
# 等待待办事项显示
WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, "//*[@text='Sample Todo']")))
write(i)
i += 1
# 向右滑动待办事项
element = driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='Sample Todo']")
start_x = element.location['x'] + element.size['width'] // 2  # 按键的右边缘
start_y = element.location['y'] + element.size['height'] // 2  # 按键的中心点
end_x = start_x + 500  # 向左滑动500像素
end_y = start_y
driver.swipe(start_x, start_y, end_x, end_y)
write(i)
i += 1
# 等待待办事项消失
WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((MobileBy.XPATH, "//*[@text='Sample Todo']")))
write(i)
i += 1
# 关闭Appium连接
driver.quit()