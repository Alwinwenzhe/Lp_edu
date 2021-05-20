#！/usr/bin/env python
# Author:Alwin
# Date:
# STATUS:
from Common.doc_cmd import Doc_Cmd


class Por_list:

    def port_is_used(self,port_num):
        #查看端口是否被占用：False--没有被占用
        self.doc = Doc_Cmd()
        command = 'netstat -ano | findstr ' + port_num     #字符串只能和字符串拼接
        flag = None
        result_list = self.doc.excute_cmd_result(command)
        if len(result_list)> 0:
            flag = False    #False时，占用
        else:
            flag = True     #true时，就未被占用
        return flag

    def create_port_list(self,start_port,devices_list):   #传入开始端口、server中的设备列表
        '''start_port:开始端口，devices_list：设备列表'''
        port_list = []
        if devices_list != None:
            while len(port_list) != len(devices_list):       #port少于设备就执行
                if self.port_is_used(str(start_port)):       #检测端口是否被占用
                    port_list.append(start_port)
                start_port += 1                              #端口自增
            return port_list
        else:                           #判定devices_list返回的是none时，提示生成失败
            print("adb没有检测到连接的手机设备")

if __name__ == '__main__':
    p = Por_list()
    # s = Serverr()
    print(p.port_is_used('4755'))
    # print(p.create_port_list(4756,s.get_devices()))