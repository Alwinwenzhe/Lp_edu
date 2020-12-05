# Debug ：2020-12-05
# Status:
from time import sleep
from appium import webdriver
from Common import time_operate
from Common import get_excel_data
from Common import appium_start

# 下方命令需单独命令，不能放在一个py文件中执行--启动运动可以不用带设备ID
# command = "appium -p 4001 -bp 5001 --no-reset --session-override --command-timeout 3000"
# os.system(command)

class AppSina(object):

    def __init__(self):
        self.time_op = time_operate.TimeOperate()
        self.driver = self.get_driver()
        self.get_data = get_excel_data.GetExcelData()
        self.appium_init = appium_start.AppiumStart()

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

    def add_article(self, title, content, camery):
        '''
        新增文章
        :return:
        '''
        sleep(10)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.sina.weibo:id/titleSave")').click()
        self.time_op.sleep_random()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("微评")').click()
        self.time_op.sleep_random()
        
        # # 这里要滑动一下，解决输入发问题
        # self.slide.swip_up()
        # sleep(3)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.sina.weibo:id/iv_edit_pic")').click()
        self.time_op.sleep_random()
        # 点击相册
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.sina.weibo:id/photo_album_title_icon")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("test")').click()
        # 选择照片,注意这里的多个结果，该使用什么方法和定位
        self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.sina.weibo:id/photo_album_grideview_item_select")')[0].click()

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("下一步(1)")').click()
        self.time_op.sleep_random()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("下一步(1)")').click()
        self.time_op.sleep_random()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("选择")').click()
        self.time_op.sleep_random()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("搜索物品、电影、地点...")').click()
        self.time_op.sleep_random()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("搜索物品、电影、地点...")').send_keys("自考")
        sleep(3)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("点击添加物品话题")').click()
        self.time_op.sleep_random()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("种草生活好物，你的真实体验可以帮助更多人～")').click()
        self.time_op.sleep_random()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("种草生活好物，你的真实体验可以帮助更多人～")').send_keys(
            content)
        # 这里看是否要切换到frame
        self.time_op.sleep_random()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("添加标题")').click()
        self.time_op.sleep_random()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("填写标题")').send_keys(title)
        sleep(3)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.sina.weibo:id/titleSave")').click()
        sleep(10)

    def send_chap(self,case):
        '''
        滑动浏览视频
        :return:
        '''
        # self.appium_init()
        # sleep(10)
        x = 0
        while x < 5:
            app, app_activity, title, content, camery,edu_mode = self.get_data.app_data(case)
            content = content + '\n 详情咨询李老师  电话(微信)：15008499834'
            self.add_article(title, content, camery)
            self.time_op.sleep_random()  # 这里不等待时间很有可能两个滑动至生效一个
            x += 1
        else:
            print('case 超过5条的不处理')


if __name__ == '__main__':
    driv = AppSina()
    driv.send_chap()