import set_goal
from appium import webdriver
import xml.etree.ElementTree as ET
from time import sleep
import config
from openai import OpenAI
import re
from control_screen import control
import element_info_extractor
from saver import recorder

# openai.api_base = config.api_base


class Context:
    def __init__(self, activity, ui_elem):
        self.activity = activity
        self.ui = ui_elem
        self.elem_num = {x: 0 for x in ui_elem}

    def add_elem_num(self, elem):
        if elem in self.elem_num:
            self.elem_num[elem] += 1
        else:
            self.elem_num[elem] = 1
        return self.elem_num[elem]

    def find_possible_elem(self, ui_elem, elem_info):
        ui_elem_copy = ui_elem.copy()
        elem_info_copy = elem_info.copy()
        for i in range(len(ui_elem_copy) - 1, -1, -1):
            if self.elem_num[ui_elem_copy[i]] >= 2:
                del ui_elem_copy[i]
                del elem_info_copy[i]
        return ui_elem_copy, elem_info_copy

    def equal(self, activity, ui_elem):
        if activity != self.activity:
            print(False)
            return False
        if len(self.ui) != len(ui_elem):
            print(False)
            return False
        for key in ui_elem:
            if key not in self.ui:
                print(False)
                return False
        return True


class History:
    def __init__(self):
        self.all_contexts = []

    def check_same(self, activity, ui_elem):
        for index, context in enumerate(self.all_contexts):
            if context.equal(activity, ui_elem):
                return index
        return None

    def eliminate_duplications(self, elements, elements_info):
        context_index = self.check_same(driver.current_activity, elements)
        if context_index is None:
            return elements, elements_info
        else:
            return self.all_contexts[context_index].find_possible_elem(elements, elements_info)

    def store(self, elements, elem):
        context_index = self.check_same(driver.current_activity, elements)
        if context_index is None:
            new_context = Context(driver.current_activity, elements)
            self.all_contexts.append(new_context)
            return self.all_contexts[-1].add_elem_num(elem)
        else:
            return self.all_contexts[context_index].add_elem_num(elem)

    def history_cache_check(self, activity, ui_elem):
        for index, context in enumerate(self.all_contexts):
            if context.equal(activity, ui_elem):
                print('cache found')
                return index


def gpt_generation(messages):
    client=config.agent
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
        temperature=0.2,
    )
    return completion.choices[0].message["content"]


class Migration:
    def __init__(self, target, source_case):
        self.get_current_page_info = None
        self.successful = False
        self.goal = target
        self.source_testcase = source_case
        self.chose_performance = []
        self.finished_welcome = False
        self.current_step = 0
        self.natural_language_actions = ""
        self.indexes = ""
        self.text = ""
        self.action = 0
        self.current_page_info = ""
        self.element_List = []
        self.decision_element = 0
        self.scroll_decision = 0
        self.flag = False
        self.message = []
        self.result_collector = recorder(config.source, config.migrate)
        self.possible_actions = {"action0": "click", "action1": "long click", "action2": "swipe down",
                                 "action3": "swipe up",
                                 "action4": "send keys and search", "action5": "send keys and enter",
                                 "action6": "send keys and hide keyboard", "action7": "clear and send keys"}

    def get_number(self, input_string):
        match = re.match(r'^(\d+)', input_string)
        if match:
            return match.group(1)
        else:
            return False

    def extract_quoted_text(self, data_string):
        quoted_text = []
        pattern = r"'(.*?[^'])'\s*\]"  # 正则表达式匹配单引号中的内容，后面跟着一个以']'结尾的字符序列

        matches = re.findall(pattern, data_string)
        for match in matches:
            quoted_text.append(match)

        return quoted_text

    def actions_in_natural_language(self):
        content = ""
        if len(self.chose_performance) == 0:
            return ""
        else:
            content += "\nCurrently, we have already performed the following actions to reach this goal, meaning that " \
                       "you don't have to redo these steps anymore:\n"
            for i in range(len(self.chose_performance)):
                if self.chose_performance[i][1] is not None:
                    content += f"\naction{i}. The widget we choose: {str(self.chose_performance[i][1])}, and "
                    content += f"the action we perform on the widget is {str(self.chose_performance[i][2])}"
                    if len(self.chose_performance[i]) == 4:
                        content += f", and the text we enter: {str(self.chose_performance[i][3])}"
                else:
                    content += f"\nWe are trying to {self.chose_performance[i][2][0]}. This element's " \
                               f"{self.chose_performance[i][2][2]} is {self.chose_performance[i][2][3]}."
        self.natural_language_actions = content

    def finished_welcome_session(self):
        sentence = "The initial stage of any software includes a setup/configuration interface and a brief " \
                   "description of the software to provide information to the users who interact with this app for " \
                   "the first time. Do you think our app, with package {config.package_name}, is in the initial stage " \
                   "or in the main screen where the core functionality resides now? Choose [not main] or [main] with " \
                   "explanations. Here are the existing widgets' information:"
        ui_hierarchies = driver.page_source
        root = ET.fromstring(ui_hierarchies)
        layout_min = {}
        set_goal.extract_elements_with_conditions(root, layout_min)
        layout_min = set_goal.remove_consecutive_duplicates(layout_min)
        sentence += set_goal.templating(layout_min)
        mes = [
            {"role": "user", "content": sentence}
        ]
        completion = gpt_generation(mes)
        mes.append({"role": "assistant", "content": completion})
        mes.append({"role": "user", "content": "[main] or [not main]"})
        completion = gpt_generation(mes)
        print(completion)
        return "[not main]" in completion

    def act_on_welcome(self):
        sentence = "Currently, you are on the welcome and permission screens that explains the software's " \
                   f"features, instructions, tips, and permissions for use." \
                   f"You need to transfer from welcome and permission screens to the main screen. which widgets do" \
                   f"you decide to choose? Here are the existing widgets' information:"
        ele = []
        current_page_info = element_info_extractor.info(driver,
                                                        ele)
        self.index_list(current_page_info, False)
        print(self.indexes)
        sentence += str(self.indexes)
        completion = gpt_generation([{"role": "user", "content": sentence}])
        print(completion)
        num = int(self.choose(completion, "index"))
        ele[num].click()

    def checked_if_finished(self):
        nlp=self.natural_language_actions.replace("Currently, we have already performed the following actions to reach this goal, meaning that you don't have to redo these steps anymore:","")
        nlp=nlp.replace('\n',"")
        cont = f"This is a test case description of a particular APP: {self.goal}. You are trying to perform the same " \
               f"step described above to a related APP, an APP that has similar functions but different " \
               f"organizations. Now, you are trying to perform one of the action described in the test case: " \
               f"{self.source_testcase[self.current_step]}. These are the actions we already performed: \n" \
               f"{nlp} \n"
        cont += f"Do you think the action in the test case to the action we performed? Because our task is imitating the action in the test case, " \
                f"the attribute of the widget only need to be similar. They do not need to strictly be the same."\
                f"If the actions are similar, output [1], and I will provide you with next " \
                f"step of this test case. else output [0]. First, output only with [0] or [1]. Then, explain the reason"
        mes = [{"role": "user", "content": cont}]
        #mes.append({"role": "assistant", "content": completion})
        #mes.append({"role": "user", "content": "From your previous output, respond only with [0] or [1]."
        #            "Remember, the attributes do not need to be the same. Similar functions is fine"})
        for p in mes:
            print(p['role'],p['content'])
        #completion = gpt_generation(mes)
        #print(completion)
        completion = gpt_generation(mes)
        print(completion)
        return "[1]" in completion

    def choose(self, completion, content):
        candidates = completion.split(content)
        for i in range(len(candidates)):
            if self.get_number(candidates[i]):
                return self.get_number(candidates[i])

    def index_list(self, info, add=True):
        message = ""
        self.scroll_decision = 0
        self.flag = False
        for i in range(len(info)):
            message += f"index{i}:{str(info[i])} \n"
            if "scrollable" in info[i] and info[i]["scrollable"] and self.flag is False:
                self.flag = True
                self.scroll_decision = i
        if self.flag:
            message += f"Among these indexes, index{self.scroll_decision} is a scrollable element that can can lead you to discover elements that are " \
                       f"hidden under the current UI state that might lead you to finish the testcase. If you want to act on this element, this element" \
                       f"will be swiped down. However, if you already swipe this elements, you should not do it again.\n"
        if add:
            message += "Please choose the index you think can imitate the above test case or bring us closer to the goal. Display your " \
                       "answer in the form [index{i}]. For example, [index0]"
        else:
            message += "Please choose the index you think can transfer to main screen. Display your " \
                       "answer in the form [index{i}]. For example, [index0]"
        self.indexes = message
        print(self.indexes)

    def choose_action(self):
        print(self.decision_element, self.scroll_decision, self.flag)
        if self.decision_element == self.scroll_decision and self.flag:
            return 2, None
        action_list = "Choose only one of the following actions you want to perform on this index:\n "
        action_list += "action0: click\n action1:" \
                       "long click\n action2:swipe down\n action3:swipe up\n" \
                       "answer with the structure [action{i}]. For example, [action0]."
        if "fillable" in self.get_current_page_info[self.decision_element]:
            action_list += "action4:send keys and search \n action5. send keys and enter \n " \
                           "action6: send keys and hide keyboard. \n action7: clear and send keys. \n If you perform " \
                           "action4 to action8, provide me with the structure [action{i},'{content you want to " \
                           "send}'] for example, [action4, 'Hello'],[action8, '18']. \n Since this widget is " \
                           "fillable, you better to choose between action4 and action7 and enter the text of the " \
                           "event in the source testcase that corresponds to the action we want to perform now."
        self.message.append({"role": 'assistant', "content": "index" + str(self.decision_element)})
        self.message.append({'role': "user", "content": action_list})
        completion = gpt_generation(self.message)
        choose_action = self.choose(completion, "action")
        if choose_action[len(choose_action) - 2].isdigit() and int(choose_action[len(choose_action) - 2]) >= 4 and int(
                choose_action[len(choose_action) - 2]) <= 7:
            self.message.append({'role': 'assistant', 'content': completion})
            self.message.append({'role': 'user',
                                 'content': "Only select one action that is most suitable, and in the form [action{"
                                            "i},'{content you want to send}']. For example, [action8, '12']. This is "
                                            "a wrong answer:['clear_and_send_keys','12'],don't do that.{content you "
                                            "want to send} refers to the text in the source testcase that corresponds "
                                            "to the  action we want to perform now."})
        #completion = gpt_generation(self.message)
        choose_action = self.check_valid_response(self.message, "action")
        if "fillable" in self.get_current_page_info[self.decision_element]:
            text = self.extract_quoted_text(completion)
            print(text)
        else:
            text = None
        print(completion)
        return choose_action, text

    def send_migrate_result_oracle(self, ele):
        if self.source_testcase[self.current_step]["action"][0] == "wait_until_text_presence":
            process_result = element_info_extractor.process(driver.page_source, ele)
            dic = {"text": ele.text, "content-desc": ele.get_attribute("content-desc"),
                   "class": ele.get_attribute("class"), "resource-id": ele.get_attribute("resourceId"),
                   "activity": driver.current_activity, "package": driver.current_package,
                   "parent_text": element_info_extractor.get_parent_text(process_result),
                   "sibling_text": element_info_extractor.get_sibling_text(process_result),
                   "child_text": element_info_extractor.get_child_text(ele),
                   "clickable": ele.get_attribute("clickable"), "event_type": "oracle",
                   "action": self.source_testcase[self.current_step]["action"]}
            page = driver.page_source
            self.result_collector.add_event(dic, page)
        elif self.source_testcase[self.current_step]["action"][0] == "wait_until_text_invisible":
            dic = {"class": "", "resource-id": "", "text": "", "content-desc": "", "clickable": "", "password": "",
                   "parent_text": "", "sibling_text": "", "package": driver.current_package,
                   "activity": driver.current_activity, "event_type": "oracle",
                   "action": self.source_testcase[self.current_step]["action"]}
            page = driver.page_source
            self.result_collector.add_event(dic, page)

    def send_migrate_result_gui(self):
        ele = self.element_List[self.decision_element]
        process_result = element_info_extractor.process(driver.page_source, ele)
        dic = {
            "text": ele.text, "content-desc": ele.get_attribute("content-desc"), "class": ele.get_attribute("class"),
            "resource-id": ele.get_attribute("resourceId"), "activity": driver.current_activity,
            "package": driver.current_package, "parent_text": element_info_extractor.get_parent_text(process_result),
            "sibling_text": element_info_extractor.get_sibling_text(process_result),
            "child_text": element_info_extractor.get_child_text(ele), "clickable": ele.get_attribute("clickable"),
            "event_type": "oracle"
        }
        if self.text is None:
            dic["action"] = [self.possible_actions["action" + str(self.action)]]
        else:
            dic["action"] = [self.possible_actions["action" + str(self.action)], self.text]
        page = driver.page_source
        self.result_collector.add_event(dic, page)
    def check_valid_response(self,message, keyword): #to prevent chatgpt respond a non-number call
        try:
            completion = gpt_generation(message)
            choose_number = self.choose(completion, keyword)
            return int(choose_number)
        except:
            return self.check_valid_response(message,keyword)

    def perform_gpt(self):
        content = [ {"role": "user",
                    "content": f"This is a test case description of a particular APP: {self.goal}. You are trying to "
                               f"perform the same step described above to a related APP, an APP that has similar "
                               f"functions but different organizations. Now, you are trying to perform one of the "
                               f"action described in the test case: {self.source_testcase[self.current_step]}. I will "
                               f"provide you the indexes you can perform within the current screen. Please choose the "
                               f"most suitable index in order to imitate the above test case procedures\nIf you can "
                               f"not find an index similar to the events in the test case,choose an index that you "
                               f"think can bring us closer to the events in the original test case or the goal"},
                   {"role": "assistant", "content": "Sure, I'll be happy to help you perform the similar goal on the "
                                                    "related APP. Please provide the actions you've taken before and "
                                                    "the current UI hierarchy information. Once you share that "
                                                    "information, I'll be able to guide you further and suggest the "
                                                    "appropriate index to achieve your goal."}]
        if self.natural_language_actions != "":
            lead = "After these actions, we reach the screen that contains the following indexes:"
        else:
            lead = "Currently, we haven't performed any actions yet. Here are the indexes you can choose to reach our " \
                   "goal:"
        content.append({"role": "user", "content": self.natural_language_actions + lead + self.indexes})
        self.decision_element = self.check_valid_response(content,"index")
        content.append({"role": "assistant", "content": "index" + str(self.decision_element)})
        self.message = content

    def normal_step(self):
        # Pass Welcome Session (Different apps contain distinctive welcome sessions, therefore it is better to
        # preprocess them).
        while not self.finished_welcome:
            current_result = self.finished_welcome_session()
            if current_result:
                self.act_on_welcome()
            else:
                self.finished_welcome = True
        # After passing Welcome Session
        while True:
            # All previously performed actions' descriptions are translated into natural language in the string form
            # (store in self.natural_language_actions)
            self.actions_in_natural_language()
            # If previously there were actions being performed in the target app, check whether these actions are
            # similar to the specific step currently specified by self.current_step. If similar, move to the next
            # specific step. Otherwise, remain in this step.
            if len(self.chose_performance) != 0:
                current_finish = self.checked_if_finished()
                if current_finish:
                    self.current_step += 1
                    #  Once finished imitating all test cases, prompt ChatGPT to assess the accuracy of this test
                    #  case and decide whether to terminate or regenerate.
                    if self.current_step >= len(self.source_testcase):
                        print("This test migration is finished. Check termination...")
                        self.result_collector.save_file()
                        self.termination_judgement()
                        break
            # If the current source testcase action is oracle-based, trying to migrate this oracle to the target APP
            if self.source_testcase[self.current_step]["event_type"] == "oracle":
                act_result, ele = screen_control.act_on_emulator_oracle(
                    self.source_testcase[self.current_step]["action"], driver)
                print(act_result, ele)
                # If the migration achieves
                if act_result:
                    self.send_migrate_result_oracle(ele)
                    lst = [ele, None, self.source_testcase[self.current_step]["action"]]
                    self.chose_performance.append(lst)
                    continue
                # If the migration fails (cannot find the designated resource-id, xpath, etc.), restart the process.
                else:
                    print("Migration is failed. Cannot complete the oracle. Terminate and redo...")
                    self.clear_class()
                    self.normal_step()
            # If the current source testcase action is GUI-based
            # Used to store the current screen's elements in the form of WebElement objects.
            self.element_List = []
            # Store the attributes of the current screen's elements (including their corresponding resource-id, text,
            # class, etc.) in a list. Each index within the list represents an element's information.
            self.get_current_page_info = element_info_extractor.info(driver, self.element_List)
            # Prevent loop by adjusting self.element_List and self.get_current_page_info to ignore multiple invocations.
            self.element_List, self.get_current_page_info = record_history.eliminate_duplications(self.element_List,
                                                                                                  self.get_current_page_info)
            # Format elements information into natural language form for ChatGPT to make selections.
            self.index_list(self.get_current_page_info)
            # Ask ChatGPT to select the most suitable element
            self.perform_gpt()
            # Store this element into the history
            record_history.store(self.element_List, self.element_List[self.decision_element])
            # Request ChatGPT to choose an action on this element.
            self.action, self.text = self.choose_action()
            # Record the action information in the chose_performance variable.
            lst = [self.element_List[self.decision_element], self.get_current_page_info[self.decision_element],
                   [self.possible_actions["action" + str(self.action)]]]
            if 4 <= int(self.action) <= 7:
                lst[-1].append(self.text)
            self.chose_performance.append(lst)
            # generate dic for the testcase
            self.send_migrate_result_gui()
            # Perform action
            screen_control.act_on_emulator_gui(self.action, self.element_List, self.decision_element, self.text)


    def clear_class(self):
        # Restore the class to its original state.
        self.get_current_page_info = None
        self.successful = False
        self.chose_performance = []
        self.finished_welcome = False
        self.current_step = 0
        self.natural_language_actions = ""
        self.indexes = ""
        self.element_List = []
        self.decision_element = 0
        self.message = []

    def termination_judgement(self):
        sys_mes = "Suppose you are performing a binary classification, where you need to judge from a response and a " \
                  "target description to determine whether the target is achieved or not.\n"
        problem_body = f"The target is {goal}.\n The action performed by us is:"
        problem_body += self.natural_language_actions
        prompt = problem_body + "Will the target be achieved after we take the action? Please response with [YES] or " \
                                "[NO].\n Your answer is:"
        messages = [{'role': 'system', 'content': sys_mes}, {'role': 'user', 'content': prompt}]
        response = gpt_generation(messages)
        messages.append({"role": "assistant", "content": response})
        messages.append({"role": "user", "content": "Only answer in [YES] or [NO]"})
        print(response)
        if 'YES' not in response:
            self.clear_class()
            self.normal_step()
        else:
            print("finished!")


if __name__ == "__main__":
    # start appium
    goal, source_testcase = set_goal.comprehend(config.source_path)
    migrate = Migration(goal, source_testcase)
    appium_server = config.appium_server
    desired_caps = config.desired_caps
    driver = webdriver.Remote(appium_server, desired_caps)
    screen_control = control(driver)
    sleep(5)
    record_history = History()
    migrate.normal_step()
