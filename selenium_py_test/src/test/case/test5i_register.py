# -*- coding: utf-8 -*-
import sys
sys.path.append("C:\\PycharmProjects\\selenium_py_test")
from selenium import webdriver
import unittest,time
from src.test.page.test5i_register_page import Test5iRegisterPage

class Test5iRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    # 用例执行体
    def test_login_mail(self):
        url = "http://www.5itest.cn/register"
        self.login_page = Test5iRegisterPage(self.driver, url, u"注册 - 乐学", "RegisterElement")

    def test_login_email_error(self):
        self.test_login_mail()
        self.login_page.open()
        self.login_page.input_email("11111")
        self.login_page.input_username("Mshishi")
        self.login_page.input_password("111111")
        self.login_page.input_code("ssss")
        self.login_page.click_submit()
        mess = self.login_page.get_email_error_text()
        self.assertTrue(mess,"请输入有效的电子邮件地址")

    def test_login_name_error(self):
        self.test_login_mail()
        self.login_page.open()
        self.login_page.input_email("11111@123.com")
        self.login_page.input_username("s")
        self.login_page.input_password("111111")
        self.login_page.input_code("ssss")
        self.login_page.click_submit()
        mess = self.login_page.get_username_error_text()
        self.assertTrue(mess,"字符长度必须大于等于4，一个中文字算2个字符")

    def test_login_password_error(self):
        self.test_login_mail()
        self.login_page.open()
        self.login_page.input_email("11111@123.com")
        self.login_page.input_username("ssss")
        self.login_page.input_password("111")
        self.login_page.input_code("sdee")
        self.login_page.click_submit()
        mess = self.login_page.get_pwd_error_text()
        self.assertTrue(mess,"最少需要输入5个字符")

    def test_login_code_error(self):
        self.test_login_mail()
        self.login_page.open()
        self.login_page.input_email("11111@123.com")
        self.login_page.input_username("ssss")
        self.login_page.input_password("111111")
        self.login_page.input_code("sdee")
        self.login_page.click_submit()
        mess = self.login_page.get_code_error_text()
        self.assertTrue(mess,"验证码错误")

if __name__ == "__main__":
    unittest.main()
