def subset(pick, k):
    if pick == k:
        if bit.count(1) == 6:
            for i in range(k):
                if bit[i] == 1:
                    print(cs[i + 1], end=' ')
            print()
    else:
        bit[pick] = 1
        subset(pick + 1, k)
        bit[pick] = 0
        subset(pick + 1, k)


while True:
    cs = list(map(str, input().split()))
    if cs[0] == '0':
        break
    else:
        k = int(cs[0])
        # 부분집합을 만들 bit
        bit = [0] * k
        pick = 0
        subset(pick, k)
        print()