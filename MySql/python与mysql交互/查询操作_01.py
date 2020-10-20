#  coding:utf-8
import pymysql


def main():
    # 一、创建连接对象
    # 1. host :服务器的主机地址(默认为localhost)
    # 2. port: mysql数据库的端口号(默认为3306)
    # 3. user :用户名
    # 4. password :密码
    # 5. database:操作的数据库
    # 6. charset：编码格式
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='huihuiyo',
                           db='test',
                           charset='utf8')

    # 二、获取游标，目的就是要执行sql语句
    cursor = conn.cursor()

    # 三、执行sql语句，返回受影响的行数
    sql = "select * from name where name = 'zhang'"
    cursor.execute(sql)
    # 下面方法防止sql注入
    # sql = "select * from name where name = %s"
    # cursor.execute(sql, ('zhang')) # 第二个参数是元组/列表/字典

    # 四、获取查询结果，得到的数据类型是一个元组，多条则为二维元组
    # 取查询的第一条结果
    # result = cursor.fetchone()
    # 取查询的全部数据
    result = cursor.fetchall()
    # 取查询的指定条数数据
    # result = cursor.fetchmany(3)  # 取3条
    print(result)

    # 五、关闭游标和连接
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
