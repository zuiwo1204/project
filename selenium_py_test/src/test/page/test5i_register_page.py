#coding=utf-8
import sys
sys.path.append("C:\\PycharmProjects\\selenium_py_test")
from src.test.common.BasePage import BasePage

class Test5iRegisterPage(BasePage):
    email_loc = "user_email"
    username_loc = "user_name"
    password_loc = "password"
    code_text_loc = "code_text"
    email_error_loc = "user_email_error"
    user_name_error_loc = "user_name_error"
    password_error_loc = "user_password_error"
    code_text_error_loc = "code_text_error"
    submit_loc = "register_button"

    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url, self.pagetitle)

    # 调用send_keys对象，输入邮箱
    def input_email(self, email):
        self.find_element(self.email_loc).send_keys(email)

    # 调用send_keys对象，输入用户名
    def input_username(self, username):
        self.find_element(self.username_loc).send_keys(username)

    #调用send_keys对象，输入密码
    def input_password(self, password):
        self.find_element(self.password_loc).send_keys(password)

    # 调用send_keys对象，输入密码
    def input_code(self, code):
        self.find_element(self.code_text_loc).send_keys(code)

    # 调用send_keys对象，邮箱错误
    def get_email_error_text(self):
        return self.find_element(self.email_error_loc).text

    # 调用send_keys对象，邮箱错误
    def get_username_error_text(self):
        return self.find_element(self.user_name_error_loc).text

    # 调用send_keys对象，密码错误
    def get_pwd_error_text(self):
        return self.find_element(self.password_error_loc).text

    # 调用send_keys对象，输入验证码
    def get_code_error_text(self):
        return self.find_element(self.code_text_error_loc).text

    #调用send_keys对象，点击登录
    def click_submit(self):
        self.find_element(self.submit_loc).click()