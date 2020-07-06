#引用模块
import smtplib      #发邮件
from email.mime.text import MIMEText    #用于构建内容文本
from email.header import Header    #用于构建邮件头

class Email_sends:
        def sendEmail(self,moment):
                #服务器，端口
                host='smtp.qq.com'
                port=465
                #我方账户，授权码
                username='1426570981@qq.com'
                password='fsapfxfxguqvhcii'
                #对方账户
                to_addr=['2966835961@qq.com','778537175@qq.com']  #添加多个账户采用列表形式


                #要发送的内容(moment参数)
                #构建纯文本的邮件内容
                msg = MIMEText(moment,'plain','utf-8')   #文件内容/文本格式/编码
                #构建邮件头
                msg['From'] = Header('丁丁')       #2.from来自哪里，指发件人的名称或地址
                msg['To'] = Header('小可爱')         #3.to收件人邮箱地址
                msg['Subject'] = Header('我用python')    #4.主题

                try:
                        # 开启发信服务
                        server = smtplib.SMTP_SSL(host)
                        server.connect(host, port)
                        # 登录发信邮箱
                        server.login(username, password)
                        # 发送邮件
                        server.sendmail(username, to_addr, msg.as_string())
                        # 关闭服务器
                        server.quit()
                        print('发送成功')
                except:
                        print('发送失败')


        def getMoment(self,demo_counts,success_counts,fail_counts):
                moment="本次执行用例共"+demo_counts+"个,其中成功数量为"+success_counts+"个,失败数量为"+fail_counts+"个。"
                return moment

