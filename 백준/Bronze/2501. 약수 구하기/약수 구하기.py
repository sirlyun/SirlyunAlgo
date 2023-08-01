N, K = map(int, input().split())

result_list = []
for n in range(1, N+1):
    if N % n == 0:
        result_list.append(n)

if len(result_list) < K:
    print(0)
else:
    print(result_list[K-1])