import os

import os, json
ref_List=(('a13', 'com.stoutner.privacybrowser.standard','com.stoutner.privacybrowser.activities.MainWebViewActivity'),('a14','de.baumann.browser','.Activity.BrowserActivity'),('a15','org.mozilla.focus','.activity.MainActivity'),\
          ('a21', 'com.rubenroy.minimaltodo','.MainActivity'),('a22','douzifly.list','.ui.home.MainActivity'),('a23','org.secuso.privacyfriendlytodolist', '.view.SplashActivity'),('a24','kdk.android.simplydo','.SimplyDoActivity'),('a25','com.woefe.shoppinglist', '.activity.MainActivity'),\
          ('a51','anti.tip','.Tip'),('a52','com.appsbyvir.tipcalculator','.MainActivity',),('a53','com.tleapps.simpletipcalculator', '.MainActivity'),('a54','com.zaidisoft.teninone','.Calculator'),('a55','com.jpstudiosonline.tipcalculator','.MainActivity'),\
          ('Expense1','com.benoitletondor.easybudgetapp','.view.MainActivity'),('Expense2', 'luankevinferreira.expenses','.MainActivity'),('Expense3','com.kvannli.simonkvannli.dailybudget','.MainActivity'),('Expense4','com.blogspot.e_kanivets.moneytracker','.activity.record.MainActivity'),\
          ('abc','com.abc.abcnews','.ui.StartActivity'),('fox','com.foxnews.android','.corenav.StartActivity'),('smartnews','jp.gocro.smartnews.android','activity.SmartNewsActivity'),('theguardian','com.guardian','.feature.stream.NewHomeActivity'),('usatoday','com.usatoday.android.news','com.gannett.android.news.ActivityLoading'),\
          ('Note2','com.moonpi.swiftnotes','.MainActivity'),('Note3','me.writeily','.PromptPinActivity'),('Note4','chan.android.app.pocketnote','.MainActivity'),\
          ('Shop1','pl.com.andrzejgrzyb.shoppinglist','.MainActivity'),('Shop2', 'br.com.activity','br.com.vansact.MainApp'),('Shop3','privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist', '.ui.main.SplashActivity'),('Shop4','org.openintents.shopping', '.ShoppingActivity'),\
          ('5miles', 'com.thirdrock.fivemiles','com.insthub.fivemiles.Activity.GuidePagerActivity'),('geek','com.contextlogic.geek','com.contextlogic.wish.activity.browse.BrowseActivity'),('home','com.contextlogic.home','com.contextlogic.wish.activity.browse.BrowseActivity'))
#appname,app package,app activity

cat=('a2','a5','News','shop2')
class ticker(object):
    def __init__(self,cat):
        self.pointer=0
        self.cat=cat
        self.path='..\\dateset pairing\\'+cat+'_meta.json'
        self.dataset=json.load(open(self.path))
        self.is_finished=False
        return
    def update_status(self):
        self.pointer += 1
        if self.pointer >= len(self.dataset['data']):
            self.is_finished = True
    def get_finish(self):
        return self.is_finished
    def get_current(self):
        return self.dataset['data'][self.pointer]


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


source = ""
migrate = ""
package_name = ""
app_activity = ""
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
appium_server = 'http://localhost:4723'
ground = "..\\generate"
source_path = ""
api_key = "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"
save_file = "..\\"
num = 3