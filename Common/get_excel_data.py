from Common import ExcelHandler
from Conf import Config

class GetExcelData(object):

    def __init__(self):
        '''
        获取数据源
        '''
        self.data_resource = ExcelHandler.ExcelHandler()
        self.con = Config.Config()

    def app_data(self,case):
        '''
        获取app端所需参数
        :param case:
        :return:
        '''
        test_app = self.con.sina
        test_app_activity = self.con.sina_activity
        title = case['title']
        content = case['content']
        album = case['album']
        edu_mode = case['edu_mode']
        return test_app,test_app_activity,title,content,album,edu_mode

if __name__ == "__main__":
    get = GetExcelData()
    print(get.app_data())

