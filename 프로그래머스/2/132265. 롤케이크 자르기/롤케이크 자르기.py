'''
    각 조각에 동일한 가짓수의 토핑이 올라가면 정상으로 판단
    어쩔 수 없는 비정상의 경우도 존재
    
    정상으로 구성할 수 있는 방법의 수를 출력
'''

def solution(topping):
    answer = 0
    
    left_set = set()
    right_set = set()
    left_dict = {}
    right_dict = {}
    topping_len = len(topping)
    
    for idx, top in enumerate(topping):
        left_set.add(top)
        left_dict[idx] = len(left_set)
        
    for idx, top in enumerate(topping[::-1]):
        right_set.add(top)
        right_dict[topping_len-1-idx] = len(right_set)
        
    for i in range(topping_len):
        if left_dict[i] == right_dict.get(i+1):
            answer += 1
    
    return answer