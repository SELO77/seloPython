def selection_sort(x):
    loop_count = 0
    for i in range(len(x)-1):
        for j in range(i+1, len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
            loop_count += 1
            print x
    print loop_count
    return x

if __name__ == "__main__":
    test_list = [35, 80, 21, 53, 11, 45, 92, 39]
    result = selection_sort(test_list)
    print result
