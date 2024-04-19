'''
    불량 사용자 목록을 만들어 당첨 처리 시 제외
    아이디의 일부 문자를 *로 가려서 전달
    * 하나 당 문자 하나
    불량 사용자 목록에 매핑된 아이디를 제재 아이디로 부름
    제재 아이디 목록이 가능한 경우의 수를 반환
'''

from itertools import permutations
 
 
def match(user, banned_id):
    for i in range(len(user)):
        if len(user[i]) == len(banned_id[i]):
            for j in range(len(user[i])):
                if user[i][j] != banned_id[i][j]:
                    if banned_id[i][j] == '*':
                        continue
                    else:
                        return False
        else:
            return False
    return True
 
 
def solution(user_id, banned_id):
    answer = []
 
    for banned_user in permutations(user_id, len(banned_id)):
        if match(banned_user, banned_id):
            banned_user = set(banned_user)
            
            if banned_user not in answer:
                answer.append(banned_user)
                
    return len(answer)
