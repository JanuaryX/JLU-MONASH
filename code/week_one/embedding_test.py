import gensim
import logging
import os

#../data/mymodel
fname = os.path.join(os.pardir,os.pardir, "data", "model01")
model = gensim.models.Word2Vec.load(fname)
print(model.wv.most_similar('python'))
print(model.wv.similarity('python','java'))
print(model.wv.most_similar(positive=['python','nltk'],negative=['java'],topn=1))
