for _ in range(10):
    t = int(input())
    chk = input()
    sent = input()

    result = 0
    for i in range(len(sent)-len(chk)+1):
        j = 0
        while j < len(chk):
            if sent[i] != chk[j]:
                break
            j += 1
            i += 1
        else:
            result += 1
    print(f'#{t} {result}')