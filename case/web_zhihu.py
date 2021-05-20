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

class WebZhiHu(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.time_random = TimeOperate()
        self.get_data = get_excel_data.GetExcelData()
        print('Start zhihu.....................')
        self.log()

    def log(self):
        self.driver.implicitly_wait(10)
        log_url = "https://www.zhihu.com/"
        self.driver.get(log_url)
        self.time_random.sleep_random()
        self.driver.maximize_window()
        # 切换到密码登录
        self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/div[1]/div[2]').click()
        self.time_random.sleep_random()
        '''点击发布文章'''
        username = self.driver.find_elements_by_tag_name('input')[0]
        username.clear()
        username.send_keys('15828022852')
        self.time_random.sleep_random()
        username = self.driver.find_elements_by_tag_name('input')[1]
        username.clear()
        username.send_keys('123456ab!@')
        self.time_random.sleep_random()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/button').click()
        self.time_random.sleep_random(3,4)
        self.driver.find_element_by_link_text('首页').click()
        self.time_random.sleep_random(3,4)

    def send_chap(self,title,content):
        '''发布操作'''
        self.driver.switch_to.window(self.driver.window_handles[-1])        # 切换到最新打开的浏览器窗口
        self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[2]/div[2]/label/textarea').send_keys(title)
        self.time_random.sleep_random()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[2]/div[3]/div/div[2]/div/div[2]/div/div/div/div/span').send_keys(content)
        self.time_random.sleep_random()
        # 点击发布按钮旁的下拉菜单
        self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div/div[1]/div/div[2]/div[2]/button/svg').click()
        self.time_random.sleep_random()
        # 选择标签
        self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/ul[1]/li[1]/span/a[1]').click()
        self.time_random.sleep_random()
        # 点击下一步
        self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[4]/button').click()
        # 选择专栏
        self.driver.find_element_by_xpath('//*[@id="PublishPanel-columnItem-0"]').click()
        self.time_random.sleep_random()
        # 确认发布
        self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[3]/button[2]').click()
        self.time_random.sleep_random(3,6)

        self.driver.close()    # 关闭当前窗口
        # self.driver.window_handles(mainWindow)  #切回主窗口
        self.time_random.sleep_random(3,8)


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
    zhihu = WebZhiHu()
    zhihu.send_chap('四川成人学历自考 成教 网教 有什么区别','四川成人学历提升报名怎么报？在哪儿报名？学费多少？‌‌成人学历分为自考，成教，网教，电大四大类型')