N = int(input())
time_list = [list(map(int, input().split())) for _ in range(N)]
time_list.sort(key=lambda x: (x[1], x[0]))

result = 1
pre = time_list[0][1]
for n in range(1, N):
    if time_list[n][0] >= pre:
        result += 1
        pre = time_list[n][1]

print(result)