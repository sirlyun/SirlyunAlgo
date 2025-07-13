def solution(s):
    """
    :param s: 공백으로 구분된 숫자로 구성된 문자열
    :return: 최소값과 최대값을 찾아 '최소값 최대값' 형태로 반환
    """
    
    num_list = s.split(' ')
    num_list.sort(key=lambda x: int(x))
    
    return f'{num_list[0]} {num_list[-1]}'