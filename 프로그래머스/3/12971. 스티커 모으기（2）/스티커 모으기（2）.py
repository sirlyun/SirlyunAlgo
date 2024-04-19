'''
    N개의 스티커가 원형으로 연결됨
    몇장의 스티커를 뜯어서 뜯어낸 스티커에 적힌 숫자의 합이 최대가 되도록
    단, 스티커 한장을 뜯으면 인접해 있는 스티커는 뜯기 불가
    원형이니까 첫번째와 마지막이 연결되어 있음
    
    스티커를 뜯어 얻을 수 있는 숫자의 합의 최댓값을 반환
'''

def solution(sticker):
    answer = 0
    N = len(sticker)
    
    if N == 1:
        return sticker[0]

    # 1번 선택하는 경우
    dp1 = [0] + sticker[:-1]
    for i in range(2, N):
        dp1[i] = max(dp1[i-1], dp1[i-2] + dp1[i])
    
    # 1번 선택 안하는 경우
    dp2 = [0] + sticker[1:]
    for i in range(2, N):
        dp2[i] = max(dp2[i-1], dp2[i-2] + dp2[i])
        
    answer = max(dp1[-1], dp2[-1])
    return answer