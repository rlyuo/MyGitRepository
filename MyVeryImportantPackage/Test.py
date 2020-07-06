#coding:utf-8

from Lib import HTMLTestRunner
import unittest
from MyVeryImportantPackage.UnitTestCase01 import MyTest

if __name__=='__main__':
    suite=unittest.makeSuite(MyTest)
    report_filename ='D:\\myreport.html'

    with open(report_filename, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='httpbin.org请求测试报告', description="仅做参考")
        runner.run(suite)