import gensim
import logging
import os

#../data/mymodel
fname = os.path.join(os.pardir,os.pardir, "data", "model02")
model = gensim.models.Word2Vec.load(fname)
print(model.wv.most_similar('python'))
