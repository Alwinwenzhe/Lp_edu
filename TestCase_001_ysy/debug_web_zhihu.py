# # Debug ：2020-12-05
# # Status: PASS
# import allure, pytest, os, sys
# from case import interface_test
# from Common import ExcelHandler
# from case import web_zhihu
#
#
# @allure.feature('知乎')
# @allure.severity('blocker')
# @allure.story('发帖')
# class TestWebzhiHu(object):
#
#     excel = ExcelHandler.ExcelHandler()
#     new = interface_test.InterfaceTest()
#     zhihu = web_zhihu.WebZhiHu()
#
#
#     @pytest.mark.parametrize('case', excel.get_excel_data('all'))
#     def test_zhihu_001(self,case):
#         """
#             用例描述：获取验证码
#         """
#         self.zhihu.main(case)
#
#     def test_zhihu_002(self):
#         self.zhihu.close_driver()
#
# if __name__ =="__main__":
#     zhihu = TestWebzhiHu()
#     zhihu.test_zhihu_001()
#     zhihu.test_zhihu_002()