import os


def find_folder(folder_path, target_folder_name):
    contents = os.listdir(folder_path)
    for item in contents:
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            if item == target_folder_name:
                return item_path
            result = find_folder(item_path, target_folder_name)
            if result is not None:
                return result
    return None


source = "a21"
migrate = "a24"
package_name = "kdk.android.simplydo"
app_activity = ".SimplyDoActivity"
gpt_model = "gpt-3.5-turbo-16k"
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'forceAppLaunch': True,
    'noReset' : True,
    'appPackage': '',
    'appActivity': ''
}
desired_caps['appPackage'] = package_name
desired_caps['appActivity'] = app_activity
appium_server = 'http://localhost:4723'
source_path = find_folder("C:\\Users\\11303\\Desktop\\git\\Lyz_Lsr_5\\generate", source)
#api_key = "sk-obTstm9eJYFBC6DfsBlW6pZ8ue1yfOKkEAZ16GDZApGcNelj"
#api_base = "https://aigptx.top/v1"
api_key = "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"
save_file = "C:\\Users\\11303\\Desktop\\git\\Lyz_Lsr_5\\"
num = 1