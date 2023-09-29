base_directory = "C:\\Users\\11303\\Desktop\\generate"
filename = "C:\\Users\\11303\\Desktop\\Analyze migration pairs.xlsx"  

import pandas as pd
import os
import json
import xml.etree.ElementTree as ET
def find_folders_with_name(target_string, root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            if target_string in dirname:
                return os.path.join(dirpath, dirname)
def read_excel_columns(filename):
    df = pd.read_excel(filename)
    column_1 = []
    column_3 = []
    for index, row in df.iterrows():
        col3_value = str(row.iloc[2]).strip() 
        if col3_value != 'nan':  
            col1_value = [item.strip() for item in str(row.iloc[0]).split("-")]
            col3_split = [item.strip() for item in col3_value.split(",")]

            column_1.append(col1_value)
            column_3.append(col3_split)
    return column_1, column_3

def extract_elements_with_conditions(node, layout, current_level=0):
    element_info = {}
    text = node.attrib.get('text', '')
    if text != '':
        element_info['text'] = text
    content_desc = node.attrib.get("content-desc",'')
    if content_desc != "":
        element_info["content-desc"]=content_desc
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
    if element_info != {} and not(len(element_info)==1 and "clickable" in element_info):
        layout.setdefault(current_level, []).append(element_info)
        
    for child in node:
        extract_elements_with_conditions(child, layout, current_level + 1)

        
def find_and_read_json(dir_path, index):
    target_name = os.path.basename(dir_path) + ".json"
    for filename in os.listdir(dir_path):
        if filename == target_name:
            json_path = os.path.join(dir_path, filename)
            with open(json_path, 'r',encoding='utf-8') as f:
                data = json.load(f)   
                if index < len(data):
                    return data[index]

def find_and_read_xml(dir_path, index):
    target_filename="hierarchy"+str(index) + ".xml"
    xml_path = os.path.join(dir_path, target_filename)
    if os.path.exists(xml_path):
        tree = ET.parse(xml_path)
        root = tree.getroot()
        layout_min = {}
        extract_elements_with_conditions(root, layout_min)
    else:
        return False
    content = ""
    for level, elements in layout_min.items():
        for element in elements:
            content += str(level * '\t') + str(element) + "\n"
    return content


name, match = read_excel_columns(filename)
path = []
for i in range(len(name)):
    path1 = find_folders_with_name(name[i][0], base_directory)
    path2 = find_folders_with_name(name[i][1], base_directory)
    path.append([path1, path2])

lst = []
for i in range(len(path)):
    for j in range(len(match[i])):
        source = find_and_read_json(path[i][0],int(match[i][j][0])-1)
        target = find_and_read_xml(path[i][1], int(match[i][j][2])-1)
        if target != False:
            lst.append(f"This is the source event: \n{source}\n Please choose the widget that can imitate the source event. Here is the UI-Hierarchy of the target screen\n{target}.\n")
print(lst)
with open('output.txt', 'w',encoding='utf-8') as file:
    for element in lst:
        file.write(element + '\n\n')
