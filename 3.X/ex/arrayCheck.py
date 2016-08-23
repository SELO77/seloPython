a = 'RN_MSP'
b = ['RN', 'RT', 'CN']

test = "asdfkl_RN"
test1 = "RN"

# print(test.find(test1))
# print(a.find(b[0]))

result = list(filter(lambda x: a.find(x)  > -1, b))

print(str(result))