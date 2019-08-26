#coding=utf-8
import sys
sys.path.append("C:\\PycharmProjects\\selenium_py_test")
from src.test.common.BasePage import BasePage

class Test5iLoginPage(BasePage):
    username_loc = "username"
    password_loc = "password"
    login_btn_loc = "login-btn"
    username_error_loc = "username_error"
    password_error_loc = "password_error"
    login_error_loc = "login_error"

    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    def input_username(self,username):
        self.find_element(self.username_loc).send_keys(username)

    def input_password(self,password):
        self.find_element(self.password_loc).send_keys(password)

    def get_password_error_text(self):
        return self.find_element(self.password_error_loc).text

    def get_username_error_text(self):
        return self.find_element(self.username_error_loc).text

    def get_login_error_text(self):
        return self.find_element(self.login_error_loc).text

    def click_submit(self):
        self.find_element(self.login_btn_loc).click()