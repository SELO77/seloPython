import re
import reprlib

RE_WORD = re.compile('\w+')

## Iterable
class Sentence:


    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)


    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


    def __iter__(self):
        return SentenceIterator(self.words)

## Iterator
class SentenceIterator:


    def __init__(self, words):
        self.words = words
        self.index = 0


    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word


    def __iter__(self):
        return self


s1 = Sentence('"The time ha... Walrus said,"')
print(s1)
print()

from collections import abc
print(issubclass(SentenceIterator, abc.Iterator))

