# Debug_time:  2020-11-22
# Status:    PASS
import time, os
from appium import webdriver

# 红米note4x  ba3c96e80704   该脚本可在此手机上正常运行
# 华为P40     NABDU20901006803    该脚本在此手机运行异常

# 一生约  com.yishengyue.lifetime      com.yishengyue.lifetime.ui.WelcomeActivity

# 下方命令需单独命令，不能放在一个py文件中执行--启动运动可以不用带设备ID
# command = "appium -p 4001 -bp 5001 -U NABDU20901006803 --no-reset --session-override --command-timeout 3000"
# os.system(command)


capabilities = {
            "platformName": "Android",
            "automationName": "UiAutomator2",  # 这个忘记作用了
            "deviceName": "ba3c96e80704",
            "appActivity": "com.yishengyue.lifetime.ui.WelcomeActivity",
            # appium1.7版本之后就应该不需要改配置了;这里报错很多次，因为activity名字错误，aapt检查出来
            "appPackage": "com.yishengyue.lifetime",
            "noReset":"true"
        }
driver = webdriver.Remote("http://127.0.0.1:4001/wd/hub", capabilities)  # 这里的4725端口需要和启动appium服务端口对应
time.sleep(10)
driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.yishengyue.lifetime:id/setting")').click()     #点击‘我的’-设置
driver.back()
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.yishengyue.lifetime:id/message")').click()     #点击‘我的’--消息
driver.back()
