'''
    한 번호가 다른 번호의 접두어인 경우 확인
'''

def solution(phone_book):
    """
    :params phone_book: 전화번호 배열
    :return: 한 번호가 다른 번호의 접두어인 경우가 존재하면 False 반환
    """
    
    phone_book.sort()
    N = len(phone_book)
    
    for i in range(1, N):
        if phone_book[i-1] == phone_book[i][:len(phone_book[i-1])]:
            return False
    
    return True
    
    return True