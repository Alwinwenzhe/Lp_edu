#！/usr/bin/env python
# Author:Alwin
# Date:
# STATUS:

import os
from Common import Assert

class Doc_Cmd:

    def __init__(self):
        self.asser = Assert.Assertions()

    def excute_cmd(self,command):
        '''仅执行，不做收集'''
        os.system(command)

    def excute_cmd_result(self,command):
        '''执行后，收集特定结果'''
        result_list = []
        result = os.popen(command).readlines()  # popen执行系统命令，并返回一个结果；打开的是一个流文件，需要readlines打开
        for i in result:
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))           #stirp去掉指定符号，并返回一个副本
        return result_list

    def get_devices(self):
        '''获取设备信息'''
        results_list = self.excute_cmd_result('adb devices')
        devices_list = []
        print(len(results_list))
        if len(results_list) >= 2:
            for i in results_list:
                if 'List' in i:         #判断不存在的
                    continue
                temp = i.split("\t")
                if temp[1] == 'device':      #因为这里有可能出现不适设备的信息
                    devices_list.append(temp[0])
            return devices_list
        else:
            print("请确认手机设备已接入")
            self.asser.assert_none(None)

    def get_contact_by_dev(self):
        '''
        通过获取手机设备，返回不同联系方式
        :return:
        '''
        contact_li = "\n 详情咨询李老师  点话(威信)：15008499834"
        contact_chen = "\n 详情咨询陈老师  点话(威信)：18180734223"
        current_dev = self.get_devices()[0]
        if 'JTK5T19916007835' == current_dev:  # 华为mate30
                return contact_li
        elif 'NABDU20901006803' == current_dev:   # P40
            return contact_chen

if __name__ == "__main__":

    print ("hello ...............")
    demo = Doc_Cmd()
    print("设备有：",demo.get_devices())
    # print (demo.excute_cmd_result("adb devices"))
    # demo.excute_cmd("adb shell ime list -a")        #查询已安装在手机端输入法
    #demo.excute_cmd("adb shell ime set com.baidu.input_huawei/.ImeService")          #切换为百度华为输入法
    #demo.excute_cmd("adb shell ime set io.appium.android.ime/.UnicodeIME")   #切换为appium输入法
