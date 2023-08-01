T = int(input())
A, B, C = 300, 60, 10

a = T // 300
T = T % 300
b = T // 60
T = T % 60
c = T // 10
T = T % 10

if T != 0:
    print(-1)
else:
    print(a, b, c)