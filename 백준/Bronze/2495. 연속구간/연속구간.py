for _ in range(3):
    N = input()
    result = 0
    cnt = 1
    for i in range(7):
        if N[i] == N[i+1]:
            cnt += 1
        else:
            cnt = 1
        if cnt > result:
            result = cnt

    print(result)