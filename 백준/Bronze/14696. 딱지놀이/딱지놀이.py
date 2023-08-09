'''
    매 라운드 가지고 있는 딱지 중 한개를 냄
    딱지는 별,동그라미,네모,세모 네가지 모양들이 조합되어 그려져있다.한개 이상의 모양이 표시 같은거 여러개도 가능
    두 딱지에 그려진 그림을 비교하여 승무패를 판단
    1. 별의 개수가 다르다면 별이 많은 쪽 승리
    2. 별의 개수가 같고 동그라미 개수가 다르면 동그라미 많은 쪽 승리
    3. 별, 동그라미의 개수가 각각 같고 네모가 다르면 네모 많은 쪽 승리
    4. 별, 동그라미, 네모의 개수가 각각 같고 세모만 다르면 세모 많은 쪽 승리
    5. 모두 개수가 같다면 무승부
    별은 4 동그라미는 3 네모는 2 세모는 1로 입력 받음
'''

N = int(input())
for n in range(N):
    A_pic = list(map(int, input().split()))
    B_pic = list(map(int, input().split()))

    A_dict = {}
    B_dict = {}
    for a in range(1, len(A_pic)):
        A_dict[str(A_pic[a])] = A_dict.get(str(A_pic[a]), 0) + 1
    for b in range(1, len(B_pic)):
        B_dict[str(B_pic[b])] = B_dict.get(str(B_pic[b]), 0) + 1

    A_result = [0]*4
    B_result = [0]*4
    for a in A_dict.keys():
        A_result[int(a)-1] = A_dict.get(a)
    for b in B_dict.keys():
        B_result[int(b)-1] = B_dict.get(b)

    for i in range(3, -1, -1):
        if i == 0:
            print('D')
        if A_result[i] > B_result[i]:
            print('A')
            break
        elif A_result[i] < B_result[i]:
            print('B')
            break