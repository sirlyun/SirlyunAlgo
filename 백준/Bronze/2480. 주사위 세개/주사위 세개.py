a, b, c = map(int, input().split())

if a == b == c:
    score = 10000 + a*1000
elif a == b and b != c:
    score = 1000 + b*100
elif a == c and b != c:
    score = 1000 + a*100
elif b == c and b != a:
    score = 1000 + b*100
elif a != b and a != c and b != c:
    score = 100*max(a, b, c)

print(score)