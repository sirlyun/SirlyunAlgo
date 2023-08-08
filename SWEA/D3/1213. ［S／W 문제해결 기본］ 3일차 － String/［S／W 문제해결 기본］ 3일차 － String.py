for _ in range(10):
    t = int(input())
    chk = input()
    sent = input()

    result = 0
    # for i in range(len(sent)-len(chk)):
    #     j = 0
    #     while j < len(chk):
    #         if sent[i] != chk[j]:
    #             break
    #         j += 1
    #         i += 1
    #     else:
    #         result += 1
    # print(f'#{t} {result}')
    for i in range(len(sent)):
        if sent[i] == chk[0]:
            if sent[i:i+len(chk)] == chk:
                result += 1
    print(f'#{t} {result}')