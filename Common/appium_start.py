#！/usr/bin/env python
# Author:Alwin
# Date:
# STATUS:
from Common.doc_cmd import Doc_Cmd
from Common.por_list import Por_list
from Common.Assert import Assertions
from Common.open_device_info import Open_Device_Info

class AppiumStart(object):

    def __init__(self):             #构造函数是对象实例化是就会执行这部分，然后根据才会有后面的调用
        self.doc = Doc_Cmd()
        self.open_device_info = Open_Device_Info()
        self.device_list = self.doc.get_devices()
        self.asse = Assertions()

    def create_appium_command(self,i):
        '''要实现拼接命令：appium -p 4000 -bp 4500 -U 127.0.0.1:2534 --no-reset --ssesion-override'''
        p = Por_list()
        command_list = []
        appium_port_list = p.create_port_list(4000,self.device_list)          #根据获取设备信息创建对应端口列表
        appium_bp_port_list = p.create_port_list(4500,self.device_list)
        devices_list = self.device_list
        if devices_list != []:
        #for i in range(len(devices_list)):                                      #根据设备信息长度，对3个list进行for循环，依次去除并拼接好敏灵
            # command = "appium -p " + str(appium_port_list[i]) + " -bp " + str(appium_bp_port_list[i]) + " -U " + str(devices_list[i]) + " --no-reset --session-override --command-timeout 3000"
            command = "appium -p " + str(appium_port_list[i]) + " -bp " + str(appium_bp_port_list[i]) +  " --no-reset --session-override --command-timeout 3000"
            command_list.append(command)
            self.open_device_info.write_data(i,appium_port_list[i],appium_bp_port_list[i],devices_list[i])
            return command_list
        else :
            print("请确保有手机设备接入")


if __name__ == "__main__":
    ser = AppiumStart()
    len = ser.create_appium_command(0)
    print(len)