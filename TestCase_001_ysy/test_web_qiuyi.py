# # Debug ：2021-05-07
# # Status: PASS
# import allure, pytest, os, sys
# from case import interface_test
# from Common import ExcelHandler
# from case import web_qiuyi
#
#
# @allure.feature('求艺网')
# @allure.severity('blocker')
# @allure.story('发帖')
# class TestWebQiuyi(object):
#
#     excel = ExcelHandler.ExcelHandler()
#     new = interface_test.InterfaceTest()
#     qiuyi = web_qiuyi.WebQiuyi()
#
#
#     @pytest.mark.parametrize('case', excel.get_excel_data('all'))
#     def test_qiuyi_001(self,case):
#         """
#             用例描述：发布流程
#         """
#         self.qiuyi.main(case)
#
#     def test_qiuyi_002(self):
#         self.qiuyi.close_driver()
#
# if __name__ =="__main__":
#     qiuyi = TestWebQiuyi()
#     qiuyi.test_qiuyi_001()
#     qiuyi.test_qiuyi_002()