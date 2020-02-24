from my_pool import POOL  # 导入我们创建的数据库连接池包
import pymysql


# 打开连接
def create_conn():
    conn = POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    return conn,cursor


# 关闭连接
def close_conn(conn,cursor):
    cursor.close()
    conn.close()


# 插入一条数据
def insert(sql,args):
    conn,cursor = create_conn()
    res = cursor.execute(sql,args)
    conn.commit()
    close_conn(conn,cursor)
    return res


# 查询一条数据
def fetch_one(sql,args):
    conn,cursor = create_conn()
    cursor.execute(sql,args)
    res = cursor.fetchone()
    close_conn(conn,cursor)
    return res


# 查询所有数据
def fetch_all(sql,args):
    conn,cursor = create_conn()
    cursor.execute(sql,args)
    res = cursor.fetchall()
    close_conn(conn,cursor)
    return res


# sql = "insert into users(name,age) VALUES (%s, %s)"

# insert(sql,("mjj",9))

def func():
    # 检测当前正在运行连接数的是否小于最大链接数，如果不小于则：等待或报raise TooManyConnections异常
    # 否则
    # 则优先去初始化时创建的链接中获取链接 SteadyDBConnection。
    # 然后将SteadyDBConnection对象封装到PooledDedicatedDBConnection中并返回。
    # 如果最开始创建的链接没有链接，则去创建一个SteadyDBConnection对象，再封装到PooledDedicatedDBConnection中并返回。
    # 一旦关闭链接后，连接就返回到连接池让后续线程继续使用。
    conn = POOL.connection()

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM t_cus_info limit 2')
    result = cursor.fetchall()
    conn.close()
    return result


if __name__ == '__main__':
    print(func())

