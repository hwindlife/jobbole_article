import pymysql

if __name__ == '__main__':
    config = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "mysql",
        "database": "agentcard"
    }
    #连接数据库
    db = pymysql.connect(**config)
    #使用cursor()方法创建一个游标对象
    cursor = db.cursor()
    #使用execute()方法执行SQL语句
    cursor.execute("SELECT * FROM t_cus_info limit 2")
    #使用fetall()获取全部数据
    data = cursor.fetchall()
    #打印获取到的数据
    print(data)
    #关闭游标和数据库的连接
    cursor.close()
    db.close()