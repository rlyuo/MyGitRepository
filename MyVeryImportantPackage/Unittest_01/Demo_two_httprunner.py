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
        get���󣬲���˵����
        @URL������url��ַ
        @hearders�������ͷ����Ϣ
        @params�������Ͳ���
        @verify��ssl֤����֤����ѡ
        @timeout������ʱ���ã���ѡ
        @proxies������ip����ѡ
        :return: ��Ӧjson��״̬��
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
        @url������URL
        @headers������ͷ����Ϣ
        @data������������
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
    @test_dir��˵�����������Ĵ��·��
    @discover����װĿ¼�����з���patternҪ��Ĳ����ļ�
    @report_filename�����Ա�����ļ�������html�ļ�
    @runner������HTTPTestRunnerʵ��������discover���ļ��²�������
    """
    test_dir = "../script"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
    report_filename = f'../data/reports/tmp_{time.strftime("%Y%m%d%H%M%S")}.html'

    with open(report_filename,'w',encoding='utf-8') as f:
        runner = HTMLTestRunner(stream=f,title='httpbin.org������Ա���',description="�����ο�")
        runner.run(discover)
