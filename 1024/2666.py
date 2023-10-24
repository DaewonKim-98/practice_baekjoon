N = int(input())
a, b = map(int, input().split())
# 벽장 0은 닫혀 있고 1은 열려 있음
arr = [0] * N
arr[a - 1] = 1
arr[b - 1] = 1

# 들어오는 벽장 순서에서 가장 가까이 열려 있는 벽장을 옮기는데
# 가까이 열려 있는 벽장까지의 거리가 같다면 다음 순서에 올 벽장에서 더 먼 것을 옮기는게 최소로 할듯
sequence = []
M = int(input())
for _ in range(M):
    sequence.append(int(input()) - 1)

min_cnt = 400
cnt = 0
# 아오 근데 수가 작아서 그냥 재귀로 모두 다 탐색해서 해도 될 것 같은데 다시 재귀로 해보자 망할거
i = 0
def dfs(i, cnt):
    global min_cnt
    if i == M:
        if min_cnt > cnt:
            min_cnt = cnt
        return
    if arr[sequence[i]] == 1:
        dfs(i + 1, cnt)
    else:
        j = 1
        while sequence[i] - j >= 0:
            if arr[sequence[i] - j] == 1:
                arr[sequence[i] - j] = 0
                arr[sequence[i]] = 1
                dfs(i + 1, cnt + j)
                arr[sequence[i] - j] = 1
                arr[sequence[i]] = 0
                break
            else:
                j += 1
        k = 1
        while sequence[i] + k < N:
            if arr[sequence[i] + k] == 1:
                arr[sequence[i] + k] = 0
                arr[sequence[i]] = 1
                dfs(i + 1, cnt + k)
                arr[sequence[i] + k] = 1
                arr[sequence[i]] = 0
                break
            else:
                k += 1
dfs(i, cnt)
print(min_cnt)