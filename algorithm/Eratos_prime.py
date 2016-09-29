import time


input_num = input("Input num")
data = list(range(2, input_num))
print type(data)
def eratos(data):
    prime = []
    index = 0
    count = 0
    while True:
        if count == 0:
            prime.append(data.pop(0))
            count += 1
        if  data[index] % prime[-1] == 0:
            print "!! %s" % data[index]
            del data[index]
            index -= 1
        index += 1
        if index == len(data) - 1:
            index = 0
            prime.append(data.pop(0))
            print prime[-1], data[-1]
            if data[-1] < pow(prime[-1], 2):
                prime += data
                break
        print prime, index
        # time.sleep(1)
    return prime

print eratos(data)
