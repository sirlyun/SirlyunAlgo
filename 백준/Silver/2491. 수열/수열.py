'''
    0~9 숫자로 이루어진 길이 N짜리 수열
    그 수열 속 연속해서 커지거나, 연속해서 작아지는 수열 중
    길이가 가장 긴 것을 찾아 길이 출력
    숫자가 같은 건 노상관
'''

N = int(input())
num_list = list(map(int, input().split()))
dp1 = [1]*N
dp2 = [1]*N

for i in range(N-1):
    if num_list[i+1] >= num_list[i]:
        dp1[i+1] += dp1[i]

for i in range(N-1):
    if num_list[i+1] <= num_list[i]:
        dp2[i+1] += dp2[i]

print(max(max(dp1), max(dp2)))