'''
    일렬로 놓아진 포도주 잔
    포도주 시식 규칙
        1. 잔을 선택하면 잔에 있는 포도주 모두 마셔야 하고, 마신 후 원래 위치에 잔을 돌려놓음
        2. 연속으로 놓여있는 3잔을 모두 마시는건 불가능
    최대한 많은 양의 포도주 먹자
'''

N = int(input())
drink = [0]*10000
for n in range(N):
    drink[n] = int(input())

dp = [0]*10000
dp[0] = drink[0]
dp[1] = drink[0] + drink[1]
dp[2] = max(drink[0]+drink[1], drink[0]+drink[2], drink[1]+drink[2])

for n in range(3, N):
    dp[n] = max(dp[n-1], dp[n-2]+drink[n], dp[n-3]+drink[n-1]+drink[n])

print(dp[N-1])