#！/usr/bin/env python
# Author:Alwin
# Date:
# STATUS:
import yaml

class Open_Device_Info:
    def __init__(self):
        self.file = '../Conf/device_info.yaml'

    def read_device_info(self):
        '''读取yaml文件信息'''
        with open(self.file) as f:
            data = yaml.load(f)                                 #load：将yaml格式的字符串转换成Python对象 dump：将Python对象转换成yaml格式文档
        return data

    def get_device_info(self,key,port):
        '''读取文件中特定值'''
        data = self.read_device_info()
        return data[key][port]

    def write_data(self,i,b,bp,U):
        '''写入yaml数据'''
        with open(self.file,"a") as f:                      #a--追加
            data = self.join_data(i,b,bp,U)
            yaml.dump(data,f)

    def join_data(self,i,b,bp,U):
        '''数据拼接，注意这样的格式才对'''
        data ={
            "device_" + str(i): {
                    "b":str(b),
                    "bp": str(bp),
                    "U": str(U)
            }
        }
        return data

    def get_device_count(self):
        #获取yaml文件中的行数
        data = self.read_device_info()
        count = len(data)
        return count

if __name__ == '__main__':
    od = Open_Device_Info()
    print(od.read_device_info())
    # print(od.get_device_info('device_2','bp'))
    print (od.get_device_count())