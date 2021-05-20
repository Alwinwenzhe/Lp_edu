# Debug ：2020-12-05
# Status: PASS
import allure, pytest, os, sys
from Common import ExcelHandler
from case import app_sina
from Common import doc_cmd

@allure.feature('一生约--登录')
@allure.severity('blocker')
@allure.story('登录')
class TestAppSina(object):
    '''
    # BLOCKER = 'blocker'　　阻塞缺陷
    # CRITICAL = 'critical'　严重缺陷
    # NORMAL = 'normal'　　  一般缺陷
    # MINOR = 'minor'　　    次要缺陷
    # TRIVIAL = 'trivial'　　轻微缺陷　a
    '''

    excel = ExcelHandler.ExcelHandler()
    ap_sina = app_sina.AppSina()
    doc_c = doc_cmd.Doc_Cmd()
    # cs = CmdStart()
    #
    # def test_sina_001(self):
    #     '''
    #     启动服务，启动后，就case2就不能运行了
    #     :return:
    #     '''
    #     self.cs.start()

    @pytest.mark.parametrize('case', excel.get_excel_data('all'))
    def test_sina_002(self,case):
        """"
            用例描述：判断设备，运行不同
        """
        # self.app_ser.server_start()
        current_device = self.doc_c.get_devices()[0]
        if 'JTK5T19916007835' == current_device:      #华为mate30
            self.ap_sina.send_chap_02(case)
        elif 'NABDU20901006803' == current_device:   # P40
            self.ap_sina.send_chap(case)


if __name__ == '__main__':
    sina = TestAppSina()
    i = 0
    while i < 6:
        sina.test_sina_001()
        i += 1