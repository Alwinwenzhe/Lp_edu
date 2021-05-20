import json, re, time, hashlib, random
from Common import Log
from Common import operate_json
from Conf import Config
from Common import operate_sql_al
from Common import ExcelHandler
from Common import req_reload
from Common import Assert
from Common import Consts
from Common import get_excel_data

class InterfaceTest(object):

    def __init__(self):
        self.log = Log.MyLog()
        self.oper_j = operate_json.OperateJson()
        self.conf = Config.Config()
        self.excel = ExcelHandler.ExcelHandler()
        self.reqe = req_reload.ReqReload()
        self.tes_assert = Assert.Assertions()
        self.get_data = get_excel_data.GetExcelData()

    # def choose_envir(self,envir):
    #     '''
    #     运行环境判断
    #     :param envir:
    #     :return: 请求url域名
    #     '''
    #     if envir =='ysy_test':
    #         req_url = self.conf.tysy_host
    #     elif envir =='ysy_release':
    #         req_url = self.conf.ysy_host
    #     elif envir == 'yhz_test':
    #         req_url = self.conf.tyhz_host
    #     elif envir == 'yhz_release':
    #         req_url = self.conf.yhz_host
    #     elif envir =='tysy_o2o':
    #         req_url = self.conf.tysyo2o_host
    #     elif envir =='ysy_o2o':
    #         req_url = self.conf.ysyo2o_host
    #     elif envir == 'ysy_pro_release':
    #         req_url = self.conf.ysy_pro_host
    #     return req_url

    def response_write_to_json(self,path,response):
        '''
        写入json文件
        :param path:
        :param response:
        :return:
        '''
        self.get_path(path, response)

    def test_case_method(self,case,request_method):
        '''
        所有api测试用例调用该方法
        :param case:
        :param request_method:
        :return:
        '''
        expect, api_url, headers, params, global_var = self.param_get_deal(case)
        response = self.reqe.req(request_method, api_url, params, headers, global_var)
        if response['body']:
            self.tes_assert.assert_common(response['code'], response['body'], expect, response['time_consuming'])
        else:                       #处理PHP返回的页面请求
            self.tes_assert.assert_php(response['code'],response['time_consuming'])
        Consts.RESULT_LIST.append('True')
        if global_var:
            self.response_write_to_json(global_var, response['text'])
        print('运行case为：{0}，验证：{1}，预期结果为：{2}'.format(case['module'], case['case_description'], expect))
        time.sleep(2)

    def write_data_to_json(self):
        '''
        将当前时间戳写入json
        将随机8位数戳写入json
        将登录标记写入json
        :return:
        '''
        rand8,cur_ti,sign = self.sign_md5()     # 不能单独调用，否则时间戳等会不同
        self.oper_j.write_json_value('curTime',cur_ti)
        self.oper_j.write_json_value('nonce', rand8)
        self.oper_j.write_json_value('sign', sign)

    def randint_8(self):
        '''
        8位随机数
        :return:
        '''
        int_8 = random.randint(0,99999999)
        return int_8

if __name__ == '__main__':
    ut = New_Tool_A()
    # print(ut.while_split_data('test_debug',"s::SELECT IFNULL(dv.version,'error_version') FROM data_version dv WHERE dv.code='ios'"))
    # print(ut.split_data(''))
