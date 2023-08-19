'''
    n개의 시험장
    감독관은 총감독, 부감독으로 구성
    총감독은 가능 응시자 수 B
    부감독은 가능 응시자 수 C
    시험장에 총감독은 1명 부감독은 여러명 가능
    감시 못하는 응시자 존재 X
    감독 수 최소화
'''

N = int(input())
stu_list = list(map(int, input().split()))
B, C = map(int, input().split())

total = 0

for stu in stu_list:
    stu -= B
    total += 1
    if stu > 0:
        if stu % C == 0:
            total += stu // C
        else:
            total += stu // C + 1

print(total)