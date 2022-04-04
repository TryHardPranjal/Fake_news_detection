
from sklearn.feature_extraction.text import TfidfVectorizer
import collections

    class TfidfEmbeddingVectorizer(object):
        def __init__(self, word2vec):
            self.word2vec = word2vec
            self.word2weight = None
            self.dim = len(next(iter(word2vec.values())))
            #self.dim = len(word2vec.values())

    def features(sentence, index):
        sentence=[list[tfidf_train]]
        index=[w[index] for i in w]

    def fit(self, X, y):
        tfidf = TfidfVectorizer(analyzer=lambda x: x)
        tfidf.fit(X)

        open("test.txt", encoding = 'utf-8')