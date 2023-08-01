for _ in range(3):
    num_list = list(map(int, input().split()))
    chk = 0
    for num in num_list:
        if num == 0:
            chk += 1
    if chk == 1:
        print('A')
    elif chk == 2:
        print('B')
    elif chk == 3:
        print('C')
    elif chk == 4:
        print('D')
    else:
        print('E')