N = int(input())
get_num = list(map(int, input().split()))
stu = []
for num, order in enumerate(get_num, 1):
    stu.insert((num-1) - order, num)

print(*stu)