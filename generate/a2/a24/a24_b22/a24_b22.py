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
    'appPackage': 'kdk.android.simplydo',
    'appActivity': '.SimplyDoActivity',
    'noReset': True
}

# 连接Appium服务器
driver = webdriver.Remote('http://localhost:4723', desired_caps)

# 输入新列表名称
input_element = driver.find_element(MobileBy.ID, 'kdk.android.simplydo:id/AddListEditText')
input_element.clear()
input_element.send_keys('Sample Todo')

# 点击添加按钮
driver.find_element(MobileBy.ID, 'kdk.android.simplydo:id/AddListButton').click()

# 等待列表显示
WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, "//*[@text='Sample Todo']")))

# 长按待办事项
element = driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='Sample Todo']")
action = TouchAction(driver)
action.long_press(element).perform()

# 点击删除选项
sleep(5)
driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]').click()
sleep(5)
# 点击确认删除按钮
driver.find_element(MobileBy.ID, 'android:id/button1').click()

# 等待待办事项消失
WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((MobileBy.XPATH, "//*[@text='Sample Todo']")))

# 关闭Appium连接
driver.quit()