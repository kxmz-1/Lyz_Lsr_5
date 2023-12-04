from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
import ast

class control:
    def __init__(self, driver):
        self.driver = driver
        self.sleep_time = 0.1
        return

    def swipe_down(self,bound):
        # 获取屏幕尺寸
        x1=bound[0][0]
        y1=bound[0][1]
        x2=bound[1][0]
        y2=bound[1][1]
        #size = self.driver.get_window_size()
        #width = size['width']
        #height = size['height']
        start_x = (x1+x2) // 2
        start_y = y2//2
        end_x = (x1+x2)//2
        end_y = y1+10  # Adjust this value to control the swipe distance
        self.driver.swipe(start_x, start_y, end_x, end_y)
    def swipe_up(self,bound):
        x1=bound[0][0]
        y1=bound[0][1]
        x2=bound[1][0]
        y2=bound[1][1]
        #size = self.driver.get_window_size()
        #width = size['width']
        #height = size['height']
        start_x = (x1+x2) // 2
        start_y = y1//2
        end_x = (x1+x2)//2
        end_y = y2-10  # Adjust this value to control the swipe distance

        self.driver.swipe(start_x, start_y, end_x, end_y)

    def act_on_emulator_oracle(self, content, driver):
        try:
            if content[0] == "wait_until_element_presence" or content[0] == "wait_until_text_presence":
                if content[2] == "id":
                    WebDriverWait(driver, content[1]).until(
                        EC.presence_of_element_located((MobileBy.ID, content[3])))
                    print("find", "id")
                    return True, driver.find_element(MobileBy.ID, content[3])
                elif content[2] == "xpath":
                    WebDriverWait(driver, content[1]).until(
                        EC.presence_of_element_located((MobileBy.XPATH, content[3]))
                    )
                    print("find", "xpath")
                    return True, driver.find_element(MobileBy.XPATH, content[3])
                elif content[2] == "text":
                    WebDriverWait(driver, content[1]).until(
                        EC.presence_of_element_located((MobileBy.XPATH, f"//*[@text='{content[3]}']")))
                    print("find", "text")
                    return True, driver.find_element(MobileBy.XPATH, f"//*[@text='{content[3]}']")
            elif content[0] == "wait_until_text_invisible":
                if content[2] == "xpath":
                    WebDriverWait(driver, content[1]).until(
                        EC.invisibility_of_element_located((MobileBy.XPATH, content[3])))
                    print("invisible true")
                    return True, None
                elif content[2] == "text":
                    WebDriverWait(driver, content[1]).until(
                        EC.invisibility_of_element_located((MobileBy.XPATH, f"//*[@text='{content[3]}']")))
                    print("invisible true")
                    return True, None
        except Exception:
            return False, None

    def act_on_emulator_gui(self, action, element, decision, text=None):
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
            bound=ast.literal_eval(final_element.get_attribute("bounds").replace("][", "],["))
            print(type(bound),bound)
            self.swipe_down(bound)
        if action == 3:
            bound=ast.literal_eval(final_element.get_attribute("bounds").replace("][", "],["))
            self.swipe_up(bound)
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
