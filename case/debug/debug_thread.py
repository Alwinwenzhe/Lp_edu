# --workers=n：多进程运行需要加此参数，  n是进程数。默认为1
# --tests-per-worker=n：多线程需要添加此参数，n是线程数
# 　　如果两个参数都配置了，就是进程并行，每个进程最多n个线程，总线程数：进程数*线程数
# 注意：在windows上进程数永远为1。
# 　　需要使用 if __name__ == "__main__":，在dos中运行会报错
#     pytest-parallel加了多线程处理后，最后执行时间是运行时间最长的线程的时间

import pytest


def test_03(start, open_web1):
    print('测试用例3操作')


def test_04(start, open_web1):
    print('测试用例4操作')


if __name__ == "__main__":
    pytest.main(["-s", "debug_thread.py", '--workers=2', '--tests-per-worker=4'])
