N = int(input())
result_list = []
for _ in range(N):
    stu, apple = map(int, input().split())
    result_list.append(apple%stu)
    
print(sum(result_list))
