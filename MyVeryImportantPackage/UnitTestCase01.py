# coding=utf-8
import unittest



class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('在用例执行开始前执行一次，共执行一次')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('每个测试用例执行前运行一次')

    def test_a_run(self):
        print('开始执行第一个测试用例')
        self.assertEqual(1, 1)  # 测试用例

    def test_b_run(self):
        print('开始执行第二个测试用例')
        self.assertEqual(2, 3)  # 测试用例

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('每个测试用例执行后运行一次')

    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('所有测试用例执行完后运行一次')


