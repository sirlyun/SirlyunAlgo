def hannoi(num, start, end):
    if num == 1:
        print(start, end)
        return
    
    hannoi(num-1, start, 6-start-end)
    print(start, end)
    hannoi(num-1, 6-start-end, end)


N = int(input())
print(2**N-1)
hannoi(N, 1, 3)