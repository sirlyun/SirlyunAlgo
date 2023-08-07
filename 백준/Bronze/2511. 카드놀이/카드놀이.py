A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

a_score = 0
b_score = 0
result_list = []
for i in range(10):
    if A_list[i] > B_list[i]:
        a_score += 3
        result_list.append('A')
    elif A_list[i] < B_list[i]:
        b_score += 3
        result_list.append('B')
    else:
        a_score += 1
        b_score += 1
        result_list.append('D')

print(a_score, b_score)
if a_score > b_score:
    print('A')
elif a_score < b_score:
    print('B')
else:
    cnt = 0
    for result in result_list[::-1]:
        cnt += 1
        if result != 'D':
            print(result)
            break
    if cnt == 10:
        print('D')