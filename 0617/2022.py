from math import sqrt

def getC(w):
    return sqrt(x ** 2 - w ** 2) * sqrt(y ** 2 - w ** 2) / (sqrt(x ** 2 - w ** 2) + sqrt(y ** 2 - w ** 2))

x, y, c = map(float, input().split())

# a + b가 밑면일 때 a : c = w: 루트(y ** 2 - w ** 2)
# b : c = w: 루트(x ** 2 - w ** 2)
# a + b = w

# cw = a루트(y ** 2 - w ** 2)
# cw = b루트(x ** 2 - w ** 2)
# a + b = cw(1/루트(y ** 2 - w ** 2) + 1/루트(x ** 2 - w ** 2))
# c = 루트(x ** 2 - w ** 2) * 루트(y ** 2 - w ** 2) / (루트(x ** 2 - w ** 2) + 루트(y ** 2 - w ** 2))

# 이분탐색으로 w 찾기
start = 0
end = min(x, y)

result = 0
while start + 0.000001 < end:
    mid = (start + end) / 2
    # print(mid)
    if getC(mid) >= c:
        result = mid
        start = mid
    else:
        end = mid
        
print(result)