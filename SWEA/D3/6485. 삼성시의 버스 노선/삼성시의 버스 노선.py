T = int(input())
for t in range(1, T+1):
    N = int(input())
    stop_dict = {}
    for i in range(1, 5001):
        stop_dict[i] = 0

    for n in range(N):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            stop_dict[i] += 1

    P = int(input())
    result = []
    for p in range(P):
        result.append(stop_dict[int(input())])
        
    print(f'#{t}', *result)
