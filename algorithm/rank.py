if __name__ == "__main__":
    score_list =  [40, 5, 90, 80, 70]
    rank_list = [1 for v in range(0,5)]
    for i, v in enumerate(score_list):
        for x in score_list:
            if x > v:
                rank_list[i] += 1
    print rank_list
