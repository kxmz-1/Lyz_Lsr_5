import set_goal
from appium import webdriver
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import config
import openai
import xml.dom.minidom
from xml.dom import minidom
import re
class control():
    def __init__(self, driver):
        self.driver = driver
        self.sleep_time = 0.1
        return
    def swipe_down(self):
        # 获取屏幕尺寸
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']

        # 定义起始点和结束点坐标
        start_x = width // 2
        start_y = height // 2
        end_x = width // 2
        end_y = 0

        # 创建TouchAction对象，并执行滑动操作
        self.driver.swipe(start_x, start_y, end_x, end_y)

    def swipe_up(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        start_x = width // 2
        start_y = height // 2
        end_x = width // 2
        end_y = height - 1  # Adjust this value to control the swipe distance

        self.driver.swipe(start_x, start_y, end_x, end_y)

    def act_on_emulator(self, action, element, decision, text = None):
        action = int(action)
        final_element = element[decision]
      #  possible_actions = {"action0": "click", "action1": "long click", "action2" :"send keys",
      #                      "action3" :"send keys and search", "action4":"send keys and enter",
      #                      "action5":"send keys and hide keyboard", "action6":"swipe down", "action7" : "swipe up"}
        if action == 0:
            final_element.click()
            sleep(5)
        if action == 1:
            TouchAction(self.driver).long_press(final_element).perform()
            sleep(5)
        if action == 2:
            self.swipe_down()
        if action == 3:
            self.swipe_up()
        if action == 4:
            final_element.send_keys(text)
            self.driver.execute_script("mobile: performEditorAction", {"action": "search"})
            sleep(5)
        if action == 5:
            final_element.send_keys(text)
            self.driver.press_keycode(66)
        if action == 6:
            final_element.send_keys(text)
            self.driver.hide_keyboard()
        if action == 7:
            final_element.clear()
            final_element.send_keys(text)

    def back(self):
        self.device.press("back")
        sleep(self.sleep_time)