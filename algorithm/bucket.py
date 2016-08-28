if __name__ == "__main__":
    scores_list = [8, 2, 1, 5, 9, 7]
    rank_box = [1 for v in range(0, len(scores_list))]
    for i, v in enumerate(scores_list):
        for e in scores_list:
            if e > v:
               rank_box[i] += 1
    print("rank_box:%s" % rank_box)

    bucket_list = [0 for v in range(0,10)]
    for v in scores_list:
        bucket_list[v] = v
        print(bucket_list)
#    print bucket_list
    sorted_list = [e for e in bucket_list if e]
    print(sorted_list)
#    print sorted_list
