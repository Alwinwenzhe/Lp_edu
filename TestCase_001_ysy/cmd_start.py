import os,time

class CmdStart(object):

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

    def kill_servee(self):
        '''查找appium进程：tasklist | find "node.exe"；杀死所有node进程：taskkill -F -PID "node.exe"'''
        command = 'tasklist | find "node.exe"'
        task_msg = self.excute_cmd_result(command)
        if len(task_msg) > 0:
            self.excute_cmd('taskkill -F -PID node.exe')
        time.sleep(6)

    def start(self):
        self.kill_servee()
        # 下方命令需单独命令，不能放在一个py文件中执行--启动运动可以不用带设备ID
        command = "appium -p 4001 -bp 5001 --no-reset --session-override --command-timeout 3000"
        os.system(command)
        time.sleep(6)

if __name__ == "__main__":
    cs = CmdStart()
    cs.start()