from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    # 请自行修改下面的邮件发送者和接收者
    # 发送者
    sender = '你的邮箱@foxmail.com'
    # 接收者
    receivers = ['你的邮箱@aliyun.com']
    # 发送信息
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = Header('王大锤', 'utf-8')
    message['To'] = Header('骆昊', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    # , 465 将端口号删除
    smtper = SMTP('smtp.qq.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, '你的客户端授权码')
    # 若不加这行,在服务器环境会报错SMTPServerDisconnected("Connection unexpectedly closed")
    smtper.ehlo() 
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成')


if __name__ == '__main__':
    main()