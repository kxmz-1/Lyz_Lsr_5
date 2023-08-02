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


source = "usatoday_testAbout"
migrate = "smartnews_testAbout"
package_name = "jp.gocro.smartnews.android"
app_activity = ".activity.MainActivity"
gpt_model = "gpt-3.5-turbo-16k"
desired_caps = dict(
    automationName="uiautomator2",
    platformName="Android",  # Operating System
    appPackage=package_name,  # target appPackage
    appActivity=app_activity,  # target appActivity
    noReset=True,
    deviceName='emulator-5554',
    forceAppLaunch=True
)
appium_server = 'http://localhost:4723'
source_path = find_folder("C:\\Users\\swale\\Desktop\\generate\\", source)
#api_key = "sk-obTstm9eJYFBC6DfsBlW6pZ8ue1yfOKkEAZ16GDZApGcNelj"
#api_base = "https://aigptx.top/v1"
api_key = "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"
