# Given the triangle of consecutive odd numbers:
#
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:
#
# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8

def row_sum_odd_numbers(n):
  num_line = n + 1
  set_num = 1
  set_line = []
  sum_line_list= []

  for v in range(1, num_line):
    sum_line = ""

    for t in range(set_num, set_num + v):
      sum_line += "%s,"%(2 * t - 1)
      if t == set_num + v - 1:
        set_num = set_num + v

    set_line.append(sum_line)

  for v in set_line:
    temp_list = v.split(',')[:-1]
    result = sum([int(t) for t in temp_list])
    sum_line_list.append(result)

  return sum_line_list[-1:].pop()

# row_sum_odd_numbers(2)
print(row_sum_odd_numbers(3))
# row_sum_odd_numbers(4)
# row_sum_odd_numbers(5)