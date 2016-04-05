# configuration values
from utils import dictFile, corpusFile, logFile

# set up logging
import logging
logging.basicConfig(filename=logFile, format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# import from gensim
from gensim import corpora, models, similarities

# read the diction and corpus from disk
dictionary = corpora.Dictionary.load(dictFile)
corpus = corpora.MmCorpus(corpusFile)

# print some basic statistics about the corpus
print(corpus)

# transform the corpus to TF-IDF model
tfidf = models.TfidfModel(corpus)

# transformation
corpus_tfidf = tfidf[corpus]

# number of topics to consider
n_topics = 10

# transform one more time into LDA
model = models.LdaModel(corpus, id2word=dictionary, num_topics=n_topics, alpha='auto', eval_every=1, passes=50)
model.print_topics(n_topics)