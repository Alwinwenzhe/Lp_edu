
class Slide(object):

    def __init__(self,driver):
        '''
        初始化对象时，需传入driver
        :param driver:
        '''
        self.driver = driver

    # 获取屏幕宽高
    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左滑动：
    def swip_left(self):
        """
        此方法适合在顶部banner位置进行滑动
        :return:
        """
        x = self.get_size()[0] / 10 * 9
        y = self.get_size()[1] / 10 * 2
        x1 = self.get_size()[0] / 10 * 4
        self.driver.swipe(x, y, x1, y)

    def swip_right(self):
        x = self.get_size()[0] / 10 * 1
        y = self.get_size()[1] / 10 * 2
        x1 = self.get_size()[0] / 10 * 9
        self.driver.swipe(x, y, x1, y)

    def swip_up(self):
        '''
        此方法是从底部往上滑动
        :return:
        '''
        x = self.get_size()[0] / 10 * 5
        y = self.get_size()[1] / 10 * 6
        y1 = self.get_size()[1] / 10 * 9
        self.driver.swipe(x, y, x, y1,0.2)

    def swip_down(self):
        '''
        向下滑动
        :return:
        '''
        x = self.get_size()[0] / 10 * 2
        y = self.get_size()[1] / 10 * 2
        y1 = self.get_size()[1] / 10 * 7
        self.driver.swipe(x, y, x, y1)

    def swip_on(self, direction):
        '''
        再次封装4个滑动方法:up,down,left,right
        :return:
        '''
        if direction == 'up':
            self.swip_up()
        elif direction == 'down':
            self.swip_down()
        elif direction == 'left':
            self.swip_left()
        elif direction == 'right':
            self.swip_right()
        else:
            print('noting swip!!!')