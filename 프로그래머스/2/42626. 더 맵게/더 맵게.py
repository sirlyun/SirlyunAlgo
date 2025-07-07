'''
    모든 음식의 스코빌을 K 이상으로 만들기
    스코빌 가장 낮은 두 개를
        섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    모두 K 이상일 때까지 반복
'''

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + 2*second)
        answer += 1
        
        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break
    
    return answer