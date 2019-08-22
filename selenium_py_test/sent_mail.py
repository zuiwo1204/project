#coding=utf-8
from email.mime.text import MIMEText
import smtplib
import time,os

class SendEmail(object):

    # 定义发送邮件
    def sentmail(self,file_new):
        # 发信邮箱
        mail_from = '1021071864@qq.com'
        # 收信邮箱
        mail_to = '18174679235@163.com'

        # 定义正文
        f = open(file_new, 'rb')
        mail_body = f.read()
        f.close()
        msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')

        # 定义标题
        msg['Subject'] = u"5itest测试报告"

        # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
        msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        smtp = smtplib.SMTP()

        # 连接 SMTP 服务器，此处用的126的 SMTP 服务器
        smtp.connect('smtp.qq.com')

        # 用户名密码
        smtp.login('1021071864@qq.com', 'pkizggqjyalubfae')
        smtp.sendmail(mail_from, mail_to, msg.as_string())
        smtp.quit()
        if mail_body != b'':
            print('email has send out !')
        else :
            print('email has send error !',mail_body)

    # 查找测试报告，调用发邮件功能
    def sendreport(self,path):
        lists = os.listdir(path)
        lists.sort(key=lambda fn: os.path.getmtime(path + "\\" + fn) if not
        os.path.isdir(path + "\\" + fn) else 0)
        # 找到最新生成的文件
        file_new = os.path.join(path, lists[-1])
        print(u'最新测试生成的报告： ', file_new)
        # 调用发邮件模块
        SendEmail.sentmail('',file_new)

if __name__ == '__main__':
    path = 'C:\\PycharmProjects\\selenium_py_test\\report'
    SendEmail.sendreport('',path)