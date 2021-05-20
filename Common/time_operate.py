import time, random
from datetime import datetime

class TimeOperate(object):

    def sleep_random(self,start_time=2,end_time=4):
        '''
        等待指定范围段内的随机时间
        :return:
        '''
        sleep_time = random.randrange(start_time, end_time)
        time.sleep(sleep_time)

    def get_time(self):
        '''
        当前时间的时间戳获取,
        :return:
        '''
        time_stru = int(time.time() * 1000)  # 强制将得到的浮点数进行转化
        return time_stru

    def time_compare_1(self):
        '''
        时间对比
        :return:
        '''
        t1 = self.get_time()
        t3 = 0
        while t3 < 1280:
            self.operate()
            t2 = self.get_time()
            t3 = t2 - t1
        else:
            self.operator_coin()
            t3 = 10

if __name__ == "__main__":
    ti = TimeOperate()
    ti.sleep_random()