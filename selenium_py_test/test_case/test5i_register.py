# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class Test5iRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_5itest_register(self):
        driver = self.driver
        driver.get("http://www.5itest.cn/register")
        driver.find_element_by_id("register_email").click()
        driver.find_element_by_id("register_email").clear()
        driver.find_element_by_id("register_email").send_keys("123452")
        driver.find_element_by_id("register_nickname").click()
        driver.find_element_by_id("register_nickname").clear()
        driver.find_element_by_id("register_nickname").send_keys("fdsfsgs")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='注册帐号'])[1]/following::div[1]").click()
        driver.find_element_by_id("register_password").click()
        driver.find_element_by_id("register_password").clear()
        driver.find_element_by_id("register_password").send_keys("dgsgfjhgmbmn")
        driver.find_element_by_id("content-container").click()
        driver.find_element_by_id("captcha_code").click()
        driver.find_element_by_id("captcha_code").clear()
        driver.find_element_by_id("captcha_code").send_keys("egxec")
        driver.find_element_by_id("register-btn").click()


if __name__ == "__main__":
    unittest.main()
