import nltk
import random
import codecs
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
from nltk.tokenize import word_tokenize

file = codecs.open('ParodyLyrics.txt', 'r')
RandScript = file.read()
RandScriptTokenized= word_tokenize(RandScript)
words = RandScriptTokenized

word_dict = defaultdict(list)

for word, next_word in zip(words, words[1:]):
    word_dict[word].append(next_word)

word = "Creeper"

for i in range(1, 500):
    print(word, end=' ')
    word=random.choice(word_dict[word])

print(word)


