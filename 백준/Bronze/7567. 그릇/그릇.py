chk = input()

height = 10

for i in range(1, len(chk)):
    if chk[i] == chk[i-1]:
        height += 5
    else:
        height += 10

print(height)