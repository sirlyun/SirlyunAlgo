def solution(s):
    """
    JadenCase: 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열
    s (문자열)
        숫자는 단어의 첫 문자로만 나옵니다.
        숫자로만 이루어진 단어는 없습니다.
        공백문자가 연속해서 나올 수 있습니다.
    :param s: 알파벳, 숫자, 공백으로 이루어진 문자열
    :return: JadenCase로 바꾼 문자열
    """
    answer = ' '
    tmp_answer = s.split(' ')
    
    for i in range(len(tmp_answer)):
        tmp_answer[i] = tmp_answer[i].capitalize()
    
    return answer.join(tmp_answer)