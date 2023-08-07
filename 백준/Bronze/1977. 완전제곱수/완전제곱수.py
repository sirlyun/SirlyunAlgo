M = int(input())
N = int(input())

chk_list = []
for i in range(M, N+1):
    chk = i ** (1/2)
    if chk - int(chk) == 0:
        chk_list.append(i)

if len(chk_list) == 0:
    print(-1)
else:
    print(sum(chk_list))
    print(min(chk_list))