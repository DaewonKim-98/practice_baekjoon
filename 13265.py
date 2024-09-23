import sys
from collections import deque
input = sys.stdin.readline

def canColoring(i):
    q = deque()
    q.append(i)
    colors[i] = 1
    
    while q:
        circle = q.popleft()
        for j in link[circle]:
            # 색칠하지 않았으면
            if colors[j] == 0:
                colors[j] = -colors[circle]
                q.append(j)
            # 색칠 되어 있으면
            else:
                # 색이 같은 색으로 되어 있으면 안되므로
                if colors[j] == colors[circle]:
                    return False
    return True
                    

T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().strip().split())
    link = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, input().strip().split())
        link[x].append(y)
        link[y].append(x)
    colors = [0] * (N + 1)
    # 1또는 -1로 색깔 칠하기, 색을 칠해야 하는데 다른 색으로 칠해져있으면 끝
    for i in range(1, N + 1):
        if link[i] and colors[i] == 0:
            if canColoring(i) == False:
                print('impossible')
                break
    else:
        print('possible')
    