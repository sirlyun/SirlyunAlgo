N, S = map(int, input().split())
num_list = list(map(int, input().split()))
result = 0

for i in range(1, 1<<N):
    chk = []

    for j in range(N):
        if 1<<j & i:
            chk.append(num_list[j])
    
    if sum(chk) == S:
        result += 1

print(result)