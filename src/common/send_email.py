#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


class SendEmail():
    # 构造函数
    def __init__(self, mail_host, mail_user, mail_pass, sender, receivers, subject, send_content):
        self.mail_host = mail_host  # 设置服务器
        self.mail_user = mail_user  # 用户名
        self.mail_pass = mail_pass  # 口令
        self.sender = sender  # 发送者
        self.receivers = receivers  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        self.subject = subject  # 主题
        self.send_content = send_content  # 发送内容

    def send_qq_email(self):
        # 第三方 SMTP 服务

        message = MIMEText(self.send_content, 'plain', 'utf-8')
        message['From'] = Header("爬虫机器人警告信息", 'utf-8')
        message['To'] = Header("尊敬的客户", 'utf-8')

        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)    # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers,
                             message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print(f"Error: 无法发送邮件:{e}")


if __name__ == '__main__':
    SendEmail(
mail_host="smtp.qq.com", mail_user="liyinchi@qq.com", mail_pass="jjkkxzlbiyyfbgfe", sender='233227763@qq.com', receivers=['233227763@qq.com'],subject="爬虫数据出现异常",send_content="爬虫数据出现异常!!!!!"
    ).send_qq_email()
