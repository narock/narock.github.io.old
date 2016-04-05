# configuration variables
from utils import dictFile, corpusFile

# import reading of directory
from os import walk

# setup logging
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# read the abstract files
documents = []
from utils import abstractPath
for (dirpath, dirnames, filenames) in walk(abstractPath):
    for fname in filenames:
      fullPath = dirpath + "/" + fname
      if ("-" in fullPath): # valid abstract files have - in the name, avoid .DS_Store and other OS files
          txt = open(fullPath)
          abstract = txt.read()
          try:
            abstract = abstract.decode('utf-8')
            abstract = abstract.replace('"','')
            documents.append(abstract)
            txt.close()
          except UnicodeError:
            print "string is not UTF-8 " + fullPath 

# import the gensim topic modeling library
from gensim import corpora, models, similarities

# remove stop words
from utils import stoplist
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
         for text in texts]

# create a bag of words vector representation 
##  Here we assigned a unique integer id to all words appearing in the corpus with the 
##  gensim.corpora.dictionary.Dictionary class. This sweeps across the texts, collecting 
##  word counts and relevant statistics. In the end, there are N distinct words in the 
##  processed corpus, which means each document will be represented by N numbers 
##  (ie., by a N dimensional vector). 
dictionary = corpora.Dictionary(texts)
dictionary.save(dictFile) # store for later use

# The function doc2bow() simply counts the number of occurences of each distinct word, 
# converts the word to its integer word id and returns the result as a sparse vector. 
# The sparse vector [(0, 1), (1, 1)] therefore reads: in the document 
# "Human computer interaction", the words computer (id 0) and human (id 1) appear once; 
# the other dictionary words appear (implicitly) zero times.
corpus = [dictionary.doc2bow(text) for text in texts]
# save the corpus in the Matrix Market format (http://radimrehurek.com/gensim/tut1.html#corpus-formats)
corpora.MmCorpus.serialize(corpusFile, corpus) # store to disk, for later use