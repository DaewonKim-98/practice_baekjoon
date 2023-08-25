import sys
input = sys.stdin.readline

for i in range(4):    
    a, b, c, d, x, y, z, w = map(int, input().split())

    # 겹치는 부분이 직사각형일 때
    if (a <= x < c or a < z <= c or (x <= a and c <= z)) and ((y <= b and d <= w) or b <= y < d or b < w <= d):
        print('a')

    # 겹치는 부분이 선분일 때
    elif ((a <= x < c or a < z <= c or (x <= a and c <= z)) and (b == w or d == y)) or ((x == c or a == z) and ((y <= b and d <= w) or b <= y < d or b < w <= d)):
        print('b')

    # 겹치는 부분이 점일 때
    elif (a == z and b == w) or (a == z and d == y) or (c == x and b == w) or (c == x and d == y):
        print('c')
    
    # 모두 아니면
    else:
        print('d')