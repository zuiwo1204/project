#coding=utf-8
import sys
sys.path.append("C:\\PycharmProjects\\selenium_py_test")
from src.test.common.find_element import FindElement

from selenium import webdriver

class BasePage(object):
    def __init__(self,selenium_driver, base_url, pagetitle,node):
        self.base_url = base_url
        self.pagetitle = pagetitle
        self.driver = selenium_driver
        self.node = node

    # 打开页面，校验页面链接是否加载正确
    def _open(self, url, pagetitle):
        self.driver.get(url)
        self.driver.maximize_window()
        # 使用assert进行校验，打开的链接地址是否与配置的地址一致。调用on_page()方法
        assert self.on_page(pagetitle), u"打开开页面失败 %s" % url

    #使用current_url获取当前窗口Url地址，进行与配置地址作比较，返回比较结果（True False）
    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    # 定义script方法，用于执行js脚本，范围执行结果
    def script(self, src):
        self.driver.execute_script(src)

    #重新find_element方法
    def find_element(self, loc):
        ini_path = 'C:\PycharmProjects\selenium_py_test\config\FindElement.ini'
        fd = FindElement(self.driver,ini_path,self.node)
        return fd.get_element(loc)

    # 重写定义send_keys方法
    def send_keys1(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (loc))

    #重写switch_frame方法  切换窗口
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)