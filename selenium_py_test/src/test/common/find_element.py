#coding=utf-8
from src.utils.read_ini import ReadIni
from selenium.webdriver.support.wait import WebDriverWait

class FindElement(ReadIni):
    def __init__(self, driver,file_name,node):
        self.driver = driver
        self.file_name = file_name
        self.node = node

    def get_element(self, key):
        read_ini = ReadIni(self.file_name,self.node)
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'classname':
                return self.driver.find_element_by_class_name(value)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(value)
        except:
            #self.driver.save_screenshot('', value)
            print(u"%s 页面中未能找到 %s 元素" % (self, value))
            return None
