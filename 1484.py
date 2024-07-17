G = int(input())

# 이분탐색일듯
# 현재 몸무게
canPrint = False
for i in range(1, 100001):
    start = 1
    end = 100000
    while start <= end:
        middle = (start + end) // 2
        if i ** 2 - middle ** 2 < G:
            end = middle - 1
        elif i ** 2 - middle ** 2 > G:
            start = middle + 1
        else:
            print(i)
            canPrint = True
            break
if canPrint == False:
    print(-1)