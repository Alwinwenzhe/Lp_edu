from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium import webdriver


class Until(object):
    '''通过方法'''
    def wait_element(driver, time, element_by, element, msg):
        """
        等待元素出现
        :param driver: driver
        :param time: 等待时间
        :param element_by: 元素类型
        :param element: 元素关键字
        :param msg: 输出信息
        :return:
        """
        WebDriverWait(driver, time). \
            until(expected_conditions.presence_of_element_located((element_by, element)), msg)


if __name__ == "__main__":
    un = Until()
    # 调用
    un.wait_element(deriver, 10, By.ID, "com.xxx.xxx.ceshi:id/main_select_index_rb", "没有发现xxxx...")

