'''
    스킬 순서에 없는 내용은 그냥 배울 수 있음
    순서에 있는거는 무조건 순서대로 배워야함
    
    CBD 기준
    BACDE -> X
    CBADF -> C B A(not in) D
'''

def solution(skill, skill_trees):
    answer = 0
    
    for trees in skill_trees:
        tmp_skill = skill
        cnt = 0
        for t in trees:
            if t not in tmp_skill:
                continue
                
            if tmp_skill[cnt] != t:
                break
            
            cnt += 1
        else:
             answer += 1
    
    return answer