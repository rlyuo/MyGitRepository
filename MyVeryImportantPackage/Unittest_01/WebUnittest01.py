# coding=utf-8
import unittest
from selenium import webdriver
import time

class baidu_test_2(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(15)
        cls.driver.get(r'http://www.baidu.com')

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_baidu_enabled(self):
        so=self.driver.find_element_by_id('kw')    #检查元素是否可编辑用is_enabled()，可以编辑返回的是True
        self.assertTrue(so.is_enabled())   #如果返回的是True，那么就是真真为真~通过
    def test_baidu_sousuo(self):
        so = self.driver.find_element_by_id('kw')
        so.send_keys('你好中国')  #上面的代码选择了输入框，这是输入：send_keys()
        self.driver.find_element_by_id('su').click()   #该方法是模拟点击操作click()
        print(so.get_attribute('value'))     #根据属性获取表单中的值get_attribute('value')
        self.assertEqual(so.get_attribute('value'),'你好中国')       #我们用获取到的值，和我们预期的值做对比，看是否相等
        time.sleep(10)

if __name__ == '__main__':
    unittest.main(verbosity=2)


'''

'''

