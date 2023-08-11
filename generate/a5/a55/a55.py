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
    'appPackage': 'com.jpstudiosonline.tipcalculator',
    'appActivity': '.MainActivity'
}

# 连接Appium服务器
driver = webdriver.Remote('http://localhost:4723', desired_caps)

# 清除并输入账单总额
bill_total_input = driver.find_element(MobileBy.ID, 'com.jpstudiosonline.tipcalculator:id/etBillTotal')
bill_total_input.clear()
bill_total_input.send_keys('56.6')

# 清除并输入小费百分比
tip_percent_input = driver.find_element(MobileBy.ID, 'com.jpstudiosonline.tipcalculator:id/etTipAmount')
tip_percent_input.clear()
tip_percent_input.send_keys('15')
driver.hide_keyboard()

# 点击计算按钮
calculate_button = driver.find_element(MobileBy.ID, 'com.jpstudiosonline.tipcalculator:id/btCalculate')
calculate_button.click()

# 等待总金额出现
WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ID, 'com.jpstudiosonline.tipcalculator:id/tvTotalWithTip')))

# 关闭Appium连接
driver.quit()
