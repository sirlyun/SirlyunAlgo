N = int(input())

ans = ''
for i in range(N//4):
    N = N % 4
    ans += 'long '

print(f'{ans}'+'int')