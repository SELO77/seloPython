# Write a function
#
# triple_double(num1, num2)
# which takes in numbers num1 and num2 and returns 1 if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.
# For example:
# triple_double(451999277, 41177722899) == 1 // num1 has straight triple 999s and
#                                           // num2 has straight double 99s
#
# triple_double(1222345, 12345) == 0 // num1 has straight triple 2s but num2 has only a single 2
#
# triple_double(12345, 12345) == 0
#
# triple_double(666789, 12345667) == 1


def triple_double(num1, num2):
  check_num = parsing_num(num1)
  if check_num:
    str_num2 = str(num2)
    length = len(str_num2)
    for idx, val in enumerate(str_num2):
      if check_num == val:
        if idx + 1 < length:
          if val == str_num2[idx + 1]:
            return 1
  return 0

def parsing_num(num):
  num_list = [v for v in str(num)]
  length = len(num_list)
  for idx, val in enumerate(num_list):
    if idx + 1 < length:
      if val == num_list[idx + 1]:
        if idx + 2 < length:
          if val == num_list[idx + 2]:
            return val
  return False


### Good Solutions

# def triple_double(num1, num2):
#     return any([i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789'])
#
# def triple_double(num1, num2):
#     for x in range(10):
#         if str(x) * 3 in str(num1):
#             if str(x) * 2 in str(num2):
#                 return 1
#     return 0
#
# import re
# def triple_double(num1, num2):
#     #code me ^^
#     r3 = re.compile(r'(\d)\1\1')
#     f = r3.findall(str(num1))
#     if len(f)>0:
#         r2 = re.compile(f[0]+'{2}')
#         if len(r2.findall(str(num2))):
#             return 1
#     return 0



