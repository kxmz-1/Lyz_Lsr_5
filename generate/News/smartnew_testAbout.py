from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'forceAppLaunch': True,
    'appPackage': '',
    'appActivity': '',
    'noReset' : True
}
desired_caps['appPackage'] = 'jp.gocro.smartnews.android'
desired_caps['appActivity'] = 'activity.SmartNewsActivity'

driver = webdriver.Remote('http://localhost:4723', desired_caps)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.ID, 'jp.gocro.smartnews.android:id/settingButton')))

event_0_button = driver.find_element(MobileBy.ID, 'jp.gocro.smartnews.android:id/settingButton')
event_0_button.click()


def swipe_down():
# 获取屏幕尺寸
    size = driver.get_window_size()
    width = size['width']
    height = size['height']

    # 定义起始点和结束点坐标
    start_x = width // 2
    start_y = height // 2
    end_x = width // 2
    end_y = 0

    # 创建TouchAction对象，并执行滑动操作
    driver.swipe(start_x, start_y, end_x, end_y)
swipe_down()
swipe_down()
swipe_down()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[7]')))

event_1_button = driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.widget.LinearLayout[7]")
event_1_button.click()

driver.quit()
