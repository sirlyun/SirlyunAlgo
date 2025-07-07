'''
    택배 상자는 크기가 모두 같다
    1번부터 n번까지 순서대로 전달
    벨트에 놓인 순서대로 상자를 내릴 수 있음
    택비 기사가 알려준 순서에 맞게 실어야 함
    
    맨 앞에 놓인 상자가 순서가 아니라면 보조 벨트에 놓음
    보조 벨트는 마지막에 보관한 상자부터 꺼내짐
'''

def solution(order):
    answer = 0
    stack = []
    order_len = len(order)
    num = 0
    
    while answer < order_len:
        if order[answer] > num:
            num += 1
            stack.append(num)
        elif order[answer] == stack[-1]:
            stack.pop()
            answer += 1
        else:
            break
    
    return answer