#  coding:utf-8
import pymysql


# 1. host :服务器的主机地址(默认为localhost)
# 2. port: mysql数据库的端口号(默认为3306)
# 3. user :用户名
# 4. password :密码
# 5. database:操作的数据库
# 6. charset：编码格式
def main():
    # 一、创建连接对象
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='huihuiyo',
                           db='test',
                           charset='utf8')
    # 二、获取游标，目的就是要执行sql语句
    cursor = conn.cursor()
    # 插入
    # sql = "insert into name(id,name) values(%s, %s);"
    # 修改
    sql = "update name set name = %s where id = %s;"
    # 删除
    # sql = 'delete from name where id = 1;'
    try:
        # 三、执行sql语句，返回受影响的行数
        row = cursor.execute(sql, ['zhu', 4])
        print('受影响的行数为：', row)
        # 四、提交修改的数据到数据库
        conn.commit()
    except Exception as e:
        # 对修改的数据进行撤销﹐表示数据回滚（回到没有修改数据之前的状态）
        conn.rollback()
    finally:
        # 五、关闭游标和连接
        cursor.close()
        conn.close()


if __name__ == '__main__':
    main()
