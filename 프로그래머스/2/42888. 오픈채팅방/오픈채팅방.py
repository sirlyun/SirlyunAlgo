"""
    [닉네임]님이 들어왔습니다.
    [닉네임]님이 나갔습니다.
    
    닉변 방법
        채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다
        채팅방에서 닉변
        
    닉변 시에는 기존에 출력됐던 메시지들의 닉네임도 모두 강제 변경된다
    중복 닉네임 허용

    유저는 유저 아이디로 구분
    입장: Enter [유저 아이디] [닉네임]
    퇴장: Leave [유저 아이디]
    변경: Change [유저 아이디] [닉네임]
"""

def solution(record):
    answer = []
    order_answer = []
    user_dict = {}
    
    for idx, r in enumerate(record):
        tmp = r.split(' ')
        order = tmp[0]
        user_id = tmp[1]
        
        if order == 'Enter':
            user_dict[user_id] = tmp[2]
            order_answer.append([user_id, '님이 들어왔습니다.'])
        elif order == 'Leave':
            order_answer.append([user_id, '님이 나갔습니다.'])
        else:
            user_dict[user_id] = tmp[2]
            
    for o in order_answer:
        tmp = [user_dict[o[0]], o[1]]
        answer.append(''.join(tmp))
    
    return answer