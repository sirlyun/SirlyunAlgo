'''
    2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다. > 골드바흐의 수
    짝수를 두 소수의 합으로 나타내는 표현 > 골드바흐 파티션
    만약 골드바흐 파티션이 여러가지인 경우 두 소수의 차이가 가장 작은 것을 출력
'''

def check(num):
    if num == 1:
        return False

    for n in range(2, int(num**(0.5))+1):
        if num % n == 0:
            return False
    return True

for _ in range(int(input())):
    num = int(input())

    a, b = num//2, num//2
    while a > 0:
        if check(a) and check(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1