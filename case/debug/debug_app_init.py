# Debug_time:  2020-11-22
# Status:    PASS
# 最原始操作

# 下方命令需单独命令，不能放在一个py文件中执行--启动运动可以不用带设备ID
# command = "appium -p 4001 -bp 5001 --no-reset --session-override --command-timeout 3000"
# os.system(command)

from appium import webdriver
from time import sleep
import random

def get_driver():
    capabilities ={
        "platformName": "Android",
        "deviceName": "ba3c96e80704",       # 非必填项
        # "appActivity": "ui.WelcomeActivity",
        #"appActivity": "ui.WelcomeActivity",  #用户引导页
        "appActivity" : "com.ss.android.ugc.aweme.splash.SplashActivity",        #appium1.7版本之后就应该不需要改配置了;这里报错很多次，因为activity名字错误，aapt检查出来
        "appPackage": "com.ss.android.ugc.aweme.lite",
        # "appPackage": "com.yishengyue.lifetime"
        "noReset":"true"
    }
    driver = webdriver.Remote("http://127.0.0.1:4001/wd/hub",capabilities)
    return driver

#获取屏幕宽高
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width,height

#向左滑动：
def swip_left():
  """
  此方法适合在顶部banner位置进行滑动
  :return:
  """
  x = get_size()[0]/10*9
  y = get_size()[1]/10*2
  x1 = get_size()[0]/10*4
  driver.swipe(x,y,x1,y)

def swip_right():
  x = get_size()[0] / 10 * 1
  y = get_size()[1] / 10 * 2
  x1 = get_size()[0] / 10 * 9
  driver.swipe(x,y,x1,y)

def swip_up():
  '''
  此方法是从底部往上滑动
  :return:
  '''
  x = get_size()[0] / 10 * 1
  y = get_size()[1] / 10 * 8
  y1 = get_size()[1] / 10 * 4
  driver.swipe(x,y,x,y1)

def swip_down(driver):
  '''
  向下滑动
  :return:
  '''
  x = get_size()[0] / 10 * 2
  y = get_size()[1] / 10 * 2
  y1 = get_size()[1] / 10 * 7
  driver.swipe(x,y,x,y1)

def swip_on(direction):
    '''
    再次封装4个滑动方法:up,down,left,right
    :return:
    '''
    if direction == 'up':
        swip_up()
    elif direction == 'down':
        swip_down()
    elif direction == 'left':
        swip_left()
    elif direction == 'right':
        swip_right()
    else:
        print('noting swip!!!')

def sleep_random():
    '''
    等待等待时间
    :return:
    '''
    sleep_time = random.randrange(1,40)
    return sleep_time


driver = get_driver()
while 1:
    swip_on("up")
    print('reset 3 seconds:-------')
    sleep(sleep_random())            #这里不等待时间很有可能两个滑动至生效一个