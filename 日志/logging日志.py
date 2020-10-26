# coding:utf-8

# 日志等级默认是warning,只有大于等于当前日志级别的日志才会输出显示
import logging

logging.basicConfig(
    level=logging.DEBUG,  # 设置日志的记录级别(DEBUG则可以记录全部)
    filename='log.txt',  # 设置文件输出名称
    filemode='a',  # 设置输出的文件模式（a,w,r）
    format="%(asctime)s -- %(name)s -- %(filename)s [line:%(lineno)d] - %(levelname)s - %(message)s"
)
logging.debug('这是debug')
logging.info('这是info')
logging.warning('这是warning')
logging.error('这是error')
logging.critical('这是critical')
