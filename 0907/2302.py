import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

if N == M:
    print(1)
    exit()

arr = [-1] + [0] * (N + 2)
# 고정석 지정
for i in range(M):
    arr[int(input().strip())] = -1

lst =  [1] * (N + 3)

for i in range(2, N + 1):
    # 고정석이면 이전의 경우의 수
    if arr[i] == -1:
        lst[i] = lst[i - 1]
    # 그 다음 것은 고정석 이전의 경우의 수
    elif arr[i - 1] == -1:
        lst[i] = lst[i - 1]
    # 그 다음은 고정석 이전의 경우의 수 * 2
    elif arr[i - 2] == -1:
        lst[i] = lst[i - 1] * 2
    elif arr[i - 3] == -1:
        lst[i] = lst[i - 2] * 3
    # i번째는 자신 이전까지 한 것과 자신 전전까지 한 것 * 2를 더한 경우이므로
    else:
        lst[i] = lst[i - 1] + lst[i - 2]

print(lst[N])