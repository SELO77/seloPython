import re
import reprlib


RE_WORD = re.compile('\w+')


class Sentence:


    def __init__(self, text):
        self.text = text


    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


    def __iter__(self):
        count = 0
        for match in RE_WORD.finditer(self.text):
            print(count)
            yield match.group()
            count += 1


s1 = Sentence('"The time ha... Walrus said,"')

for v in s1:
    print(v)