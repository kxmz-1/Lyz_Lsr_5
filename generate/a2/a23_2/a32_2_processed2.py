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

tid = 'a23_2'
path = 'C:\\Users\\11303\\Desktop\\miaozi\\generate\\a2'
dire = os.path.join(path, tid)
if not os.path.exists(dire):
    os.mkdir(dire)
# 点击Skip按钮

sleep(5)
skip_button = driver.find_element(MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/btn_skip')
write(i)
i += 1
skip_button.click()
sleep(5)
# 点击新建任务按钮
new_task_button = driver.find_element(MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/fab_new_task')
write(i)
i += 1
new_task_button.click()
sleep(5)
# 输入任务名称并隐藏键盘
task_name_input = driver.find_element(MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/et_new_task_name')
write(i)
i += 1
task_name_input.send_keys('Sample Todo')
driver.hide_keyboard()

# 点击Okay按钮
okay_button = driver.find_element(MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/bt_new_task_ok')
write(i)
i += 1
okay_button.click()
write(i)
i += 1
# 等待Sample Todo文本出现
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/tv_exlv_task_name'), 'Sample Todo'))

# 长按Sample Todo任务
sample_todo_task = driver.find_element(MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/tv_exlv_task_name')
write(i)
i += 1
TouchAction(driver).long_press(sample_todo_task).perform()

# 点击删除任务
delete_task_button = driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]")
write(i)
i += 1
delete_task_button.click()
write(i)
i += 1
# 等待Sample Todo文本消失
WebDriverWait(driver, 10).until_not(EC.text_to_be_present_in_element((MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/tv_exlv_task_name'), 'Sample Todo'))
write(i)
i += 1
# 关闭Appium连接
driver.quit()
