### python日志

```python
import logging

# 日志级别：CRITICAL(严重的)>ERROR()>WARNING()>INFO()>DEBUG()
logging.basicConfig(
    level = logging.DEBUG,   # 设置日志的记录级别(DEBUG则可以记录全部)
    filename='log.log',
    filemode='a',
    format="%(asctime)s -- %(name)s -- %(filename)s [line:%(lineno)d] - %(levelname)s - %(message)s"
    )
logging.debug('这是debug')
logging.info('这是info')
logging.warning('这是warning')
logging.error('这是error')
logging.critical('这是critical')
```

得到：

```python
2020-10-07 12:39:57,735 -- root -- test.py [line:9] - DEBUG - 这是debug
2020-10-07 12:39:57,735 -- root -- test.py [line:10] - INFO - 这是info
2020-10-07 12:39:57,735 -- root -- test.py [line:11] - WARNING - 这是warning
2020-10-07 12:39:57,735 -- root -- test.py [line:12] - ERROR - 这是error
2020-10-07 12:39:57,735 -- root -- test.py [line:13] - CRITICAL - 这是critical
```



- 日志配置参数

  - |   参数   |                             作用                             |
    | :------: | :----------------------------------------------------------: |
    | filename |                     设定日志输出的文件名                     |
    | filemode |              设置输出的文件模式：r[+],w[+],a[+]              |
    |  format  |                      设置日志的输出格式                      |
    | datefat  |                    日志附带日期时间的格式                    |
    |  style   |                   格式占位符，默认为%和{}                    |
    |  level   |                      设置日志的输出级别                      |
    |  stream  | 定义输出流，用来初始化StreamHandler对象，不能与filename一起使用 |
    | handles  |      定义处理器对象，不能与filename、stream参数一同使用      |

- 格式化变量

  - |    变量     |      格式       | 变量说明                                                     |
    | :---------: | :-------------: | :----------------------------------------------------------- |
    |   asctime   |   %(asctime)s   | 将日志的时间构造成可读的形式，默认情况下精确到毫秒，如：2020-10-07 12:39:57,735。也可以额外指定datefmt参数来指定该变量的格式 |
    |    name     |    %(name)s     | 日志对象的名称                                               |
    |  filename   |  %(filename)s   | 不包含路径的文件名                                           |
    |  pathname   |  %(pathname)s   | 包含路径的文件名                                             |
    |  funcName   |  %(funcName)s   | 日志记录所在的函数名                                         |
    |  levelname  |  %(levelname)s  | 日志级别的名称                                               |
    |   message   |   %(message)s   | 具体的日志信息                                               |
    |   lineno    |   %(lineno)s    | 日志记录所在的行号                                           |
    |   process   |   %(process)s   | 当前进程id                                                   |
    | processName | %(processName)s | 当前进程名称                                                 |
    |   thread    |   %(thread)d    | 当前线程id                                                   |
    | threadName  | %(threadName)s  | 当前线程名称                                                 |

    