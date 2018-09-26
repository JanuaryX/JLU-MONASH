import pymysql
import gensim
import logging
import os
from prepros import *

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
fname = os.path.join(os.pardir, "data", "model02")
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='1234',
                       db='stackoverflow')
cursor = conn.cursor()
sql = "select tags from Posts where tags is not null"
cursor.execute(sql)
tags = cursor.fetchall()
params = []

for tag in tags:
    tag_done = tag[0][1:-1].split('><')
    params.append(tag_done)
model = gensim.models.Word2Vec(params, min_count=2, size=200, workers=8)

model.save(fname)
