# -*- coding: utf-8 -*-
from selenium import webdriver
import HTMLTestRunner
import unittest
import sys
sys.path.append("C:\\PycharmProjects\\selenium_py_test")
from src.test.page.test5i_login_page import Test5iLoginPage


class Test5iLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.close()
        self.assertEqual([], self.verificationErrors)

    def login_base(self,username,password):
        self.test_login_mail()
        self.login_page.open()
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_submit()


    # 用例执行体
    def test_login_mail(self):
        url = "http://www.5itest.cn/login"
        self.login_page = Test5iLoginPage(self.driver, url, u"登录 - 乐学", "LoginElement")

    def test_login_username_error(self):
        self.login_base("","11111")
        mess = self.login_page.get_username_error_text()
        self.assertTrue(mess, "请输入账号")

    def test_login_password_error(self):
        self.login_base("sss","")
        mess = self.login_page.get_password_error_text()
        self.assertTrue(mess, "请输入密码")

    def test_login_error(self):
        self.login_base("sss", "111")
        mess = self.login_page.get_login_error_text()
        self.assertTrue(mess, "用户名或密码错误")

if __name__ == "__main__":
    #unittest.main()
    # 定义一个单元测试容器
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    testunit.addTest(Test5iLogin("test_login_username_error"))
    testunit.addTest(Test5iLogin("test_login_password_error"))
    testunit.addTest(Test5iLogin("test_login_error"))
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