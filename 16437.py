import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def saveSheep(i):
    sheep = 0
    # 각 섬에 있는 양 더하기, 늑대면 빼기
    if i != 1:
        if islands[i][0] == 'W':
            sheep -= islands[i][1]
        else:
            sheep += islands[i][1]
            
    for island in link[i]:
        sheep += saveSheep(island)
    
    # 만약 양이 0보다 작으면 늑대만 있거나 늑대한테 다 잡아먹혔다는 것이므로 0
    if sheep <= 0:
        return 0
    else:
        return sheep

N = int(input().strip())
islands =[[] for _ in range(N + 1)]
link = [[] for _ in range(N + 1)]

for i in range(2, N + 1):
    t, a, p = map(str, input().strip().split())
    islands[i] = [t, int(a)]
    link[int(p)].append(i)
   
# 아 걍 dfs로 해야겠다 개빡치네
cnt = saveSheep(1)
print(cnt)