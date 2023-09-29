# 4칸의 범위
def frange(n, x, y):
    return [[(x, x + n // 2), (y, y + n // 2)], [(x, x + n // 2), (y + n // 2, y + n)],
            [(x + n // 2, x + n), (y, y + n // 2)], [(x + n // 2, x + n), (y + n // 2, y + n)]]
    
# 각 범위에서 돌렸을 때 모두 같은 수가 나오면 white와 blue에 추가
# 아니면 재귀로 n 자르기
def makesame(N, x, y):
    global white
    global blue
    # N이 1이되면 더 이상 잘라질 수 없으므로 끝
    if N == 1:
        if arr[x][y] == 0:
            white += 1
        else:
            blue += 1
        return
    for i in range(4):
        lst = frange(N, x, y)[i]
        # 돌릴 때 칸들의 합이 (N // 2) ** 2이면 모두 파랑, 0이면 모두 흰색이므로
        sum_square = 0
        for r in range(lst[0][0], lst[0][1]):
            for c in range(lst[1][0], lst[1][1]):
                sum_square += arr[r][c]
                
        if sum_square == (N // 2) ** 2:
            blue += 1
        elif sum_square == 0:
            white += 1
        # 둘 다 아니면 재귀
        else:
            if i == 0:
                makesame(N // 2, x, y)
            elif i == 1:
                makesame(N // 2, x, y + N // 2)
            elif i == 2:
                makesame(N // 2, x + N // 2, y)
            else:
                makesame(N // 2, x + N // 2, y + N // 2)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0
x = 0
y = 0

# 처음에 모두 흰색 또는 파란색일 때
s = 0
for r in range(N):
    for c in range(N):
        s += arr[r][c]
if s == N ** 2:
    print(0)
    print(1)
elif s == 0:
    print(1)
    print(0)
else:
    makesame(N, x, y)
    print(white)
    print(blue)