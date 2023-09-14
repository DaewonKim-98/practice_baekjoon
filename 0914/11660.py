import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
# 인덱스에 맞추기 위해 0 배열 추가
arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

# 누적합은 자기 전 것들을 더한 것인데 중복해서 더하는 것들이 있으므로 빼주고 자신을 더한다.
lst = [[0] * (N + 1) for _ in range(N + 1)]
for r in range(1, N + 1):
    for c in range(1, N + 1):
        lst[r][c] = lst[r][c - 1] + lst[r - 1][c] - lst[r - 1][c - 1] + arr[r][c]

# 이후의 합은 마찬가지로 빼주고 중복해서 빼준 것을 더한다
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = lst[x2][y2] - lst[x2][y1 - 1] - lst[x1 - 1][y2] + lst[x1 - 1][y1 - 1]
    print(result)