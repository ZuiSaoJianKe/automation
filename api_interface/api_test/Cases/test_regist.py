# -*- coding: utf-8 -*-
import unittest
import requests
import json
class testRegist(unittest.TestCase):
    def setUp(self):
         pass
    def test_regist_01(self):
        #有效正确的登录
        result=requests.post(url="http://localhost:9527/user/regist",
                             data={"username":"root",
                                   "password":"123456"}
                             )
        expect_result_code=200
        self.assertEqual(result.status_code,expect_result_code,"对比结果不一致")

    def test_regist_02(self):
        #有效正确的登录
        result=requests.post(url="http://localhost:9527/user/regist",
                             data={"username":"zjw",
                                   "password":"123456"}
                             )
        expect_result_code=200
        self.assertEqual(result.status_code,expect_result_code,"对比结果不一致")
    def tearDown(self):
        pass