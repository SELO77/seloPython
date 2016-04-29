# JavaScript provides a built-in parseInt method.
#
# It can be used like this:
#
# parseInt("10") returns 10
# parseInt("10 apples") also returns 10
# We would like it to return "NaN" (as a string) for the second case because the input string is not a valid number.
#
# You are asked to write a myParseInt method with the following rules:
#
# It should make the conversion if the given string only contains a single integer value (and eventually spaces - including tabs, line feeds... - at both ends)
# For all other strings (including the ones representing float values), it should return NaN
# It should assume that all numbers are not signed and written in base 10

import re

def my_parse_int(string):
  # \D 숫자가 아닌 문자를 찾습니다. [^0-9]에 해당합니다.
  pass



my_parse_int("123 HELO")

# 정규식 없이 주민번호 포함하는 텍스트 파싱하기
data = """
SELO 870411-1122334
LEE  660099-1234123
"""

result = []
for line in data.split("\n"):
  word_result = []

  for word in line.split(" "):
    if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
      word = word[:6] + "-" + "*******"

    word_result.append(word)

  result.append("".join(word_result))

print("\n".join(result))


# 정규식을 이용한 파싱
pat = re.compile("(\d{6})[-]\d{7}]")
print(pat.sub("\g<1>-*******", data))