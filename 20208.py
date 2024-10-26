dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def drinkMilk(r, c, milk, health):
    global maxMilk
    
    homeDistance = abs(r - home[0]) + abs(c - home[1])
    if homeDistance <= health:
        maxMilk = max(maxMilk, milk)
    
    # 우유를 돌면서 찾기
    for nr, nc in milks:
        # 갈 수 있는 거리면
        distance = abs(r - nr) + abs(c - nc)
        if distance <= health and milkVisited[nr][nc] == 0:
            milkVisited[nr][nc] = 1
            drinkMilk(nr, nc, milk + 1, health + H - distance)
            milkVisited[nr][nc] = 0
            

N, M, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

home = []
milks = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            home = [r, c]
        elif arr[r][c] == 2:
            milks.append((r, c))

# dfs
maxMilk = 0
milkVisited = [[0] * N for _ in range(N)]
drinkMilk(home[0], home[1], 0, M)
print(maxMilk)