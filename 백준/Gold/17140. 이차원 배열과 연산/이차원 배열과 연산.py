'''
    크기가 3x3인 배열 A
    1초마다 배열에 연산 적용
        R 연산: 배열 A의 모든 행에 대하여 정렬을 수행, 행의 개수 >= 열의 개수인 경우에 적용
        C 연산: 배열 A의 모든 열에 대하여 정렬을 수행, 행의 개수 < 열의 개수인 경우에 적용
    한 행 또는 열에 있는 수를 정렬하려면 각각의 수가 몇번 나왔는지를 알아야 한다
    그 다음 수의 등장 횟수가 커지는 순으로 그러한 것이 여러가지면 수가 커지는 순으로 정렬
    그 다음에는 배열 A에 정렬된 수를 다시 넣어야 한다
    정렬된 결과를 배열에 넣을 때는 수와 등장 횟수를 모두 넣으며 순서는 수가 우선이다.
        [3, 1, 1]에는 3이 1번, 1가 2번 등장한다.
        정렬된 결과는 [3, 1, 1, 2]가 된다. 
        다시 이 배열에는 3이 1번, 1이 2번, 2가 1번 등장한다. 
        다시 정렬하면 [2, 1, 3, 1, 1, 2]가 된다.

    행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.
'''

def cal_R():
    global A
    new_arr = []
    max_cnt = 0
    for i in A:
        chk_dict = {}
        for j in i:
            if j != 0:
                chk_dict.setdefault(j, 0)
                chk_dict[j] += 1

        tmp = sorted(chk_dict.items(), key=lambda x:(x[1], x[0]))
        chk = []
        for t in tmp:
            chk.append(t[0])
            chk.append(t[1])
        new_arr.append(chk[:100])
        max_cnt = max(max_cnt, len(tmp)*2)

    for i in range(len(new_arr)):
        cnt = len(new_arr[i])
        if cnt < max_cnt:
            for _ in range(max_cnt-cnt):
                new_arr[i].append(0)
    A = new_arr
    

def cal_C():
    global A
    A = [[row[i] for row in A] for i in range(len(A[0]))]

    new_arr = []
    max_cnt = 0
    for i in A:
        chk_dict = {}
        for j in i:
            if j != 0:
                chk_dict.setdefault(j, 0)
                chk_dict[j] += 1

        tmp = sorted(chk_dict.items(), key=lambda x:(x[1], x[0]))
        chk = []
        for t in tmp:
            chk.append(t[0])
            chk.append(t[1])
        new_arr.append(chk[:100])
        max_cnt = max(max_cnt, len(tmp)*2)

    for i in range(len(new_arr)):
        cnt = len(new_arr[i])
        if cnt < max_cnt:
            for _ in range(max_cnt-cnt):
                new_arr[i].append(0)
    

    A = [[row[i] for row in new_arr] for i in range(len(new_arr[0]))]


R, C, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

if 0<=R<=3 and 0<=C<=3:
    if A[R-1][C-1] == K:
        print(0)
        exit()

for i in range(101):
    if 0<=R-1<len(A) and 0<=C-1<len(A[0]):
        if A[R-1][C-1] == K:
            print(i)
            break

    if len(A[0]) > len(A):
        cal_C()
    else:
        cal_R()
else:
    print(-1)