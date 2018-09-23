import unittest
from selenium import webdriver
from time import sleep
from parameterized import parameterized


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def baidu_search(self, search_key):
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(2)



    @parameterized.expand([
        #("用例名称", 具体数据,),    用例名称可不指定
        ("case01", "python"),
        ("case02","selenium"),
        ("case03","unittest")
    ])
#数组（列表list）里面放元组，，每一个元组里面放一条用例的数据
    def test_search_01(self,name,search_key):#name为用例名称，可要可不要，
        """ 测试搜索关键字"""
        dr = self.driver
        dr.get(self.base_url)
        self.baidu_search(search_key)
        title = dr.title
        self.assertEqual(title, search_key + "_百度搜索")

  

if __name__ == '__main__':
    unittest.main()
        
