from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

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

# 点击Skip按钮
skip_button = driver.find_element(MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/btn_skip')
skip_button.click()
sleep(5)
# 点击新建任务按钮
new_task_button = driver.find_element(MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/fab_new_task')
new_task_button.click()
sleep(5)
# 输入任务名称并隐藏键盘
task_name_input = driver.find_element(MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/et_new_task_name')
task_name_input.send_keys('Sample Todo')
driver.hide_keyboard()

# 点击Okay按钮
okay_button = driver.find_element(MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/bt_new_task_ok')
okay_button.click()

# 等待Sample Todo文本出现
WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/tv_exlv_task_name'), 'Sample Todo'))

# 长按Sample Todo任务
sample_todo_task = driver.find_element(MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/tv_exlv_task_name')
TouchAction(driver).long_press(sample_todo_task).perform()

# 点击删除任务
delete_task_button = driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]")
delete_task_button.click()

# 等待Sample Todo文本消失
WebDriverWait(driver, 10).until_not(EC.text_to_be_present_in_element((MobileBy.ID, 'org.secuso.privacyfriendlytodolist:id/tv_exlv_task_name'), 'Sample Todo'))

# 关闭Appium连接
driver.quit()
