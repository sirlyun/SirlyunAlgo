S = list(input().rstrip())
T = list(input().rstrip())

switch = False
while T:
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()
    if S == T:
        switch = True
        break

if switch:
    print(1)
else:
    print(0)