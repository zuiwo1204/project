# -*- coding: utf-8 -*-
from selenium import webdriver
import HTMLTestRunner
import unittest, time, re


class Test5iLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.close()
        self.assertEqual([], self.verificationErrors)


    def test_5itest_login(self):
        driver = self.driver
        driver.get("http://www.5itest.cn/login")
        driver.find_element_by_id("login_username").click()
        driver.find_element_by_id("login_username").clear()
        driver.find_element_by_id("login_username").send_keys("fdsgsv")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='注册帐号'])[1]/following::div[1]").click()
        driver.find_element_by_id("login_password").click()
        driver.find_element_by_id("login_password").clear()
        driver.find_element_by_id("login_password").send_keys("dvdfgbgfb")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='密码'])[1]/following::button[1]").click()


if __name__ == "__main__":
    #unittest.main()
    # 定义一个单元测试容器
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    testunit.addTest(Test5iLogin("test_5itest_login"))
    # 定义个报告存放路径，支持相对路径
    filename = 'C:\PycharmProjects\selenium_py_test\/result.html'
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'5itest登录测试报告',
        description=u'用例执行情况：',
        verbosity=2)
    # 运行测试用例
    runner.run(testunit)