# -*- coding: utf-8 -*-
import os
import time
from api_test.Common.Email import send_email
from api_test.Common import HTMLTestRunner
import unittest
import json

from api_test.Cases.test_login import  testLogin
from api_test.Cases.test_regist import testRegist

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testRegist))
    suite.addTest(unittest.makeSuite(testLogin))
    now = time.strftime("%Y-%m-%d")
    path=os.getcwd()+"/result/" + now + "result.html"
    with open(path, "wb") as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告")
        runner.run(suite)
    send_email(path)
    # print(casesData)


