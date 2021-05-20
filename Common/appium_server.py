# Date:2020-12-16
# STATUS: pass

import threading,time
from Common import doc_cmd
from Common import appium_start
from Common import por_list
from Common import open_device_info

class AppiumServer(object):


    doc = doc_cmd.Doc_Cmd()
    device_list = doc.get_devices()
    appiu = appium_start.AppiumStart()
    open_device_info = open_device_info.Open_Device_Info()

    def __init__(self):
        self.server_start()     #初始化就执行了


    def create_appium_command(self,i):
        '''要实现拼接命令：appium -p 4000 -bp 4500 -U 127.0.0.1:2534 --no-reset --ssesion-override'''
        p = por_list.Por_list()
        command_list = []
        appium_port_list = p.create_port_list(4000,self.device_list)          #根据获取设备信息创建对应端口列表
        appium_bp_port_list = p.create_port_list(4500,self.device_list)
        devices_list = self.device_list
        if devices_list != None:
        #for i in range(len(devices_list)):                                      #根据设备信息长度，对3个list进行for循环，依次去除并拼接好敏灵
            command = "appium -p " + str(appium_port_list[i]) + " -bp " + str(appium_bp_port_list[i]) + " -U " + str(devices_list[i]) + " --no-reset --session-override --command-timeout 300"
            command_list.append(command)
            self.open_device_info.write_data(i,appium_port_list[i],appium_bp_port_list[i],devices_list[i])
            return command_list

    def start_server(self,i):
        self.start_list = self.create_appium_command(i)              #带self的就表示对象本身，属于该py全局的，这里就可以认为定义全局变量
        self.doc.excute_cmd(self.start_list[0])                      #这里为什么是0？？？因为47行每次只穿一条命令进来;而且start_list赋值于list所以它也是list类型

    def server_start(self):
        self.kill_servee()
        self.clear_device_info()
        for i in range(len(self.device_list)):                       #根据得到的启动命令列表长度，确认该启动几个线程
            start = threading.Thread(target=self.start_server,args=(i,))
            start.start()                                                         #只是启动了，程序运行后，没有清理环境？？？
        time.sleep(10)

    def kill_servee(self):
        '''查找appium进程：tasklist | find "node.exe"；杀死所有node进程：taskkill -F -PID "node.exe"'''
        command = 'tasklist | find "node.exe"'
        task_msg = self.doc.excute_cmd_result(command)
        if len(task_msg) > 0:
            self.doc.excute_cmd('taskkill -F -PID node.exe')

    def clear_device_info(self):
        '''运行前先清理device_info.yaml中的文件信息'''
        with open('../Conf/device_info.yaml',"w") as f:       #w--写权限
            f.truncate()


if __name__ == "__main__":
    ser = AppiumServer()