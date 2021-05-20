# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 上午10:46
# @Author  : WangJuan
# @File    : Config.py

from configparser import ConfigParser
from Common import Log
import os, re

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 脚本路径
TEST_CASE_PATH = BASE_PATH + r'\Conf\case_data.xlsx'

class Config:
    # type:
    App_info = "app_info"

    # values:
    YSY_APP = "yishengyue"
    YSY_APP_ACTIVITY = "yishengyue_activity"
    TIK_TOK_APP = "tik_tok_speed"
    TIK_TOK_APP_ACTIVITY = "tik_tok_speed_activity"
    SINA = "sina"
    SINA_ACTIVITY = "sina_activity"

    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.log = Log.MyLog()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        # print(self.conf_path)
        self.xml_report_path = Config.path_dir+'/allure-results'
        self.html_report_path = Config.path_dir+'/allure-report'

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")
        self.config.read(self.conf_path, encoding='utf-8')

        # 一生约测试环境信息
        self.ysy_app = self.get_conf(Config.App_info, Config.YSY_APP)
        self.ysy_app_activity = self.get_conf(Config.App_info,Config.YSY_APP_ACTIVITY)
        self.tik_tok_app = self.get_conf(Config.App_info,Config.TIK_TOK_APP)
        self.tik_tok_app_activity = self.get_conf(Config.App_info,Config.TIK_TOK_APP_ACTIVITY)
        self.sina = self.get_conf(Config.App_info,Config.SINA)
        self.sina_activity = self.get_conf(Config.App_info,Config.SINA_ACTIVITY)

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改：w+ 可读可写-覆盖写；如无文件则创建
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

if __name__ == "__main__":
    con = Config()
    print(TEST_CASE_PATH)
    print(con.ysy_app)

