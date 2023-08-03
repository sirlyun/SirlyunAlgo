N = int(input())
result = 0
for n in range(1, N+1):
    chk = 0
    for i in str(n):
        chk += int(i)
    if n % chk == 0:
        result += 1

print(result)