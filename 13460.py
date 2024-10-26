from copy import deepcopy
from collections import deque

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def incline():
    q = deque()
    q.append((arr, 0, -1))
    
    while q:
        board, cnt, d = q.popleft()
        # 10회 이상은 안되므로
        if cnt == 10:
            print(-1)
            return
        
        for i in range(4):
            if d == i:
                continue
            newBoard = deepcopy(board)
            # 오른쪽과 위로 기울였을 때
            if i == 0 or i == 3:
                canMove = False
                rsucess = False
                bsucess = False
                for r in range(N):
                    for c in range(M - 1, -1, -1):
                        nr, nc = r, c
                        if newBoard[nr][nc] == 'R' or newBoard[nr][nc] == 'B':
                            color = newBoard[nr][nc]
                            # 갈 수 있을때까지
                            newBoard[nr][nc] = '.'
                            while newBoard[nr][nc] == '.':
                                nr += dir[i][0]
                                nc += dir[i][1]
                                # 다른 색깔에 부딪히면 다시 뒤로
                                if newBoard[nr][nc] == 'R' or newBoard[nr][nc] == 'B':
                                    newBoard[nr - dir[i][0]][nc - dir[i][1]] = color
                                    canMove = True
                                    break
                                # 벽에 부딪히면 다시 뒤로
                                elif newBoard[nr][nc] == '#':
                                    newBoard[nr - dir[i][0]][nc - dir[i][1]] = color
                                    canMove = True
                                    break
                                # 골이면
                                elif newBoard[nr][nc] == 'O':
                                    if color == 'R':
                                        rsucess = True
                                    else:
                                        bsucess = True
                                    break
                if rsucess == True and bsucess == False:
                    print(cnt + 1)
                    return
                if canMove == True and bsucess == False:
                    q.append((newBoard, cnt + 1, i))
                            
            # 왼쪽과 아래로 기울였을 때
            elif i == 1 or i == 2:
                canMove = False
                rsucess = False
                bsucess = False
                for r in range(N - 1, -1, -1):
                    for c in range(M):
                        nr, nc = r, c
                        if newBoard[nr][nc] == 'R' or newBoard[nr][nc] == 'B':
                            color = newBoard[nr][nc]
                            # 갈 수 있을때까지
                            newBoard[nr][nc] = '.'
                            while newBoard[nr][nc] == '.':
                                nr += dir[i][0]
                                nc += dir[i][1]
                                # 다른 색깔에 부딪히면 다시 뒤로
                                if newBoard[nr][nc] == 'R' or newBoard[nr][nc] == 'B':
                                    newBoard[nr - dir[i][0]][nc - dir[i][1]] = color
                                    canMove = True
                                    break
                                # 벽에 부딪히면 다시 뒤로
                                elif newBoard[nr][nc] == '#':
                                    newBoard[nr - dir[i][0]][nc - dir[i][1]] = color
                                    canMove = True
                                    break
                                # 골이면
                                elif newBoard[nr][nc] == 'O':
                                    if color == 'R':
                                        rsucess = True
                                    else:
                                        bsucess = True
                                    break
                if rsucess == True and bsucess == False:
                    print(cnt + 1)
                    return
                if canMove == True and bsucess == False:
                    q.append((newBoard, cnt + 1, i))
                    
    print(-1)
                            

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
        
incline()