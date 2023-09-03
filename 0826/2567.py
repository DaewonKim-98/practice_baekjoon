import sys
N = int(input().strip())

# 배열
arr = [[0] * 101 for _ in range(101)]

# 배열에 색종이를 넣는다.
for i in range(N):
    c, r = map(int, input().split())
    for j in range(10):
        for k in range(10):
            arr[r + j][c + k] = 1

result = 0
# 색종이의 둘레는 0부터 돌았을 때 처음으로 1이 나오면 왼쪽 면/윗 면,
# 그 순간부터 돌았을 때 0이 나오거나 벽이 나오면 오른쪽 면/아랫 면이므로
for r in range(101):
    c = 0
    # c가 101을 넘어가면 인덱스를 넘어가므로 종료
    while c < 100:
        if arr[r][c] == 0 and arr[r][c + 1] == 1:
            result += 1
        elif arr[r][c] == 1 and arr[r][c + 1] == 0:
            result += 1
        c += 1
        
for c in range(101):
    r = 0
    # c가 101을 넘어가면 인덱스를 넘어가므로 종료
    while r < 100:
        if arr[r][c] == 0 and arr[r + 1][c] == 1:
            result += 1
        elif arr[r][c] == 1 and arr[r + 1][c] == 0:
            result += 1
        r += 1
        
print(result)