from bs4 import BeautifulSoup
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import StaleElementReferenceException
import time
import ast

def process(dom, element):
    soup = BeautifulSoup(dom, 'lxml')
    cond = {'resource-id': element.get_attribute('resourceId'), 'class': element.get_attribute('class'),
            'content-desc': element.get_attribute('content-desc'), 'text': element.get_attribute('text')}
    ele = soup.find(attrs=cond)
    return ele


def get_child_text(element):
    result = []
    children_elements = element.find_elements(MobileBy.XPATH, ".//*")
    for child_element in children_elements:
        if child_element.text != "":
            result.append(child_element.text)
    return result


def get_parent_text(soup_ele):
    parent_text = ""
    parent = soup_ele.find_parent()
    if parent and 'text' in parent.attrs and parent['text']:
        parent_text += parent['text']
    # consider grandparent if it's TextInputLayout (for ? related apps)
    parent = parent.find_parent()
    if parent and 'text' in parent.attrs and parent['text'] and parent['class'][0] == 'TextInputLayout':
        parent_text += parent['text']
    return parent_text


def get_sibling_text(soup_ele):
    # (for Tip related apps)
    # consider immediate previous sibling text if exists and the parent is LinearLayout
    sibling_text = ''
    parent = soup_ele.find_parent()
    if parent and parent.name in ['android.widget.LinearLayout',
                                  'android.widget.relativelayout']:  # 使用 .name 属性来获取元素的标签名
        prev_sib = soup_ele.find_previous_sibling()
        if prev_sib:  # 添加类型检查，确保处理的是元素节点
            if 'text' in prev_sib.attrs and prev_sib['text']:
                sibling_text = prev_sib['text']
    return sibling_text


def remove_duplicate_resource_id(data_list):
    count = 1
    last_resource_id = None
    new_data_list = []
    # Iterate through the list of dictionaries
    for i in range(len(data_list)):
        new_data_list.append(data_list[i].copy())
        if 'resource_id' in new_data_list[i]:
            current_resource_id = new_data_list[i]['resource_id']
        else:
            current_resource_id = None
        if current_resource_id == last_resource_id and current_resource_id is not None:
            count += 1
        else:
            if count >= 5:
                new_data_list = new_data_list[:-count - 1] + [new_data_list[-1]]
            count = 1
        last_resource_id = current_resource_id
    print(new_data_list)
    return new_data_list


def get_element_info(driver, element, element_info):
    # Initialize child_texts here for each call
    process_result = process(driver.page_source, element)
    parent_text = get_parent_text(process_result)
    # sibling_text = get_sibling_text(process_result)
    child_text = get_child_text(element)
    if element.get_attribute("content-desc") is not None:
        element_info["content-desc"] = element.get_attribute("content-desc")
    if element.text != "":
        element_info['text'] = element.text.strip()
    if element.get_attribute("class") != "":
        element_info['class'] = element.get_attribute("class")
    if element.get_attribute('resourceId') and "/" in element.get_attribute('resourceId'):
        element_info['resource_id'] = element.get_attribute('resourceId').split('/')[-1].replace('_', ' ')
    if parent_text != '':
        element_info['parent_text'] = parent_text
    #   if sibling_text != '':
    #       element_info['sibling_text'] = sibling_text
    if len(child_text) > 0:
        element_info['child_text'] = child_text
    return element_info

def parse_string_to_list(string_with_bounds):
    try:
        # Fix the input string by adding a comma between the two sublists
        fixed_string = string_with_bounds.replace("][", "],[")
        # Convert the fixed string to a Python object using ast.literal_eval
        parsed_list = ast.literal_eval(fixed_string)

        if not isinstance(parsed_list, list) or len(parsed_list) != 2:
            raise ValueError("Input should be a string representation of a list containing two sublists.")

        for sublist in parsed_list:
            if not isinstance(sublist, list) or len(sublist) != 2:
                raise ValueError("Sublists should contain exactly two elements each.")

            for element in sublist:
                if not isinstance(element, int):
                    raise ValueError("Elements in the sublists should be integers.")

        return parsed_list

    except (ValueError, SyntaxError):
        raise ValueError(
            "Invalid input format. Please provide a valid string representation of a list containing two sublists.")

def info(driver, element_list):
    time.sleep(10)
    elements = driver.find_elements(MobileBy.XPATH, "//*")
    overall = []
    for element in elements:
        try:
            element_info = {}
            if element.is_displayed() and element.get_attribute("clickable") == "true":
                element_info["clickable"] = True
            if element.is_displayed() and element.get_attribute("scrollable") == "true":
                element_info["scrollable"] = True
                element_info["bounds"] = parse_string_to_list("["+element.get_attribute("bounds")+"]")
            if element.is_displayed() and element.get_attribute("long-clickable") == "true":
                element_info["long-clickable"] = True
            if element.is_displayed() and element.get_attribute("checked") == "true":
                element_info["checked"] = True
            if element.is_displayed() and element.get_attribute("class") == "android.widget.EditText":
                element_info["fillable"] = True
            if len(element_info) > 0:
                element_list.append(element)
                element_info = get_element_info(driver, element, element_info)
                overall.append(element_info)
        except StaleElementReferenceException:
            pass
    overall = remove_duplicate_resource_id(overall)
    print(overall)
    return overall
