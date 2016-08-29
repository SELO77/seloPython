def buble_sort(x):
    loop_count = 0
    for i in range(0, len(x)-1):
        for idx, j in enumerate(range(i+1, len(x))):
            if x[idx] > x[idx+1]:
                x[idx], x[idx+1] = x[idx+1], x[idx]
            loop_count += 1
    print loop_count
    return x


if __name__ == "__main__":
    test_list = [35, 80, 21, 53, 11, 45, 92, 39]
    result = buble_sort(test_list)
    print result
