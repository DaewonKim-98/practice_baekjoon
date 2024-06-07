def dfs(i, power, happy):
    global maxHappy
    if power <= 0:
        return
    maxHappy = max(happy, maxHappy)
    for j in range(i + 1, N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(j, power - lose[j], happy + get[j])
            visited[j] = 0
        

N = int(input())
lose = list(map(int, input().split()))
get = list(map(int, input().split()))

# dfs를 통해
maxHappy = 0
for i in range(N):
    visited = [0] * N
    visited[i] = 1
    dfs(i, 100 - lose[i], get[i])
    
print(maxHappy)