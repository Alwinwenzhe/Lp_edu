# Debug ：2020-12-05
# Status: PASS
import allure, pytest, os, sys
from Common import ExcelHandler
from case import app_new
from Common import appium_server

@allure.feature('头条')
@allure.severity('blocker')
@allure.story('发布头条')
class TestAppNew(object):

    excel = ExcelHandler.ExcelHandler()
    # app_ser = appium_server.AppiumServer()
    # app_ser.server_start()
    ap_new = app_new.AppNew()

    @pytest.mark.parametrize('case', excel.get_excel_data('all'))
    def test_new_001(self,case):
        """
            用例描述：发布头条
        """
        # self.app_ser.server_start()
        self.ap_new.send_chap(case)


if __name__ == '__main__':
    # server()
    appnew = TestAppNew()
    i = 0
    while i < 10:
        appnew.test_new_001()
        i += 1