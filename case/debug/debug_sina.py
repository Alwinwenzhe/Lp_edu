# Debug_time:  2020-12-01
# Status: PASS

# 下方命令需单独命令，不能放在一个py文件中执行--启动运动可以不用带设备ID
# command = "appium -p 4001 -bp 5001 --no-reset --session-override --command-timeout 3000
# "
# os.system(command)

from appium import webdriver
from time import sleep
from datetime import datetime
import random

class DebugSina(object):

    def __init__(self):
        self.driver = self.get_driver()

    def get_driver(self):
        capabilities ={
            "platformName": "Android",
            #"deviceName": "JTK5T19916007835",
            "appActivity" : "com.sina.weibo.MainTabActivity",        #appium1.7版本之后就应该不需要改配置了;这里报错很多次，因为activity名字错误，aapt检查出来
            "appPackage": "com.sina.weibo",
            "noReset":"true"
        }
        driver = webdriver.Remote("http://127.0.0.1:4001/wd/hub",capabilities)
        return driver

    def sleep_random(self):
        '''
        等待等待时间
        :return:
        '''
        sleep_time = random.randrange(1,20)
        return sleep_time

    def get_time(self):
        '''
        获取当前时间戳
        :return:
        '''
        return datetime.now(self)

    def time_compare_1(self):
        '''
        时间对比
        :return:
        '''
        t1 = self.get_time()
        t3 = 0
        while t3 < 1280:
            self.operate()
            t2 = self.get_time()
            t3 = t2 - t1
        else:
            self.operator_coin()
            t3 = 10

    def add_article(self):
        '''
        新增文章
        :return:
        '''
        sleep(10)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.sina.weibo:id/titleSave")').click()
        sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("微评")').click()
        sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("种草生活好物，你的真实体验可以帮助更多人～")').click()
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("种草生活好物，你的真实体验可以帮助更多人～")').send_keys("今天又花了4099元\n要努力赚钱呀！")
        #这里看是否要切换到frame
        sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.sina.weibo:id/iv_edit_pic")').click()
        sleep(1)
        #点击相册
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.sina.weibo:id/photo_album_title_icon")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("test")').click()
        # 选择照片,注意这里的多个结果，该使用什么方法和定位
        self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.sina.weibo:id/photo_album_grideview_item_select")')[0].click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("下一步(1)")').click()
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("下一步(1)")').click()
        sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("添加标题")').click()
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("填写标题")').send_keys("花钱真爽")
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("选择")').click()
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("搜索物品、电影、地点...")').click()
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("搜索物品、电影、地点...")').send_keys("自考")
        sleep(3)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("点击添加物品话题")').click()
        sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.sina.weibo:id/titleSave")').click()
        sleep(10)

    def operate(self):
        '''
        滑动浏览视频
        :return:
        '''
        self.add_article()
        sleep(self.sleep_random())  # 这里不等待时间很有可能两个滑动至生效一个

if __name__ == '__main__':
    driver = DebugSina()
    driver.operate()

