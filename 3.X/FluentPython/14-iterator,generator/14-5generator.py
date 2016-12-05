import re
import reprlib

RE_WORD = re.compile('\w+')

## Iterator by Generator function
class Sentence:


    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)


    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


    def __iter__(self):
        return iter(self.words)

    ## Generator function
    # def __iter__(self):
    #     for word in self.words:
    #         yield word

s1 = Sentence('"The time ha... Walrus said,"')
for v in s1:
    print(v)



# def generator_test():
#     s = iter("ABC")
#     for v in s:
#         yield v
#
# for v in generator_test():
#     print(v)