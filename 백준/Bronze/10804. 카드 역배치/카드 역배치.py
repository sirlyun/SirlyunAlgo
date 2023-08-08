num_list = [i for i in range(1, 21)]
for _ in range(10):
    a, b = map(int, input().split())
    chk = (b - a + 1) // 2

    for i in range(chk):
        num_list[a - 1 + i], num_list[b - 1 - i] = num_list[b - 1 - i], num_list[a - 1 + i]
        
print(*num_list)