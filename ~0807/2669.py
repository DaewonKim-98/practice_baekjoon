# 0으로 이루어진 배열을 만든다.
arr = []
for i in range(100):
    arr += [[0] * 100]

for j in range(4):
    # 받아온 좌표에서 직사각형에 해당하는 부분을 배열에서 1로 바꾼다.
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(y1, y2):
        for c in range(x1, x2):
            arr[r][c] = 1

# 직사각형이 차지하는 면적을 cnt로 둔다.
cnt = 0
for r in range(100):
    for c in range(100):
        # 직사각형에 해당하는 부분이 있으면 cnt 에 1을 추가
        if arr[r][c] == 1:
            cnt += 1

print(cnt)