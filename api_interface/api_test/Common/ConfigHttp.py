# -*- coding: utf-8 -*-
import json
import requests
from api_test.Common.other import excl_read
# method=excl_read('..\\testData\\test.xls',"username")
# print(method)
def send_request(url,data,method):
    print (method["method"])
    if method["method"]=="get":
        result=requests.get(url,data=data)
    if method ["method"]== "post":
        result= requests.post(url,data=data)
    if method ["method"]== "put":
        result =requests.put(url,data=data)
    if method ["method"]== "delete":
        result =requests.delete(url, data=data)
    return result