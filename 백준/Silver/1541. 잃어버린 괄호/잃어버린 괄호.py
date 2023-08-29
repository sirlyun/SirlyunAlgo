'''
    +, -, 괄호 가지고 수식 생성 후 괄호를 모두 지움
    +, - 만 남은 수식에 괄호를 자유롭게 적절히 쳐서 결과를 최소화하고 싶음
'''

cal_str = input().split('-')

new_cal = []
for c in cal_str:
    chk = c.split('+')
    cal = 0
    for i in chk:
        cal += int(i)
    new_cal.append(cal)

result = new_cal[0]
for c in range(1, len(new_cal)):
    result -= new_cal[c]

print(result)