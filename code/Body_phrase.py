import pymysql
import re

conn = pymysql.connect(host='localhost',
                        port= 3306,
                        db='test',
                        user='root',
                        password='plmadmin')
cursor = conn.cursor()

sql = 'select body from posts'

cursor.execute(sql)
result = cursor.fetchall()
for i in result:
    # res = nltk.sent_tokenize(str(i))
    # print(res)
    print("-------------------------------------------------------------------------------------------------------------------------------")
    str_ = str(i)
    str_done = re.sub("[<p></p>&#]","",str_)
    print(str_done)
    print(str_done.split('. '))



