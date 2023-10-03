# dfs로 집합 찾기
def dfs(i, s):
    if i == k:
        possible.add(s)
        return
    else:
        dfs(i + 1, s + arr[i])
        dfs(i + 1, s)
        dfs(i + 1, s - arr[i])

k = int(input())
arr = list(map(int, input().split()))

s = 0
S = sum(arr)
# 1부터 S 사이
weights = set(range(1, S + 1))
i = 0
l = 0
visited = [0] * k
# 가능한 물의 무게
possible = set()
dfs(i, s)
result = weights - possible
print(len(result))