t = int(input()) # 테스트 케이스의 수

for i in range(t):
    n = int(input())

    num_list = list(map(int, input().split()))
    result = 0

    while(len(num_list) > 1):
        max_num = max(num_list)
        for j in range(num_list.index(max_num)):
            result += max_num - num_list[j]
        del num_list[:num_list.index(max_num)+1]


    print(f'#{i+1} {result}')