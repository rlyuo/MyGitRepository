#!/usr/bin/env python
# coding=utf-8

# Todo：接口自动化测试
# Author：归根落叶
# Blog：http://this.ispenn.com

import json
import http.client, mimetypes
from urllib.parse import urlencode
import random
import time
import re
import logging
import os, sys

try:
    import xlrd
except:

    # 就是 -U，-upgrade，意思是如果已安装就升级到最新版
    os.system('pip install -U xlrd')
    import xlrd
try:
    from pyDes import *
except ImportError as e:
    os.system('pip install -U pyDes --allow-external pyDes --allow-unverified pyDes')
    from pyDes import *
import hashlib
import base64
import smtplib
from email.mime.text import MIMEText

def runTest(testCaseFile):
    testCaseFile = os.path.join(os.getcwd(), testCaseFile)
    if not os.path.exists(testCaseFile):
        logging.error('测试用例文件不存在！！！')
        sys.exit()

    # 打开表格文件
    testCase = xlrd.open_workbook(testCaseFile)

    # 打开表格文件第一个sheet
    table = testCase.sheet_by_index(0)

    # 定义一个列表
    errorCase = []


    # 给字典添加数据
    # table.nrows获取该sheet中的有效行数
    for i in range(1, table.nrows):

        #如果表格第1行，第11列的值用空字符串替换换行和回车后是Yes，replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串);\n换行，\r回车。
        if table.cell(i, 10).value.replace('\n', '').replace('\r', '') != 'Yes':
            continue

        #取每一行的值并赋给一个变量
        num = str(int(table.cell(i, 0).value)).replace('\n', '').replace('\r', '')
        api_purpose = table.cell(i, 1).value.replace('\n', '').replace('\r', '')
        api_host = table.cell(i, 2).value.replace('\n', '').replace('\r', '')
        request_url = table.cell(i, 3).value.replace('\n', '').replace('\r', '')
        request_method = table.cell(i, 4).value.replace('\n', '').replace('\r', '')
        request_data_type = table.cell(i, 5).value.replace('\n', '').replace('\r', '')
        request_data = table.cell(i, 6).value.replace('\n', '').replace('\r', '')
        encryption = table.cell(i, 7).value.replace('\n', '').replace('\r', '')
        check_point = table.cell(i, 8).value
        correlation = table.cell(i, 9).value.replace('\n', '').replace('\r', '').split(';')