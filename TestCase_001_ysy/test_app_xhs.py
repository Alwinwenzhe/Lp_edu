# Debug ：2021-05-14
# Status: PASS
import allure, pytest, os, sys
from Common import ExcelHandler
from case import app_xhs
from Common import appium_server

@allure.feature('头条')
@allure.severity('blocker')
@allure.story('发布小红书')
class TestAppXHS(object):

    excel = ExcelHandler.ExcelHandler()
    ap_xhs = app_xhs.XHS()

    @pytest.mark.parametrize('case', excel.get_excel_data('all'))
    def test_new_001(self,case):
        """
            用例描述：发布小红书
        """
        self.ap_xhs.send_chap(case)


if __name__ == '__main__':
    appnew = TestAppXHS()
    i = 0
    while i < 10:
        appnew.test_new_001()
        i += 1