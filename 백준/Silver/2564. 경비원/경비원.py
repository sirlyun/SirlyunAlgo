N, M = map(int, input().split())
shop = int(input())
shop_list = [list(map(int, input().split())) for _ in range(shop)]
man_di, man_dist = map(int, input().split())

result = 0

if man_di == 1:
    for s in shop_list:
        if s[0] == 1:
            result += abs(man_dist - s[1])
        elif s[0] == 2:
            result += M + min((man_dist + s[1]), (2*N - man_dist - s[1]))
        elif s[0] == 3:
            result += man_dist + s[1]
        else:
            result += N - man_dist + s[1]

elif man_di == 2:
    for s in shop_list:
        if s[0] == 1:
            result += M + min((man_dist + s[1]), (2*N - man_dist - s[1]))
        elif s[0] == 2:
            result += abs(man_dist - s[1])
        elif s[0] == 3:
            result += man_dist + M - s[1]
        else:
            result += N - man_dist + M -s[1]

elif man_di == 3:
    for s in shop_list:
        if s[0] == 1:
            result += man_dist + s[1]
        elif s[0] == 2:
            result += M - man_dist + s[1]
        elif s[0] == 3:
            result += abs(man_dist - s[1])
        else:
            result += N + min((man_dist + s[1]), (2*M - man_dist - s[1]))

else:
    for s in shop_list:
        if s[0] == 1:
            result += man_dist + N - s[1]
        elif s[0] == 2:
            result += M - man_dist + N - s[1]
        elif s[0] == 3:
            result += N + min((man_dist + s[1]), (2*M - man_dist - s[1]))
        else:
            result += abs(man_dist - s[1])

print(result)