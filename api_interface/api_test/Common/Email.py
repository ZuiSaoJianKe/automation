# -*- coding: utf-8 -*-
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
import time
import smtplib
def send_email(report_file):
    f=open(report_file,"rb")
    mail_body=f.read()
    f.close()

    username="xxxxx@xx.com"
    password="xxxxx"
    sender="xxxxx@xx.com"
    receiver=["xxxxx@xx.com","xxxxx@xx.com"]

    body=MIMEText(mail_body,"html","utf-8")
    msg=MIMEMultipart()
    msg['Subject'] = Header("自动化测试报告", 'utf - 8').encode()
    msg['From'] =Header( sender)
    print(msg['From'])
    msg['To'] = ";".join(receiver)
    print(msg["To"])
    msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    msg.attach(body)
    #添加附件
    att = MIMEApplication(open(report_file,"rb").read())
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=report_file)
    msg.attach(att)

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')  # 邮箱服务器
    smtp.login(username, password)  # 登录邮箱
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送者和接收者
    smtp.quit()
    print("邮件已发出！注意查收。")

# send_email("D:\\PycharmProjects\\api_interface\\api_test\\result\\2020-04-02_11_09_10result.html")