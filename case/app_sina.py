# Debug ：2021-05-12
# Status: Pass
# Comment:新浪发布得主入口，区分了mate30与P40
from time import sleep
from appium import webdriver
from Common import time_operate
from Common import get_excel_data
import random
from Common import slide

# 手机usb模式设置为文件模式--P40
# 下方命令需单独命令，不能放在一个py文件中执行--启动运动可以不用带设备ID
# command = "appium -p 4001 -bp 5001 --no-reset --session-override --command-timeout 3000"
# os.system(command)

class AppSina(object):

    '''新浪微博业务层'''

    def __init__(self):
        self.time_op = time_operate.TimeOperate()
        self.get_data = get_excel_data.GetExcelData()

    def get_driver(self):
        capabilities = {
            "platformName": "Android",
            # "deviceName": "JTK5T19916007835",     # 单台设备运行，可不指定
            "appActivity": "com.sina.weibo.MainTabActivity",  # appium1.7版本之后就应该不需要改配置了;这里报错很多次，因为activity名字错误，aapt检查出来
            "appPackage": "com.sina.weibo",
            "noReset": "true"
        }
        driver = webdriver.Remote("http://127.0.0.1:4001/wd/hub", capabilities)
        return driver
    

    def add_article(self, title, content, camery,edu_mode):
        '''
        新增微评
        :return:
        '''
        driver = self.get_driver()          # 不能放到初始化中，否则变成单app执行
        sleep(10)
        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.sina.weibo:id/titleSave")').click()
        self.time_op.sleep_random()
        driver.find_element_by_android_uiautomator('new UiSelector().text("微评")').click()
        self.time_op.sleep_random()

        # # 这里要滑动一下，解决输入发问题
        # self.slide.swip_up()
        # sleep(3)
        self.micro_review(driver,title, content, camery,edu_mode)

    def micro_review(self,driver,title, content, camery,edu_mode):
        '''
        微评具体内容填充
        :param driver:
        :param title:
        :param content:
        :param camery:
        :return:
        '''
        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.sina.weibo:id/iv_edit_pic")').click()
        self.time_op.sleep_random()
        # 点击相册
        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.sina.weibo:id/photo_album_title_icon")').click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("test")').click()
        # 选择照片,注意这里的多个结果，该使用什么方法和定位

        #选择随机图片
        # num = driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.sina.weibo:id/photo_album_grideview_item_select")').count()
        rand_pic = random.randint(0,3)
        driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.sina.weibo:id/photo_album_grideview_item_select")')[rand_pic].click()
        self.time_op.sleep_random(2,5)
        driver.find_element_by_android_uiautomator('new UiSelector().text("下一步(1)")').click()
        self.time_op.sleep_random(3,5)
        driver.find_element_by_android_uiautomator('new UiSelector().text("下一步(1)")').click()
        self.time_op.sleep_random(3,5)
        driver.find_element_by_android_uiautomator('new UiSelector().text("选择")').click()
        self.time_op.sleep_random()
        driver.find_element_by_android_uiautomator('new UiSelector().text("搜索物品、电影、地点...")').click()
        self.time_op.sleep_random()
        driver.find_element_by_android_uiautomator('new UiSelector().text("搜索物品、电影、地点...")').send_keys(edu_mode)
        sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("点击添加物品话题")').click()
        self.time_op.sleep_random()
        ##############################卡在这里得评价了，才能下一步#############################
        driver.find_element_by_xpath("//android.widget.ImageView[@index='4']").click()
        self.time_op.sleep_random()
        driver.find_element_by_android_uiautomator('new UiSelector().text("分享你的体验和真实评价，可以帮助更多小伙伴~")').click()
        self.time_op.sleep_random()
        driver.find_element_by_android_uiautomator('new UiSelector().text("分享你的体验和真实评价，可以帮助更多小伙伴~")').send_keys(
            content)
        # 这里看是否要切换到frame
        # self.time_op.sleep_random()
        # driver.find_element_by_android_uiautomator('new UiSelector().text("添加标题")').click()
        # self.time_op.sleep_random()
        # driver.find_element_by_android_uiautomator('new UiSelector().text("填写标题")').send_keys(title)
        sleep(3)
        driver.find_element_by_id("com.sina.weibo:id/titleSave").click()
        self.time_op.sleep_random()

    def add_article_02(self, title, content, camery,edu_mode):
        '''
        新增文章
        :return:
        '''
        driver = self.get_driver()
        sleep(10)
        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.sina.weibo:id/titleSave")').click()
        self.time_op.sleep_random()
        driver.find_element_by_android_uiautomator('new UiSelector().text("写微博")').click()
        self.time_op.sleep_random(5,8)
        driver.find_element_by_id("com.sina.weibo:id/ib_add_app").click()       # 点击更多
        self.time_op.sleep_random()
        # # # 这里要滚动一下，解决输入发问题
        # start_element = driver.find_element_by_xpath("//android.widget.RelativeLayout[@index='3']")
        # end_element = driver.find_element_by_xpath("//android.widget.RelativeLayout[@index='0']")
        # driver.scroll(start_element, end_element, 300)  # 从A元素滚动到B元素，这里不可行
        # 滑动一下  仅针对mate30 2k分辨率
        driver.swipe(500,2200,500,1600,100)
        # self.swip_up()  不知道为什么滑动失败
        self.time_op.sleep_random()
        # 选择微评
        driver.find_element_by_android_uiautomator('new UiSelector().text("微评")').click()
        self.time_op.sleep_random()
        self.micro_review(driver,title, content, camery, edu_mode)

    def get_size(self):
        '''
        获取屏幕宽，高
        :return:
        '''
        driver = self.get_driver()
        size = driver.get_window_size()
        width = size['width']
        height = size['height']
        return width,height

    def swip_up(self):
        '''
        向上滑动
        :return:
        '''
        x = self.get_size()[0] / 10 * 5
        y = self.get_size()[1] / 10 * 6
        y1 = self.get_size()[1] / 10 * 9
        self.get_driver().swipe(x, y1, x, y, 100)

    def send_chap(self,case):
        '''
        发布微评
        :return:
        '''
        # self.appium_init()
        # sleep(10)
        app, app_activity, title, content, camery,edu_mode = self.get_data.app_data(case)
        content = content + '\n 详情咨询陈老师  电话(微信)：18180734223'
        self.add_article(title, content, camery,edu_mode)
        self.time_op.sleep_random()  # 这里不等待时间很有可能两个滑动至生效一个

    def send_chap_02(self,case):
        '''
        发布文章
        :return:
        '''
        # self.appium_init()
        # sleep(10)
        app, app_activity, title, content, camery,edu_mode = self.get_data.app_data(case)
        content = content + '\n 详情咨询李老师  电话(微信)：15008499834'
        self.add_article_02(title, content, camery,edu_mode)
        self.time_op.sleep_random()  # 这里不等待时间很有可能两个滑动至生效一个

if __name__ == '__main__':
    driv = AppSina()
    # driv.send_chap()
    # driv.send_chap_02()