back_list = [[0]*1001 for _ in range(1001)]
N = int(input())
for n in range(1, N+1):
    a, b, width, height = map(int, input().split())
    for i in range(b, b+height):
        for j in range(a, a+width):
            back_list[i][j] = n
            
for n in range(1, N+1):
    result = 0
    for chk in range(1001):
        result += back_list[chk].count(n)
    print(result)