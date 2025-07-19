from itertools import combinations

def solution(relation):
    """
    후보키
        유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
        최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. 즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.
    :param relation: 릴레이션을 나타내는 문자열 배열
    :return: 후보키의 최대 개수
    """
    answer = 0
    
    check_comb = []
    for i in range(1, len(relation[0]) + 1):
        check_comb.extend(combinations(range(len(relation[0])), i))
        
    result = []
    for comb in check_comb:
        check = set([tuple(rel[key] for key in comb) for rel in relation])
        set_comb = set(comb)
        
        if len(check) == len(relation):
            if not result:
                answer += 1
                result.append(set_comb)
                continue
            
            for r in result:
                if r.issubset(set_comb):
                    break
            else:
                print(set_comb)
                answer += 1
                result.append(set_comb)

    return answer