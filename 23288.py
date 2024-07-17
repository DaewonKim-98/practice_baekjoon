from copy import deepcopy
from collections import deque

# 주사위 회전
def rotate(dir):
    global direction
    if dir == 'right':
        direction += 1
        direction %= 4
    elif dir == 'left':
        direction += 3
        direction %= 4
    else:
        direction += 2
        direction %= 4
        
# 주사위 굴리기
def tumble(direction):
    oldDice = deepcopy(dice)
    if direction == 0:
        dice[1][0] = oldDice[3]
        dice[1][1] = oldDice[1][0]
        dice[1][2] = oldDice[1][1]
        dice[3] = oldDice[1][2]
    elif direction == 1:
        dice[1][1] = oldDice[0]
        dice[2] = oldDice[1][1]
        dice[3] = oldDice[2]
        dice[0] = oldDice[3]
    elif direction == 2:
        dice[1][2] = oldDice[3]
        dice[1][1] = oldDice[1][2]
        dice[1][0] = oldDice[1][1]
        dice[3] = oldDice[1][0]
    else:
        dice[1][1] = oldDice[2]
        dice[0] = oldDice[1][1]
        dice[3] = oldDice[0]
        dice[2] = oldDice[3]
        
# 점수 획득
def getPoint(x, y):
    q = deque()
    visited = [[0] * M for _ in range(N)]
    q.append((x, y))
    num = arr[x][y]
    visited[x][y] = 1
    cnt = 1
    
    while q:
        x, y = q.popleft()
        for d in dir:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == num and visited[nx][ny] == 0:
                cnt += 1
                visited[nx][ny] = 1
                q.append((nx, ny))
                
    return num * cnt
        
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 처음 주사위
dice = [2, [4, 1, 3], 5, 6]
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
direction = 0
x, y = 0, 0
point = 0

for _ in range(K):
    # 이동 방향에 칸이 있다면
    if 0 <= x + dir[direction][0] < N and 0 <= y + dir[direction][1] < M:
        x = x + dir[direction][0]
        y = y + dir[direction][1]
        # 점수 획득
        point += getPoint(x, y)
        # 굴리기
        tumble(direction)
        # 방향 결정
        if dice[3] > arr[x][y]:
            rotate('right')
        elif dice[3] < arr[x][y]:
            rotate('left')
    # 칸이 없다면 반대 방향으로
    else:
        x = x - dir[direction][0]
        y = y - dir[direction][1]
        rotate('opposite')
        # 점수 획득
        point += getPoint(x, y)
        # 굴리기
        tumble(direction)
        # 방향 결정
        if dice[3] > arr[x][y]:
            rotate('right')
        elif dice[3] < arr[x][y]:
            rotate('left')
            
print(point)