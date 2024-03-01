N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dir = {
    'E': [0, 1],
    'W': [0, -1],
    'S': [1, 0],
    'N': [-1, 0],
}

domino = [['S'] * M for _ in range(N)]
score = 0
# 명령에 따라 도미노 무너뜨리고 세우기
for _ in range(R):
    # 공격
    x, y, d = map(str, input().split())
    x, y = int(x) - 1, int(y) - 1
    if domino[x][y] == 'S':
        domino[x][y] = 'F'
        # 길이만큼 도미노 쓰러뜨리기
        length = arr[x][y] - 1
        score += 1
        while True:
            x, y = x + dir[d][0], y + dir[d][1]
            # print(x, y, length)
            # 범위를 벗어나면 끝이고 도미노의 길이만큼 쓰러뜨리면 끝이므로
            if 0 <= x < N and 0 <= y < M and length > 0:
                length -= 1
                # 넘어져있는거면 길이만 줄이고 다시 continue
                if domino[x][y] == 'F':
                    continue
                # 도미노의 길이 갱신
                length = max(length, arr[x][y] - 1)
                # 넘어뜨리고 점수 +1
                domino[x][y] = 'F'
                score += 1
            else:
                break
        
    # 수비
    x, y = map(int, input().split())
    # print(x, y)
    # print(domino)
    domino[x - 1][y - 1] = 'S'
    
print(score)
for i in range(N):
    print(' '.join(domino[i]))