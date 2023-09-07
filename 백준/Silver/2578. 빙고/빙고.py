def check(arr):
    bingo = 0

    for i in range(5):
        cnt_r = 0
        cnt_c = 0
        for j in range(5):
            if arr[i][j] == 0:
                cnt_r += 1
            if arr[j][i] == 0:
                cnt_c += 1
        if cnt_r == 5:
            bingo += 1
        if cnt_c == 5:
            bingo += 1

    cnt_d1 = 0
    cnt_d2 = 0
    for i in range(5):
        if arr[i][i] == 0:
            cnt_d1 += 1
        if arr[i][4-i] == 0:
            cnt_d2 += 1
    if cnt_d1 == 5:
        bingo += 1
    if cnt_d2 == 5:
        bingo += 1

    return bingo




arr = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
flag = 1


for i in range(5):
    for j in range(5):
        cnt += 1
        n = call[i][j]
        # tmp = bingo ## 
        for k in range(5):
            for l in range(5):
                # print('arr[i][j]', arr[i][j], 'n', n)
                if arr[k][l] == n:
                    arr[k][l] = 0
                    bingo = check(arr)
                    # print(bingo)
                    

        # if tmp < bingo:
        #     print('bingo',bingo)
        #     for a in arr:
        #         print(a)
        #     print()
        
        if bingo >= 3:
            flag = 0
            break

    if flag == 0:
        break
            

print(cnt)







