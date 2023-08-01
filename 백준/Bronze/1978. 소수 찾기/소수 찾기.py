N = int(input())
num_list = list(map(int, input().split()))
result = 0
for num in num_list:
    chk = 0
    for i in range(1, num+1):
        if num%i == 0:
            chk += 1
    if chk == 2:
        result += 1

print(result)