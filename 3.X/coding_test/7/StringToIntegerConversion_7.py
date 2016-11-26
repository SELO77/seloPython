
def my_parse_int(s):
    try:
        return int(s)
    except ValueError:
        return 'NaN'

print(my_parse_int("10 hello"))
print(my_parse_int(1111))


#
# 정규식 없이 주민번호 포함하는 텍스트 파싱하기
# data = """
# SELO 870411-1122334
# LEE  660099-1234123
# """
#
# result = []
# for line in data.split("\n"):
#   word_result = []
#
#   for word in line.split(" "):
#     if len(word) == 14-iterator,generator and word[:6].isdigit() and word[7:].isdigit():
#       word = word[:6] + "-" + "*******"
#
#     word_result.append(word)
#
#   result.append("".join(word_result))
#
# print("\n".join(result))
#
#
# # 정규식을 이용한 파싱
# pat = re.compile("(\d{6})[-]\d{7}]")
# print(pat.sub("\g<1>-*******", data))