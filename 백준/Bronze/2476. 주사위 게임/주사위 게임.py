N = int(input())
result = 0
for n in range(N):
    num_list = list(map(int, input().split()))
    chk_list = [0]*7
    for num in num_list:
        chk_list[num] += 1
    result_chk = 0
    bool_chk = False
    max_chk = 0
    for chk in range(7):
        if chk_list[chk] == 3:
            result_chk = 10000 + chk*1000
            bool_chk = True
            break
        if chk_list[chk] == 2:
            result_chk = 1000 + chk*100
            bool_chk = True
            break
        if chk_list[chk] == 1:
            if max_chk < chk:
                max_chk = chk
    if not bool_chk:
        result_chk = max_chk*100

    if result < result_chk:
        result = result_chk
print(result)
