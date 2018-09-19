import pymysql
import gensim
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class dbHelper:
    def __init__(self, host, port, db, user, password, charset='utf8'):
        self.host = host#地址
        self.port = port#端口号
        self.db = db#数据库名
        self.user = user#用户名
        self.password = password#密码
        self.charset = charset

    def open(self):
        self.conn = pymysql.connect(
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
    def all(self,sql, params=[]):#查
        try:
            self.open()
            self.cursor.execute(sql, params)

            result = self.cursor.fetchall()#接受全部返回值
            self.close()
            return result
        except Exception as e:
            print(e)
sql = 'select tags from posts where tags is not null'
helper = dbHelper('localhost',3306,'test','root','plmadmin')
params = []
result = helper.all(sql,params)
print(result)
model = gensim.models.Word2Vec(result, min_count=1, size=200, workers=8)
print(model)


print(model.wv.similarity('fdm','brims'))
print(model.wv['fdm'])
print(model.wv.most_similar(['python']))
