a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_score = 0
b_score = 0
draw = 0
for i in range(10):
    if a_list[i] > b_list[i]:
        a_score += 1
    elif a_list[i] < b_list[i]:
        b_score += 1
    
if a_score > b_score:
    print('A')
elif a_score < b_score:
    print('B')
else:
    print('D')