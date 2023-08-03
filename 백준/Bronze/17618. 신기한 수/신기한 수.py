N = int(input())
result = 0
for n in range(1, N+1):
    chk = sum([int(c) for c in str(n)])
    if n % chk == 0:
        result += 1

print(result)