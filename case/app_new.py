# Debug ：2021-05-13
# Status: Block
from time import sleep
from appium import webdriver
from Common import time_operate
from Common import get_excel_data
from Common import appium_start
import random


class AppNew(object):

    '''今日头条业务层'''

    def __init__(self):
        self.time_op = time_operate.TimeOperate()
        driver = self.get_driver()
        self.get_data = get_excel_data.GetExcelData()

    def get_driver(self):
        capabilities = {
            "platformName": "Android",
            # "deviceName": "JTK5T19916007835",     # 单台设备运行，可不指定
            "appActivity": "com.ss.android.article.lite.activity.SplashActivity",  # appium1.7版本之后就应该不需要改配置了;这里报错很多次，因为activity名字错误，aapt检查出来
            "appPackage": "com.ss.android.article.lite",
            "noReset": "true"
        }
        driver = webdriver.Remote("http://127.0.0.1:4001/wd/hub", capabilities)
        return driver

    def add_article(self,title,  content,edu_mode,*args,**kwargs):
        '''
        新增文章
        :return:
        '''
        driver = self.get_driver()
        sleep(8)
        driver.find_element_by_id("com.ss.android.article.lite:id/b2p").click()        # 发布
        self.time_op.sleep_random(3,5)
        driver.find_element_by_android_uiautomator('new UiSelector().text("文章")').click()   # 文章
        self.time_op.sleep_random()

        tit = driver.find_element_by_xpath("//android.widget.EditText[@index='0']")
        tit.click()      #标题
        self.time_op.sleep_random()
        tit.send_keys(title)     # 输入标题
        self.time_op.sleep_random()
        con = driver.find_element_by_android_uiautomator('new UiSelector().text("请输入正文")')                      # 正文
        con.click()
        self.time_op.sleep_random()

        driver.find_element_by_id("com.ss.android.newugc:id/image_btn").click()                  #进入相册界面
        self.time_op.sleep_random()

        driver.find_element_by_id("com.ss.android.article.lite:id/bp").click()                   # 点击相册
        self.time_op.sleep_random()
        driver.find_element_by_xpath("//android.widget.TextView[@text='test']").click()          # 选择固定相册
        self.time_op.sleep_random()
        rand_pic = random.randint(0, 6)             # 注意固定了个数的
        # sum = driver.find_elements(By.id("com.ss.android.newugc:id/image_view"))           #获取元素个数失败
        # print(sum)
        driver.find_elements_by_id("com.ss.android.newugc:id/image_album_check_circle")[rand_pic].click()
        self.time_op.sleep_random(5, 10)
        driver.tap([(861,225),(1008,2259)],100)      # 这里模拟点击，指定分辨率，仅适配华为手机
        self.time_op.sleep_random()
        # driver.find_element_by_xpath("//android.widget.EditText[@text='编辑']/android.view.View[0]").send_keys(content)       # 内容编辑 寻找元素失败
        driver.find_elements_by_xpath("//android.widget.EditText[@text='编辑']/android.view.View[0]").send_keys(content)       # 内容编辑
        self.time_op.sleep_random()
        driver.find_element_by_id("com.ss.android.newugc:id/tv_publish").click()               # 下一步
        self.time_op.sleep_random()
        driver.find_elements_by_id("com.ss.android.newugc:id/setting_switcher")[0].click()     # 声明原创，这里内容如果重复，申请会失败，注意
        self.time_op.sleep_random()
        driver.find_element_by_id("com.ss.android.newugc:id/btn_publish").click()              # 发布
        self.time_op.sleep_random()


    def send_chap(self, case):
        '''
        滑动浏览视频
        :return:
        '''
        # self.appium_init()
        app, app_activity, title, content, camery, edu_mode = self.get_data.app_data(case)
        content = content + '\n 详情咨询李老师  电话(微信)：15008499834'
        self.add_article(title, content,edu_mode)
        self.time_op.sleep_random()  # 这里不等待时间很有可能两个滑动至生效一个


if __name__ == '__main__':
    driv = AppNew()
    driv.send_chap()