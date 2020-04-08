# -*- coding: utf-8 -*-
import configparser
def getUrl(path,section):
    config = configparser.ConfigParser()
    config.read(path, encoding="utf-8-sig")
    url= config.get(section=section,option=str(config.items(section)[0][0]))
    try:
        port=config.get(section=section,option=str(config.items(section)[1][0]))
    except:
        port =""
    if port =="":
        resultUrl=url
    else:
        resultUrl=url+":"+port
    return resultUrl
# print(getUrl("test"))