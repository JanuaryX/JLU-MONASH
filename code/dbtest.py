from pymysql import *

class dbHelper:
    def __init__(self, host, port, db, user, password, charset='utf8'):
        self.host = host#地址
        self.port = port#端口号
        self.db = db#数据库名
        self.user = user#用户名
        self.password = password#密码
        self.charset = charset

    def open(self):
        self.conn = connect(
            host = self.host,
            port = self.port,
            db = self.db,
            user = self.user,
            password = self.password,
            charset = self.charset
        )
        self.cursor = self.conn.cursor()#获取连接对象的数据库操作游标，提供了操作数据库所需方法
    def close(self):
        self.cursor.close()#关闭游标
        self.conn.close()#关闭连接

    def cud(self, sql, params):#增删改
        try:
            self.open()
            self.cursor.exectue(sql, params)#操作游标的执行方法
            self.conn.commit()#提交操作
            self.close()
        except Exception as e:
            print(e)
    def all(self,sql,params=[]):#查
        try:
            self.open()
            self.cursor.execute(sql, params)

            result = self.cursor.fetchall()#接受全部返回值
            self.close()
            return result
        except Exception as e:
            print(e)

sql = 'select * from posts where posts.Id = %s'#sql语句，使用参数传参用%s
helper = dbHelper('localhost',3306,'test','root','plmadmin')
params = [1]#用list的形式
result = helper.all(sql, params)
print(result)