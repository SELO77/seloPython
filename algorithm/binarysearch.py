target = 17
data = list(range(100))

def binary_search(target, data):
    index = int(len(data)/2)
    print(target, index, data)
    if target == data[index]:
        last = "hello {0}".format(target)
        return last
    elif target > data[index]:
        binary_search(target, data[index + 1:])
    elif target < data[index]:
        binary_search(target, data[:index])
    if index == 0:
        return "I can't find"





print(binary_search(target, data))
