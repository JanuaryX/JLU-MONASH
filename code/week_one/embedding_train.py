import gensim
import logging
import pymysql
import os
from prepros import get_words

fname = os.path.join(os.pardir, "data", "model01")

start = 0
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class MySentences(object):

    def __iter__(self):
        current_id = 0
        try:
            cnx = pymysql.connect(host='localhost',
                                  user='root',
                                  password='1234',
                                  db='stackoverflow')
            cursor = cnx.cursor()
            query = "SELECT Id, Body FROM Posts WHERE Score >= 0 AND Id < 40000000"
            cursor.execute(query)
            for current_id, row in cursor.fetchall():
                words_list = get_words(row)
                for words in words_list:
                    yield words
        finally:
            print("current_id: {}".format(current_id))

sentences = MySentences()

model = gensim.models.Word2Vec(sentences, min_count=2, size=200, workers=8)
model.save(fname)