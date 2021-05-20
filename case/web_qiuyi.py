# Debug: 2020-12-5
# Status:
# -*- coding:utf-8 -*-

from Common.time_operate import TimeOperate
from selenium import webdriver
from selenium.webdriver import ActionChains  #引入鼠标事件
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Common import get_excel_data

class WebQiuyi(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.time_random = TimeOperate()
        self.get_data = get_excel_data.GetExcelData()
        print('Start qiuyi.....................')
        self.log()

    def log(self):
        self.driver.implicitly_wait(10)
        log_url = "https://kf.qeo.cn/"
        self.driver.get(log_url)
        self.time_random.sleep_random()
        self.driver.maximize_window()
        # 登录
        self.driver.find_element_by_xpath('//*[@id="menut"]/li[3]/center/a[2]/img').click()
        # 选择frame
        self.driver.switch_to.frame('ptlogin_iframe')
        self.driver.find_element_by_id("switcher_plogin").click()
        self.driver.find_element_by_id('u').click()
        self.driver.find_element_by_id('u').send_keys("503106686")
        self.driver.find_element_by_id('p').click()
        self.driver.find_element_by_id('p').send_keys('20210501+-')
        self.driver.find_element_by_id('login_button').click()
        self.time_random.sleep_random(10,15)

    def send_chap(self,title,content):
        ''''''
        self.driver.find_element_by_xpath('//*[@id="menum"]/li[1]/a').click()
        self.time_random.sleep_random()

        #封面图
        self.driver.find_element_by_xpath('//*[@id="list"]/li[2]/input').click()
        self.time_random.sleep_random()
        # select组件选择课程分类
        self.driver.find_element_by_id('fl').click()
        self.driver.find_element_by_xpath('//*[@id="fl"]/option[6]').click()
        self.time_random.sleep_random()
        self.driver.find_element_by_id('fls').click()
        self.driver.find_element_by_xpath('//*[@id="fls"]/option[4]').click()
        self.driver.find_element_by_name('tit').send_keys(title)
        self.time_random.sleep_random()
        self.driver.find_element_by_name('abtxt').send_keys('四川 小自考 成教 网教 自考')
        # 正文填充
        # 选择frame
        # self.driver.switch_to.frame(''
        self.driver.switch_to.frame('baidu_editor_0')
        self.driver.find_element_by_xpath('/html/body').send_keys(content)
        self.time_random.sleep_random()
        self.driver.switch_to.default_content()
        self.time_random.sleep_random()

        self.driver.find_element_by_id('formsub').click()
        # 接受警告框
        self.driver.switch_to.alert.accept()
        self.driver.find_element_by_id('formsub').click()
        self.time_random.sleep_random()
        self.driver.switch_to.alert.accept()
        self.time_random.sleep_random(4,7)


    def main(self,case):
        '''
        发帖入口
        :return:
        '''
        app, app_activity, title, content, camery, edu_mode = self.get_data.app_data(case)
        content = content + '\n 详情咨询李老师  电话(微信)：15008499834'
        self.send_chap(title, content)
        self.time_random.sleep_random()

    def close_driver(self):
        self.time_random.sleep_random()
        self.driver.close()


if __name__ == "__main__":
    qiuyi = WebQiuyi()
    qiuyi.send_chap('四川成人学历自考 成教 网教 有什么区别','四川成人学历提升报名怎么报？在哪儿报名？学费多少？‌‌成人学历分为自考，成教，网教，电大四大类型')