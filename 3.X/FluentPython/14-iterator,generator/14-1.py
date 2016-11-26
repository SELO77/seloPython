import re
import reprlib



RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)


    def __getitem__(self, index):
        return self.words[index]


    def __len__(self):
        return len(self.words)

    # def __iter__(self):
    #     return self.words

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


s1 = Sentence('"The time ha... Walrus said,"')
for word in s1:
    print(word)

print()

from collections import abc

print(isinstance(s1, abc.Iterable))
print(isinstance(s1, abc.Iterator))
print()

s2 = "ABC"
for v in s2:
    print(v)
print()

it1 = iter(s1)
it2 = iter(s2)
while True:
    try:
        print(next(it1))
    except StopIteration:
        break

print()



