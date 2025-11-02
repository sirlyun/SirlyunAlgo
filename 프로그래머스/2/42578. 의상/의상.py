def solution(clothes):
    """
    매일 입는 의상이 최소 한 개라도 바뀌어야 함
    최소 한 개의 의상은 입음
    
    :params clothes: 의상들이 담긴 2차원 배열
    :return: 서로 다른 옷의 조합 수
    """
    answer = 1
    
    cloth_dict = {}
    for cloth in clothes:
        if cloth_dict.get(cloth[1]) is None:
            cloth_dict[cloth[1]] = 1
            continue
        
        cloth_dict[cloth[1]] += 1

    for v in cloth_dict.values():
        answer *= v + 1
    
    return answer - 1