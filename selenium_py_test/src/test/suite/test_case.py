#coding = utf-8
import unittest
import HTMLTestRunner
import time
from src.test.suite.sent_mail import SendEmail
#这里需要导入测试文件

#testunit=unittest.TestSuite()

#将测试用例加入到测试容器(套件)中

#第一种方法
# testunit.addTest(unittest.makeSuite(Test5iRegister))
# testunit.addTest(unittest.makeSuite(Test5iLogin))

#第二种方法 循环测试测试用例
# alltestnames = [
#     Test5iRegister,
#     Test5iLogin
# ]
# for test in alltestnames:
#     testunit.addTest(unittest.makeSuite(test))

#第三种方法 使用discover()方法遍历所有的测试用例
listaa = 'C:\\PycharmProjects\\selenium_py_test\src\\test\\case'
def creatsuitel():
    testunit=unittest.TestSuite()
    # discover 方法定义
    discover = unittest.defaultTestLoader.discover(listaa,
                                                   pattern='test*.py',
                                                   top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

now = time.strftime('%Y-%m-%M-%H_%M_%S',time.localtime(time.time()))
alltestnames = creatsuitel()
filename = 'C:\\PycharmProjects\\selenium_py_test\\report\\'+now+'result1.html'

#执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(testunit)

fp = open(filename, 'wb')
# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'5itest测试报告',
        description=u'用例执行情况：',
        verbosity=2)

# 运行测试用例
runner.run(alltestnames)
fp.close()

#发送报告邮件
path = 'C:\\PycharmProjects\\selenium_py_test\\report'
SendEmail.sendreport('',path)