import json
import http.client, mimetypes
from urllib.parse import urlencode
import random
import time
import re
import logging
import os, sys

try:
    import xlrd
except:

    # 就是 -U，-upgrade，意思是如果已安装就升级到最新版
    os.system('pip install -U xlrd')
    import xlrd
try:
    from pyDes import *
except ImportError as e:
    os.system('pip install -U pyDes --allow-external pyDes --allow-unverified pyDes')
    from pyDes import *
import hashlib
import base64
import smtplib
from email.mime.text import MIMEText

# 1、os.getcwd()：获取当前工作目录，也就是在哪个目录下运行这个程序。
# os.path.join()函数: 连接两个或者更多的路径名组件
'''
format参数中可能用到的格式化串：
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息
'''
log_file = os.path.join(os.getcwd(), 'log/liveappapi.log')

# 更改日志信息格式以显示 TIME、LEVEL 和 MESSAGE。
log_format = '[%(asctime)s] [%(levelname)s] %(message)s'

# format为处理程序使用指定的格式字符串。
# 将根记录器级别设置为指定的级别。默认生成的 root logger 的 level 是 logging.WARNING，低于该级别的就不输出了。级别排序：CRITICAL > ERROR > WARNING > INFO > #DEBUG。（如果需要显示所有级别的内容，可将 level=logging.NOTSET）
# filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
logging.basicConfig(format=log_format, filename=log_file, filemode='w', level=logging.DEBUG)

'''
Handler：
logging.StreamHandler 可以向类似与sys.stdout或者sys.stderr的任何文件对象(file object)输出信息
logging.FileHandler 用于向一个文件输出日志信息
logging.handlers.RotatingFileHandler 类似于上面的FileHandler，但是它可以管理文件大小。当文件达到一定大小之后，它会自动将当前日志文件改名，然后创建一个新的同名日志文件继续输出
logging.handlers.TimedRotatingFileHandler 和RotatingFileHandler类似，不过，它没有通过判断文件大小来决定何时重新创建日志文件，而是间隔一定时间就自动创建新的日志文件
logging.handlers.SocketHandler 使用TCP协议，将日志信息发送到网络。
logging.handlers.DatagramHandler 使用UDP协议，将日志信息发送到网络。
logging.handlers.SysLogHandler 日志输出到syslog
logging.handlers.NTEventLogHandler 远程输出日志到Windows NT/2000/XP的事件日志
logging.handlers.SMTPHandler 远程输出日志到邮件地址
logging.handlers.MemoryHandler 日志输出到内存中的制定buffer
logging.handlers.HTTPHandler 通过”GET”或”POST”远程输出到HTTP服务器

创建一个 StreamHandler,用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
'''
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(log_format)
console.setFormatter(formatter)

# 将定义的东西添加到logging
logging.getLogger('').addHandler(console)

logging.info('hello_word')