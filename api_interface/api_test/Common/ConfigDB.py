# -*- coding: utf-8 -*-
import configparser
import pymysql
# config=configparser.ConfigParser()
# config.read("D:\\PycharmProjects\\api_interface\\api_test\\databases.ini", encoding="utf-8-sig")
# host=config["mysql_test"]["db_host"]
# print(host)
def mysql(path,section,sql):
    config = configparser.ConfigParser()
    config.read(path, encoding="utf-8-sig")

    # host = config.get(section=section, option="db_host")
    # user = config.get(section=section, option=str(config.items(section)[1][0]))
    # pswd = config.get(section=section, option=str(config.items(section)[2][0]))
    # db = config.get(section=section, option=str(config.items(section)[3][0]))

    host = config.get(section=section,option=str(config.items(section)[0][0]))
    user=config.get(section=section,option=str(config.items(section)[1][0]))
    pswd=config.get(section=section,option=str(config.items(section)[2][0]))
    db=config.get(section=section,option=str(config.items(section)[3][0]))

    mysql=pymysql.connect(host,user,pswd,db)
    cursor=mysql.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    mysql.close()
    # print(type(data))
    return data
# print(mysql("mysql_test","select * from users"))

def mongoDB(path,section,sql):
    pass

def neo4j(path,section,sql):
    pass