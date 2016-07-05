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



print(triple_double(1234445533, 441233))
print(triple_double(12344553, 441233))
assert triple_double(1234445533, 441233) == 1


