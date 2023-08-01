N = int(input())
num_list = list(map(int, input().split()))
result_list = []

chk = 0
for num in num_list:
    if num != 0:
        chk += 1
        result_list.append((chk))
    else:
        chk = 0
        result_list.append(chk)

print(sum(result_list))