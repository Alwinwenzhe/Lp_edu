from appium import webdriver
from time import sleep


# 下方命令需单独命令，不能放在一个py文件中执行--启动运动可以不用带设备ID
# command = "appium -p 4001 -bp 5001 --no-reset --session-override --command-timeout 3000"
# os.system(command)

class AppYishengyue(object):
    def __init__(self):
        self.driver = self.get_driver()

    def get_driver(self):
        capabilities = {
            "platformName": "Android",
            # "deviceName": "JTK5T19916007835",     # 单台设备运行，可不指定
            "appActivity": "com.yishengyue.lifetime.ui.MainActivity",  # appium1.7版本之后就应该不需要改配置了;这里报错很多次，因为activity名字错误，aapt检查出来
            "appPackage": "com.yishengyue.lifetime",
            "noReset": "true"
        }
        driver = webdriver.Remote("http://127.0.0.1:4001/wd/hub", capabilities)
        return driver



if __name__ == '__main__':
    ysy = AppYishengyue()
