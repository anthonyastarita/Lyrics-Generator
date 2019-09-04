import nltk
import random
import codecs
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
from nltk.tokenize import word_tokenize

file = codecs.open('/Users/anthonyastarita/Github/ParodyLyrics.txt', 'r')
RandScript = file.read()
RandScript = RandScript.lower()
stopwords = ['[',']','(',')']

RandScriptTokenized= word_tokenize(RandScript)
tokenizedWords = RandScriptTokenized

words = [item for item in tokenizedWords if item not in stopwords]

word_dict = defaultdict(list)

for word, next_word in zip(words, words[1:]):
    word_dict[word].append(next_word)

word = "diamonds"

for i in range(1, 500):
    print(word, end=' ')
    word=random.choice(word_dict[word])

print(word)


