N = int(input())
t = (N-1984)%60
result = "ABCDEFGHIJKL"[t%12] + str(t%10)
print(result)