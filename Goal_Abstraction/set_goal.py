import xml.etree.ElementTree as ET
import os
import json
from openai import OpenAI
import config
import re
os.environ["OPENAI_API_KEY"] = config.api_key
def gpt_generation(messages):
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
        temperature=0.2,
    )
    return completion.choices[0].message.content


def extract_elements_with_conditions(node, layout, current_level=0):
    element_info = {}
    # Check if the element has 'text' attribute and it is not empty
    text = node.attrib.get('text', '')
    if text != '':
        element_info['text'] = text
    # Check if the element has 'clickable' attribute, and it is set to 'true'
    clickable = node.attrib.get('clickable', '').lower()
    if clickable == 'true':
        element_info['clickable'] = True

    long_clickable = node.attrib.get('long-clickable', '').lower()
    if long_clickable == 'true':
        element_info['long-clickable'] = True

    checkable = node.attrib.get('checkable', '').lower()
    if checkable == 'true':
        element_info['checkable'] = True

    scrollable = node.attrib.get('scrollable', '').lower()
    if scrollable == 'true':
        element_info['scrollable'] = True

    # Store the 'resource-id' attribute if it exists
    resource_id = node.attrib.get('resource-id', None)
    if element_info != {} and resource_id:
        element_info['resource-id'] = resource_id
        if "/" in resource_id:
            element_info['resource-id'] = resource_id.split('/')[-1]
            element_info['resource-id'] = resource_id.replace('_', ' ')
        #    if element_info != {}:
        #        bounds = node.attrib.get('bounds', "")
        #        element_info['bounds'] = bounds
        # Add the element info to the layout for the current level
        layout.setdefault(current_level, []).append(element_info)

    # Recursively process child elements
    for child in node:
        extract_elements_with_conditions(child, layout, current_level + 1)


def get_xml_files(xml_folder_path):
    xml_files = []
    for file_name in os.listdir(xml_folder_path):
        # Check if the file has '.xml' extension
        if file_name.endswith('.xml'):
            file_path = os.path.join(xml_folder_path, file_name)
            xml_files.append(file_path)
    return xml_files


def process_json(json_file_path):
    for file_name in os.listdir(json_file_path):
        # Check if the file has '.json' extension
        print(file_name)
        if file_name.endswith('.json'):
            print(file_name)
            file_path = os.path.join(json_file_path, file_name)
    with open(file_path, 'rb') as json_file:
        data = json.load(json_file)
    processed_data = []
    for entry in data:
        # Remove empty values (text:'' and content-desc:'')
        entry = {key: value for key, value in entry.items() if value not in ['', '']}
        if "resource-id" in entry:
            entry['resource-id'] = entry['resource-id'].split('/')[-1]
            entry['resource-id'] = entry['resource-id'].replace('_', ' ')
        # Exclude 'ignorable', 'tid', and 'password' fields
        entry.pop('ignorable', None)
        entry.pop('tid', None)
        entry.pop('password', None)
        print(entry)
        processed_data.append(entry)
    return processed_data


def remove_consecutive_duplicates(layout):
    new_layout = {}
    for level, elements in layout.items():
        new_elements = []
        current_resource_id = None
        resource_id_count = 0

        for element in elements:
            resource_id = element.get('resource-id')
            if resource_id == current_resource_id:
                resource_id_count += 1
            else:
                current_resource_id = resource_id
                resource_id_count = 1

            if resource_id_count <= 5:
                new_elements.append(element)
            elif resource_id_count == 6:  # Remove the previous four occurrences when count reaches 6
                new_elements = new_elements[:-5]
        new_layout[level] = new_elements

    return new_layout


def xml_files_enum(xml_files):
    layout = []
    for file in xml_files:
        # Parse the XML file
        tree = ET.parse(file)
        root = tree.getroot()

        # Initialize the layout dictionary
        layout_min = {}

        # Start extracting elements with conditions
        extract_elements_with_conditions(root, layout_min)
        layout_min = remove_consecutive_duplicates(layout_min)
        # Print the hierarchical layout
        layout.append(layout_min)
    return layout


def templating(content_organized):
    content = ""
    for level, elements in content_organized.items():
        for element in elements:
            content += str(level * '\t') + str(element) + "\n"
    return content


def gpt_content(layout, processed_data):
    length = len(processed_data)
    sentence = ""
    for i in range(length):
        sentence += "This is the current UI Hierarchy. Indentation refers to the level of hierarchy:\n"
        sentence += str(templating(layout[i])) + "\n"
        sentence += "Now, we execute this event within the current UI Hierarchy:\n"
        sentence += str(processed_data[i]) + "\n"
    sentence += "This is the final UI Hierarchy. Indentation refers to the level of hierarchy:\n"
    try:
        sentence += str(templating(layout[length])) + "\n"
        sentence += "Can you explain the intention of this test case to me?"
    except:
        sentence += "Can you explain the intention of this test case to me?"
    return sentence


def comprehend(provide_path, num):
    # Replace 'your_file.xml' with the path to your XML file
    path = provide_path

    xml_files = get_xml_files(path)
    layout = xml_files_enum(xml_files)
    processed_data = process_json(path)
    display = gpt_content(layout, processed_data)
#    return "The goal of this test case is to verify the successful addition of a new to-do item in the Minimal Todo app and its proper display on the main page.", ['Click on the "Add To-Do Item" floating action button', 'Enter the text "Sample Todo" in the "Title" field', 'Click on the "Make To-Do" floating action button', 'Wait until the element with the text "Sample Todo" is present on the main page'],processed_data
    print(display)
    message = [
        {"role": "system",
         "content": "You are an UI testing android expert. You are here to assist me to understand the intention of a "
                    "test case that is performed on an app."},
        {"role": "user",
         "content": "A test case contains multiple events that is performed on UI elements on a UI Hierarchy. Now, "
                    "I will provide you a test case with events and their corresponding UI hierarchy. You have to "
                    "know the goal of this test case, and explain it to me through simple sentences."
                    "I will organize it into: The current page of UI Hierarchy, the action, the following page of UI "
                    "Hierarchy, the action, the next page of UI Hierarchy, and so on..... OK?"},
        {"role": "assistant",
         "content": "Absolutely, that sounds like a structured way to convey the information. Please go ahead and "
                    "provide the test case along with the corresponding events' UI hierarchy in the format you "
                    "mentioned:\nCurrent page of UI Hierarchy\nAction\nFollowing page of UI Hierarchy\nAction"},
        {"role": "user", "content": display}
    ]
    completion = gpt_generation(message)
    message.append({"role": "assistant", "content": completion})
    # Only Goal Abstraction
    if num == 0 or num == 1 or num == 3:
        message.append({"role": "user",
                        "content": "Summarize the overall test case's goal within one sentence without "
                                   "listing and providing specific attributes' name"})
        completion = gpt_generation(message)
    del message[-1]

    if num == 1:
        message.append({"role": "user",
                        "content": "Provide me a rough description on the whole process through splitting it into"
                                   "major parts. Two or three actions may regard as one major part. "
                                   "Transform into a python list: ['<major_part_1>','<major_part2>'...]. Make sure it"
                                   "doesn't contain specific attributes' name. "})
    # Goal with step
#    if num == 2:
#        message.append({"role": "user",
#                        "content": "Summarize the overall test case's goal while referencing the"
#                                   "description on the UI events so I can perform these procedures in another "
#                                   "APP with different attributes' name"})


    # Goal+detailed step intention
    if num == 3:
        message.append({"role": "user",
                        "content": "List each event action's function and intention in reaching the goal. Transform into a python list "
                                   "['<function_and_intention_1>','<function_and_intention_2>'...] Make sure it"
                                   "doesn't contain specific attributes' name"})

    if num != 0 and num != 2:
        completion_2 = gpt_generation(message)
    else:
        completion_2 = None
    if num == 2:
        completion = gpt_generation(message)
    print(completion, completion_2)
    if completion_2 != None:
        list_str = re.findall(r'\[.*?\]', completion_2, re.DOTALL)
        completion_2 = eval(list_str[0]) if list_str else []
    print(completion, completion_2)
    return completion, completion_2, processed_data
