
def rotation_quadrangle(x, y):
  directions = [0, 1, 2, 3] # 0 오른쪽, 1 아래, 2 왼쪽, 3 위


def make_quadrangle(x, y):
  double_arr = []
  # for v in range(0, x):
  #   for q in range(0, y):
  #     print(v, q)
  #     double_arr[v].append(x*y)

  for v in range(x):
    double_arr[v] = [[0]*y]

  return double_arr


temp = []
for x in range(2):
  temp.append([v for v in range(3)])

print(temp)