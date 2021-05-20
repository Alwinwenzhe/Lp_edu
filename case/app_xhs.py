
# Debug ：2020-12-05
# Status: Block
# Comment: 注意运行前必须打开定位功能
from time import sleep
from appium import webdriver
from Common import time_operate
from Common import get_excel_data
from Common import appium_start
from Common import doc_cmd
import random


class XHS(object):
    '''小红书'''
    

    def __init__(self):
        self.time_op = time_operate.TimeOperate()
        # driver = self.get_driver()
        self.get_data = get_excel_data.GetExcelData()
        self.appium_init = appium_start.AppiumStart()
        self.doc = doc_cmd.Doc_Cmd()

    def get_driver(self):
        '''
        如果要测试不同得app这里不能预加载，否则只能执行最后一个；
        或者以参数传递形式解决问题
        :return:
        '''
        capabilities = {
            "platformName": "Android",
            # "deviceName": "JTK5T19916007835",     # 单台设备运行，可不指定
            "appActivity": "com.xingin.xhs.activity.SplashActivity",  # appium1.7版本之后就应该不需要改配置了;这里报错很多次，因为activity名字错误，aapt检查出来
            "appPackage": "com.xingin.xhs",
            "noReset": "true"
        }
        driver = webdriver.Remote("http://127.0.0.1:4001/wd/hub", capabilities)
        return driver

    def add_article(self,title, content, camery,edu_mode, *args, **kwargs):
        '''
        新增文章
        :return:
        '''
        driver = self.get_driver()
        sleep(10)
        driver.tap(([535,2280],[550,2320]),duration=100)   #进入相册，仅适配华为
        self.time_op.sleep_random()
        driver.find_element_by_id("com.xingin.xhs:id/hj").click()                                      # 添加进入
        self.time_op.sleep_random()
        driver.find_element_by_xpath("//android.widget.TextView[@text='test']").click()                # 选择相册
        self.time_op.sleep_random(4,6)
        rand_pic = random.randint(0,6)
        # 查找特点节点的子节点的弟弟节点的子节点
        driver.find_elements_by_xpath("//androidx.recyclerview.widget.RecyclerView[@index='2']/android.widget.FrameLayout/android.widget.RelativeLayout/"
                                           "android.widget.ImageView/following-sibling::android.widget.RelativeLayout/android.widget.ImageView")[rand_pic].click()      # 点击图片
        self.time_op.sleep_random()
        # driver.find_element_by_id("com.xingin.xhs:id/e1r").click()                                     # 勾选图片
        # self.time_op.sleep_random()
        driver.find_element_by_xpath("//android.widget.TextView[@text='下一步(1)']").click()          # 下一步
        self.time_op.sleep_random()
        driver.find_element_by_xpath("//android.widget.ImageView[@index='2']").click()                 # 继续下一步
        self.time_op.sleep_random()
        driver.find_element_by_xpath("//android.widget.TextView[@text='参与话题']").click()            # 话题
        self.time_op.sleep_random()
        # driver.find_element_by_xpath("//android.widget.EditText[@text='搜索更多话题']").send_keys("edu_mode")        #编辑话题
        driver.find_element_by_xpath("//android.widget.EditText[@text='搜索更多话题']").send_keys(edu_mode)        #编辑话题
        self.time_op.sleep_random()
        driver.find_element_by_xpath("//androidx.recyclerview.widget.RecyclerView[@index='0']/android.widget.RelativeLayout[@index='0']").click()  # 预览第一个
        self.time_op.sleep_random()
        driver.find_element_by_xpath("//android.widget.TextView[@text='添加地点']/following-sibling::android.widget.ImageView").click()           # 点击添加地点
        self.time_op.sleep_random()
        sea = driver.find_element_by_xpath("//android.widget.EditText[@text='搜索地点']")
        sea.click()
        sea.send_keys("成都理工大学")                                    # 搜索地点
        self.time_op.sleep_random()
        driver.find_element_by_xpath("//androidx.recyclerview.widget.RecyclerView[@index='2']/android.widget.RelativeLayout[@index='1']").click()   # 点击第一个
        self.time_op.sleep_random()
        tit=driver.find_element_by_xpath("//android.widget.EditText[@text='填写标题会有更多赞哦～']")
        tit.click()
        self.time_op.sleep_random()
        tit.send_keys(title)
        self.time_op.sleep_random()
        con = driver.find_element_by_xpath("//android.widget.EditText[@text='添加正文']")
        con.click()
        self.time_op.sleep_random()
        con.send_keys(content)
        self.time_op.sleep_random()
        driver.find_element_by_xpath("//android.widget.TextView[@text='完成']").click()                                                            # 完成内容编辑
        self.time_op.sleep_random()
        driver.find_element_by_id("com.xingin.xhs:id/w0").click()                                                                                  # 发布笔记
        self.time_op.sleep_random()
        driver.find_element_by_xpath("//android.widget.TextView[@text='取消']").click()                                                            # 取消分享
        self.time_op.sleep_random(8,12)

    def send_chap(self, case):
        '''
        发布入口，且content进行重组
        :return:
        '''
        # self.appium_init()
        # sleep(10)
        app, app_activity, title, content, camery, edu_mode = self.get_data.app_data(case)
        content = content + self.doc.get_contact_by_dev()
        self.add_article(title, content, camery,edu_mode)
        self.time_op.sleep_random()  # 这里不等待时间很有可能两个滑动至生效一个


if __name__ == '__main__':
    driv = XHS()
    driv.send_chap()