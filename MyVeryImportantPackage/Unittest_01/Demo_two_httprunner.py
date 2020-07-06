#!/usr/bin/env python

import requests
import unittest
import time
import HTMLTestRunner

class HttpbinRuquetTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_httpbin_get_request(self):
        """
        get请求，参数说明：
        @URL：请求url地址
        @hearders：请求的头部信息
        @params：请求发送参数
        @verify：ssl证书验证，可选
        @timeout：请求超时设置，可选
        @proxies：代理ip，可选
        :return: 响应json和状态码
        """

        url = 'http://httpbin.org/get'
        headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Host": "httpbin.org",
        "Referer": "http://httpbin.org/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        data = {"name":"tom","age":18}

        res = requests.get(url=url,headers=headers,params=data,timeout=3,verify=False)
        response_status = res.status_code
        response_json = res.json()

        print(response_status,response_json)


    def test_httpbin_post_request(self):
        """
        @url：请求URL
        @headers：请求头部信息
        @data：请求发送数据
        :return:
        """
        url = 'http://httpbin.org/post'
        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Host": "httpbin.org",
            "Referer": "http://httpbin.org/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        payload = {"name": "tom", "age": 18}

        res = requests.post(url=url,headers=headers,data=payload)
        response_json = res.json()

        print(response_json)


if __name__ == '__main__':
    """
    @test_dir：说明测试用例的存放路径
    @discover：载装目录下所有符合pattern要求的测试文件
    @report_filename：测试报告的文件名，是html文件
    @runner：构造HTTPTestRunner实例，运行discover的文件下测试用例
    """
    test_dir = "../script"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
    report_filename = f'../data/reports/tmp_{time.strftime("%Y%m%d%H%M%S")}.html'

    with open(report_filename,'w',encoding='utf-8') as f:
        runner = HTMLTestRunner(stream=f,title='httpbin.org请求测试报告',description="仅做参考")
        runner.run(discover)
