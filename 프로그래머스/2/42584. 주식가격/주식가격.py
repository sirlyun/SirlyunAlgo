'''
    초 단위로 기록된 prices
    가격이 떨어지지 않은 기간은 몇 초인가
'''

from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        price = queue.popleft()
        cnt = 0
        for now_price in queue:
            cnt += 1
            if price > now_price:
                break 
                
        answer.append(cnt)
        
    return answer