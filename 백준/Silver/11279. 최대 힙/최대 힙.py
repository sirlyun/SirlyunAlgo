'''
    배열에 자연수 x를 넣는다
    배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거한다.
''' 

import heapq
import sys

numbers = int(sys.stdin.readline())
heap = []

#Max Heap
for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (-num, num))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)