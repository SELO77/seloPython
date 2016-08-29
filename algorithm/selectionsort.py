def selectionsort(list):
    minimum = {
                "index": None,
                "value": None,
            }
    index = 0
    loop_count = 0
    for v in range(0, len(list)):
        for e in range(index, len(list)):
            if e == index:
                minimum['index'] = e
                minimum['value'] = list[e]
                continue
            if minimum['value'] > list[e]:
                minimum['index'] = e
                minimum['value'] = list[e]
            loop_count += 1
        temp = list[v]
        list[v] = minimum['value']
        list[minimum['index']] = temp
        index += 1
    print loop_count
    return list

if __name__ == "__main__":
    test_list = [35, 80, 21, 53, 11, 45, 92, 39]
    result = selectionsort(test_list)
    print result
