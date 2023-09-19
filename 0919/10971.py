import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(i, r):
    # 0이 하나가 남으면 다 채워진 것이므로
    if visited.count(0) == 1:
        if arr[i][r] != 0:
            # 나머지 0이있는 곳에 다시 처음으로 돌아가는 arr[i][r] 추가
            visited[i] = arr[i][r]
            prices.append(sum(visited))
            return
        else:
            return

    # visited에 도시로 가기 위한 비용 추가
    for w in range(N):
        if arr[i][w] != 0 and visited[w] == 0:
            visited[i] = arr[i][w]
            dfs(w, r)
            visited[w] = 0


N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]


# 비용
prices = []
for r in range(N):
    visited = [0] * N
    dfs(r, r)

print(min(prices))
