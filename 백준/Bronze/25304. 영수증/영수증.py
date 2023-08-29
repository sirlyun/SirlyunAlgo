x = int(input())
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

price = 0
for i in range(n):
    a, b = arr[i]
    price += a*b

if price == x:
    print('Yes')
else:
    print('No')