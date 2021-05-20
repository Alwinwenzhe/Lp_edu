
# Debug ：2020-12-13
# Status:   #    提交订单，不能定位元素
from time import sleep
from appium import webdriver
from Common import time_operate
from Common import get_excel_data
from Common import appium_start


# 下方命令需单独命令，不能放在一个py文件中执行--启动运动可以不用带设备ID
# command = "appium -p 4001 -bp 5001 --no-reset --session-override --command-timeout 3000"
# os.system(command)

class AppJingDong(object):

    '''京东茅台抢购：提前一分钟进入'''

    def __init__(self):
        self.time_op = time_operate.TimeOperate()
        self.driver = self.get_driver()
        self.get_data = get_excel_data.GetExcelData()
        self.appium_init = appium_start.AppiumStart()

    def get_driver(self):
        capabilities = {
            "platformName": "Android",
            # "deviceName": "JTK5T19916007835",     # 单台设备运行，可不指定
            "appActivity": "com.jingdong.common.jdreactFramework.activities.JDReactNativeCommonActivity",  # appium1.7版本之后就应该不需要改配置了;这里报错很多次，因为activity名字错误，aapt检查出来
            "appPackage": "com.jingdong.app.mall",
            "noReset": "true"
        }
        driver = webdriver.Remote("http://127.0.0.1:4001/wd/hub", capabilities)
        return driver

    def enter_pro(self, content):
        '''
        进入商品详情
        :return:
        '''
        sleep(8)
        # 点击 我的
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="我的"]').click()
        self.time_op.sleep_random()
        self.driver.find_element_by_name('商品收藏').click()
        self.time_op.sleep_random()
        # 点击收藏的目标商品
        self.driver.find_elements_by_xpath('//android.widget.RelativeLayout[@index=\'0\']')[0].click()
        self.time_op.sleep_random()
        # 点击例及抢购
        self.driver.find_element_by_name('立即购买').click()
        #  提交订单，不能定位元素





if __name__ == '__main__':
    driv = AppJingDong()
    driv.enter_pro()