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
    'appPackage': 'com.woefe.shoppinglist',
    'appActivity': '.activity.MainActivity'
}

# 连接Appium服务器
driver = webdriver.Remote('http://localhost:4723', desired_caps)

# 点击添加按钮
driver.find_element(MobileBy.ID, 'com.woefe.shoppinglist:id/fab_add').click()

# 输入待办事项描述
input_element = driver.find_element(MobileBy.ID, 'com.woefe.shoppinglist:id/new_item_description')
input_element.clear()
input_element.send_keys('Sample Todo')

# 点击完成按钮
driver.find_element(MobileBy.ID, 'com.woefe.shoppinglist:id/button_add_new_item').click()

# 等待待办事项显示
WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, "//*[@text='Sample Todo']")))

# 向右滑动待办事项
element = driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='Sample Todo']")
start_x = element.location['x'] + element.size['width'] // 2  # 按键的右边缘
start_y = element.location['y'] + element.size['height'] // 2  # 按键的中心点
end_x = start_x + 500  # 向左滑动500像素
end_y = start_y
driver.swipe(start_x, start_y, end_x, end_y)

# 等待待办事项消失
WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((MobileBy.XPATH, "//*[@text='Sample Todo']")))

# 关闭Appium连接
driver.quit()