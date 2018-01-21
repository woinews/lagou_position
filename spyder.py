# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 15:56:08 2018

@author: inews
"""

import requests
import pandas as pd
import numpy as np
import time
from bs4 import BeautifulSoup

proxy = {'http':'58.249.35.42:8118'}  #找的一个代理IP，失效了要更换

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

headers = {
    'User-Agent':random.choice(USER_AGENT_LIST),
    'Host':'www.lagou.com',
    'Connection':'keep-alive',
    #加入cookie才显示出正确内容，使用实时浏览器cookies
    'Cookie':''
    'Origin':'https://www.lagou.com',
    'Referer':'https://www.lagou.com/jobs/list_python%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?oquery=python%E7%88%AC%E8%99%AB&fromSearch=true&labelWords=relative&city=%E6%B7%B1%E5%9C%B3',
    'X-Anit-Forge-Code':'0',
    'X-Anit-Forge-Token':'None',
    'X-Requested-With':'XMLHttpRequest'
}

jobsInfo_list = []

for x in range(1,6):    #该处爬取1-30页的话会失败，考虑分多步请求
    form_data = {
        'first' : 'true',
        'pn' : x,
        'kd' : 'python数据分析'
        }

    result = requests.post(url,headers = headers,proxies = proxy,data = form_data)
    resultdic = result.json()
    jobsInfo = resultdic['content']['positionResult']['result']
    jobsInfo_list.extend(jobsInfo)
    time.sleep(3)
#    for job in jobsInfo:
#        print(job['companyFullName']+'|'  + '|' + job['positionName']+ '|' + job['salary'])
    
pd.DataFrame(jobsInfo_list).to_excel('positiondata2.xlsx')
