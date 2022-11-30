#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 12:01:20 2022

@author: keithcheng
"""

from urllib.request import urlopen
from nltk.tokenize import word_tokenize


target_url0 = 'http://www.gutenberg.org/files/135/135-0.txt'
book_raw = urlopen(target_url0).read().decode('utf-8')
#%%
word_tokens  = word_tokenize(book_raw)
print(book_raw[1:200])
print(word_tokens[1:40])

#%%
from nltk.corpus import stopwords
stop_words   = (stopwords.words('english'))

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  

  
print(word_tokens[1:40])
print(filtered_sentence[1:40])
print(stop_words)
#%%
#Monte-cristo
target_url1 = 'https://www.gutenberg.org/files/1184/1184-0.txt'
#Leo Tolstoy
target_url2 = 'https://www.gutenberg.org/files/2600/2600-0.txt'
#Don Quijote
target_url3 = 'https://www.gutenberg.org/cache/epub/996/pg996.txt'
#%%
book_raw1 = urlopen(target_url1).read().decode('utf-8')
word_token1 = word_tokenize(book_raw1)
filtered_sentence1 = [w for w in word_token1 if not w.lower() in stop_words]
print(len(book_raw1))
print(len(word_token1))
print(len(filtered_sentence1))
#%%
book_raw2 = urlopen(target_url2).read().decode('utf-8')
word_token2 = word_tokenize(book_raw2)
filtered_sentence2 = [w for w in word_token2 if not w.lower() in stop_words]
print(len(book_raw2))
print(len(word_token2))
print(len(filtered_sentence2))
#%%
book_raw3 = urlopen(target_url3).read().decode('utf-8')
word_token3 = word_tokenize(book_raw3)
filtered_sentence3 = [w for w in word_token3 if not w.lower() in stop_words]
print(len(book_raw3))
print(len(word_token3))
print(len(filtered_sentence3))
#  Leo Tolstoy has more words than the others, which consists of 3,293,553 words
#%%
from nltk.tokenize import sent_tokenize
Miserables_sentences1 = sent_tokenize(book_raw1)
Miserables_sentences2 = sent_tokenize(book_raw2)
Miserables_sentences3 = sent_tokenize(book_raw3)
#%%
Num0fSentences1 = len(Miserables_sentences1)
Num0fSentences2 = len(Miserables_sentences2)
Num0fSentences3 = len(Miserables_sentences3)
#%%
print('Monte-cristo :',Num0fSentences1,'Leo Tolstoy :',
      Num0fSentences2,'Don Quijote',Num0fSentences3)
#%% Average length of sentences
Avgsentenceslen1 = len(word_token1)/Num0fSentences1
Avgsentenceslen2 = len(word_token2)/Num0fSentences2
Avgsentenceslen3 = len(word_token3)/Num0fSentences3
print(Avgsentenceslen1, Avgsentenceslen2, Avgsentenceslen3)
#%%
from nltk import FreqDist 
fdist_book1 = FreqDist(word_token1)
fdist_book2 = FreqDist(word_token2)
fdist_book3 = FreqDist(word_token3)
#%%
filtered_word_freq1 = dict((word_token1,freq) for word_token1, freq in fdist_book1.items())
#%%
sorted_filter_wordfreq1 = dict(sorted(filtered_word_freq1.items(),key= lambda x:x[1],reverse=True))
max1 = max(sorted_filter_wordfreq1, key=sorted_filter_wordfreq1.get)
max2 = sorted_filter_wordfreq1[max(sorted_filter_wordfreq1, key=sorted_filter_wordfreq1.get)]
print(max1,max2)
