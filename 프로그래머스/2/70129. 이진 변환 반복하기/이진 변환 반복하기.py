def num_maker(n):
    result = ''

    while n > 0:
        n, mod = divmod(n, 2)
        result += str(mod)

    return result[::-1] 

def transform(s):
    x = s
    result_1 = 0
    result_2 =0
    
    while x != '1':
        cnt = 0
        for i in x:
            if i == '1':
                cnt += 1
            else:
                result_2 += 1
        
        x = num_maker(cnt)
        result_1 += 1
        
    return [result_1, result_2]
        
def solution(s):
    """
    x의 모든 0을 제거합니다.
    x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
    
    :param s: 0과 1로 이루어진 문자열
    :return: s가 1이 될 때까지 이진 변환을 했을 때, [변환 횟수, 제거된 0의 개수]
    """
    
    return transform(s)