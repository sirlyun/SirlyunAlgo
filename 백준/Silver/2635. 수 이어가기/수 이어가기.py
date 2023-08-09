'''
    초기 숫자 N이 주어진다
    두 번째 수는 N보다 작은 아무 숫자로 설정
    숫자 생성기:
        앞앞 수에서 앞 수를 빼서 만든다
        음의 정수가 만들어지기 전까지 만들어서
        최대 만들 수 있게 만들고 최대 개수와 만든 수들을 출력한다
'''

N = int(input())
max_cnt = 0
result_list = []
result = 0
for n in range(1,N+1):
    chk_list = []
    cnt = 0
    pre = N
    now = n
    while pre - now >= 0:
        cnt += 1
        num = pre - now
        chk_list.append(num)
        pre = now
        now = num
    if max_cnt < cnt:
        result = n
        max_cnt = cnt
        result_list.clear()
        for chk in chk_list:
            result_list.append(chk)
print(max_cnt+2)
print(N, result, *result_list)
