from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
import time

ref_List=(('a13', 'com.stoutner.privacybrowser.standard','com.stoutner.privacybrowser.activities.MainWebViewActivity'),('a14','de.baumann.browser','.Activity.BrowserActivity'),('a15','org.mozilla.focus','.activity.MainActivity'),\
          ('a21', 'com.rubenroy.minimaltodo','.MainActivity'),('a22','douzifly.list','.ui.home.MainActivity'),('a23','org.secuso.privacyfriendlytodolist', '.view.SplashActivity'),('a24','kdk.android.simplydo','.SimplyDoActivity'),('a25','com.woefe.shoppinglist', '.activity.MainActivity'),\
          ('a51','anti.tip','.Tip'),('a52','com.appsbyvir.tipcalculator','.MainActivity',),('a53','com.tleapps.simpletipcalculator', '.MainActivity'),('a54','com.zaidisoft.teninone','.Calculator'),('a55','com.jpstudiosonline.tipcalculator','.MainActivity'),\
          ('Expense1','com.benoitletondor.easybudgetapp','.view.MainActivity'),('Expense2', 'luankevinferreira.expenses','.MainActivity'),('Expense3','com.kvannli.simonkvannli.dailybudget','.MainActivity'),('Expense4','com.blogspot.e_kanivets.moneytracker','.activity.record.MainActivity'),\
          ('abc','com.abc.abcnews','.ui.StartActivity'),('fox','com.foxnews.android','.corenav.StartActivity'),('smartnews','jp.gocro.smartnews.android','activity.SmartNewsActivity'),('theguardian','com.guardian','.feature.stream.NewHomeActivity'),('usatoday','com.usatoday.android.news','com.gannett.android.news.ActivityLoading'),\
          ('Note2','com.moonpi.swiftnotes','.MainActivity'),('Note3','me.writeily','.PromptPinActivity'),('Note4','chan.android.app.pocketnote','.MainActivity'),\
          ('Shop1','pl.com.andrzejgrzyb.shoppinglist','.MainActivity'),('Shop2', 'br.com.activity','br.com.vansact.MainApp'),('Shop3','privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist', '.ui.main.SplashActivity'),('Shop4','org.openintents.shopping', '.ShoppingActivity'),\
          ('5miles', 'com.thirdrock.fivemiles','com.insthub.fivemiles.Activity.GuidePagerActivity'),('geek','com.contextlogic.geek','com.contextlogic.wish.activity.browse.BrowseActivity'),('home','com.contextlogic.home','com.contextlogic.wish.activity.browse.BrowseActivity')) 
for i in ref_List:
    appium_server = 'http://localhost:4723'
    desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'appPackage': i[1],
    'appActivity': i[2],
    'automationName': 'UiAutomator2',
    'noReset': True,
    'forceAppLaunch': True
    }
    try:
        driver = webdriver.Remote(appium_server, desired_caps)
    except:
        print(i)