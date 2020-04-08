# -*- coding: utf-8 -*-
import unittest
import requests
import json
import jsonpath
import configparser
import ddt
from api_test.Common.GetUrl import getUrl
from api_test.Common.ConfigDB import mysql
from api_test.Common.other import Compare,excl_write,excl_read
from api_test.Common.ConfigHttp import send_request
with open(".\\testData\\data.json") as json_data:
    casesData = json.loads(json_data.read().encode("utf-8-sig"))
    # print(casesData)
excl_write('.\\testData\\test.xls',mysql("./databases.ini", "mysql_test", "select * from users"),"id","password","username")
excl_data=excl_read('.\\testData\\test.xls',1,3)
excl_data_new=excl_read('.\\testData\\test.xls',2,3)
method=excl_read('.\\testData\\test.xls',"method")
Lst=[]

for j in range(len(excl_data)):
    lst=[]
    lst.append(excl_data[j])
    lst.append(excl_data_new[j])
    lst.append(method[j])
    Lst.append(lst)
print(Lst)

@ddt.ddt
class testLogin(unittest.TestCase):
    def setUp(self):
        self.url=getUrl("./servers.ini","test")
    @ddt.data(*casesData)
    @ddt.unpack
    def test_login(self,data,result):
        #有效正确的登录
        self.url+="/user/login"
        actual_result=requests.post(self.url,
                             data=data
                             )
        expect_result=result
        self.assertEqual(json.loads(actual_result.text),expect_result,"对比结果不一致")

    @ddt.data(*Lst)
    @ddt.unpack
    def test_loginsql(self,data,result,method):
        # sql_data=mysql("./databases.ini", "mysql_test", "select * from users")
        self.url += "/user/login"
        actual_result = send_request(self.url,
                                      data,
                                     method
                                      )
        expect_result={
        "message": 200,
        "user": "zjw"
                }
        Compare(actual_result,"$..user",[result["username"]])
        # self.assertEqual(json.loads(actual_result.text), expect_result, "对比结果不一致")
    def tearDown(self):
        pass
