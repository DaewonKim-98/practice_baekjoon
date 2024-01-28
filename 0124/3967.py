numbers = [('A', 1),
           ('B', 2),
           ('C', 3),
           ('D', 4),
           ('E', 5),
           ('F', 6),
           ('G', 7),
           ('H', 8),
           ('I', 9),
           ('J', 10),
           ('K', 11),
           ('L', 12),
           ]

# 각 줄 왼쪽은 좌표 찍은 개수, 오른쪽은 합
line = {
    ((0, 4), (1, 3), (2, 2), (3, 1)): [0, 0],
    ((0, 4), (1, 5), (2, 6), (3, 7)): [0, 0],
    ((1, 1), (1, 3), (1, 5), (1, 7)): [0, 0],
    ((1, 1), (2, 2), (3, 3), (4, 4)): [0, 0],
    ((1, 7), (2, 6), (3, 5), (4, 4)): [0, 0],
    ((3, 1), (3, 3), (3, 5), (3, 7)): [0, 0],
}

arr = [list(input()) for _ in range(5)]
visited = set()

def dfs(i):
    # i가 최종에 도착했을 때
    if i == len(lst):
        for r in range(5):
            for c in range(9):
                print(arr[r][c], end='')
            print()
        exit()

    for j in numbers:
        # print(i, j, visited, line)
        # 방문하지 않았으면 줄에 대해서 확인
        if j[0] not in visited:
            goOn = True
            v = []
            for k in line:
                # i에 대한 좌표가 줄에 있으면
                if (lst[i][0], lst[i][1]) in k:
                    v.append(k)
                    # 줄 갱신
                    line[k][0] += 1
                    line[k][1] += j[1]
                    if line[k][1] > 26:
                            line[k][0] -= 1
                            line[k][1] -= j[1]
                            if len(v) == 2:
                                line[v[0]][0] -= 1
                                line[v[0]][1] -= j[1]
                            goOn = False
                            break
                    
                    # 줄이 4개가 다 채워졌으면
                    if line[k][0] == 4:
                        # 합이 26이 안된다면 끝
                        if line[k][1] < 26:
                            line[k][0] -= 1
                            line[k][1] -= j[1]
                            if len(v) == 2:
                                line[v[0]][0] -= 1
                                line[v[0]][1] -= j[1]
                            goOn = False
                            break
            if goOn == True:
                visited.add(j[0])
                arr[lst[i][0]][lst[i][1]] = j[0]
                dfs(i + 1)
                visited.remove(j[0])
                arr[lst[i][0]][lst[i][1]] = 'x'
                for k in line:
                    # i에 대한 좌표가 줄에 있으면
                    if (lst[i][0], lst[i][1]) in k:
                        line[k][0] -= 1
                        line[k][1] -= j[1]
                        
                            

# 각 방향을 모두 더해서 26이 되는 것들을 찾는 dfs
lst = []
for r in range(5):
    for c in range(9):
        # 채워지지 않은 곳만 넣기
        if arr[r][c] == 'x':
            lst.append((r, c))
        # 채워진 곳이면
        elif arr[r][c] != '.':
            for k in line:
                if (r, c) in k:
                    for n in numbers:
                        if arr[r][c] == n[0]:
                            visited.add(n[0])
                            line[k][0] += 1
                            line[k][1] += n[1]
                            break
                            
# print(lst)
# print(line)
# print(visited)     
i = 0
dfs(i)