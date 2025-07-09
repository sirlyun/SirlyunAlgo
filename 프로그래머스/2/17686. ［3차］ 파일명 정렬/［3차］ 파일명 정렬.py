"""
    HEAD, NUMBER, TAIL 세 부분으로 구성됨
        HEAD: 숫자가 아닌 문자로 이루어져있고 최소 한글자
        NUMBER: 한글자에서 최대 다섯 글자의 숫자로 이루어져있고, 진짜 숫자 의미가 아니여도 됨
        TAIL: 뭐든지 가능
        
    파일명을 세부분으로 나누고 정렬
        - HEAD 우선 기준으로 사전 순 정렬, 문자열 비교 시 대소문자 구분 X
        - 다음 NUMBER의 숫자 순으로 정렬, 앞단의 0은 무시한체로 정렬
        - 입력에 주어진 순서 유지
"""

import re

def solution(files):
    answer = [re.split(r"([0-9]+)", s) for s in files]
    
    tmp_answer = sorted(answer, key = lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(tmp) for tmp in tmp_answer]