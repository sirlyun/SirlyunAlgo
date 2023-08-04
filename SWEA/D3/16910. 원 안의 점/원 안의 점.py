T = int(input())
for t in range(1, T+1):
    N = int(input()) # 반지름 N

    cnt = 0
    for x in range(201):
        for y in range(201):
           if x**2 + y**2 <= N**2:
               if x==0 and y==0:
                   cnt += 1
               elif (x==0 and y!=0) or (x!=0 and y==0):
                   cnt += 2
               else:
                   cnt += 4

    print(f'#{t}', cnt)