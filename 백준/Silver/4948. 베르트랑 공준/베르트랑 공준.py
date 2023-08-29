'''
    임의의 자연수 n에 대하여 n보다 크고 2n보다 작거나 같은 소수는 적어도 하나 존재 

'''

def check(num):
    if num == 1:
        return False
    for n in range(2, int(num**(0.5)+1)):
        if num % n == 0:
            return False
    return True

chk = []
for i in range(1, 123456*2+1):
    if check(i):
        chk.append(i)

while True:
    N = int(input())
    if N == 0:
        break
    cnt = 0
    for i in chk:
        if N < i <= 2*N:
            cnt += 1
    print(cnt)