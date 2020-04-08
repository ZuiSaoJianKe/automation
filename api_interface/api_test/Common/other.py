# -*- coding: utf-8 -*-
import jsonpath
from copy import deepcopy,copy
import requests
import json
import csv
import xlrd
import xlwt
from api_test.Common.ConfigDB import mysql
failureException = AssertionError

#################################################
# result=requests.post("http://localhost:9527/user/login",
#               data={"username":"root",
#                     "password":"123456"
#                     })
# data=jsonpath.jsonpath(json.loads(result.text),expr="$..user")
# print(data)
##################################################


def Compare(request_result,cmd,sql_data):
    apiresult=jsonpath.jsonpath(json.loads(request_result.text), expr=cmd)
    # try:
    if sql_data==apiresult:
        pass
    else:
        print(sql_data)
        print(apiresult)
        raise failureException("接口数据和数据库数据对不上")

    # except failureException:
    #     print("接口数据和数据库数据对不上")

###############################################
# sql_data=mysql("../databases.ini","mysql_test","select * from users where id=1")
# print(sql_data)
# Compare(result,"$..user",[sql_data[0][2]])
###############################################

#######################################################
# def writeData(data, file):
#     with open(file, 'a', errors='ignore', newline='') as f:
#             f_csv = csv.writer(f)
#             f_csv.writerows(data)
#     print('write_csv success')
#
# # writeData(sql_data, './test.xlsx') #数据写入到 csv文档中
###########################################
# data=xlrd.open_workbook()
# name=data.sheet_names()[0]
# table=data.sheet_by_name(name)
# print(table.nrows)
# print(table.row_values(0))
# # table.row_values(3)="yuihhhshdhshda"
# print (table.cell(0,0).value)
###########################################################
# sql_data=mysql("../databases.ini","mysql_test","select * from users")
# print(sql_data)
# workbook = xlwt.Workbook(encoding = 'ascii')
# worksheet=workbook.add_sheet("test")
# worksheet.write(0, 0, label="id")
# worksheet.write(0, 1, label="password")
# worksheet.write(0, 2, label="username")
# for i in range(1,len(sql_data)+1):
#     for j in range(len(sql_data[i-1])):
#         worksheet.write(i, j, label=sql_data[i-1][j])
# workbook.save('..\\testData\\test.xls')
####################################################
# sql_data=mysql("../databases.ini","mysql_test","select * from users")
def excl_write(file,sql_data,*head):
    # sql_data=mysql("../databases.ini","mysql_test","select * from users")
    # print(sql_data)
    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet=workbook.add_sheet("test")
    for i in range(len(head)):
        worksheet.write(0, i, label=head[i])

    for i in range(1,len(sql_data)+1):
        for j in range(len(sql_data[i-1])):
            worksheet.write(i, j, label=sql_data[i-1][j])
    workbook.save(file)

# excl_write('..\\testData\\test.xls',sql_data,"id","pwd","user")

def excl_read(file,*args):
    mile=xlrd.open_workbook(file)
    name = mile.sheet_names()[0]
    table= mile.sheet_by_name(name)
    nrows=table.nrows
    # print(nrows)
    ncols=table.ncols
    dic={}
    dic_copy={}
    lst=[]
    # for x in range(0,len(ncols)):
    if type(args[0]) == str:
        for i in range(1, nrows):
            for j in range(0, ncols):
                if table.cell(0, j).value==args[0]:
                    remember_num=j
            dic[args[0]] = table.cell(i,remember_num).value
            dic_copy = deepcopy(dic)
            lst.append(dic_copy)
    else:
        for i in range(1,nrows):
            if len(args)>1:
                for j in range(args[0], args[1]):
                    dic[table.cell(0, j).value] = table.cell(i, j).value
                    dic_copy = deepcopy(dic)
                lst.append(dic_copy)
            else:
                for j in range(args[0],ncols):
                    dic[table.cell(0,j).value] = table.cell(i,j).value
                    dic_copy=deepcopy(dic)
                    # print(dic[table.cell(0,j).value] )
                lst.append(dic_copy)
    # print(lst)
    return lst
# print(excl_read('..\\testData\\test.xls',1,3))
