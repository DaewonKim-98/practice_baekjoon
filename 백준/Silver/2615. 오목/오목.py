arr = [list(map(int ,input().split())) for _ in range(19)]

# 델타 탐색 방향은 오른쪽 아래로만 + 대각선 위로
dir = [[0, 1], [1, 0], [1, 1], [-1, 1]]

# 오목이 이기는 것만큼 델타탐색
def delta(r, c):
    for d in dir:
        # 각 방향에 따라 cnt를 세어 주어야 하므로
        cnt = 0
        for i in range(1, 5):
            nr, nc = r + d[0] * i, c + d[1] * i
            if 0 <= nr < 19 and 0 <= nc < 19:
                # 자신 이후에 자신과 똑같은 것들이 있으면 cnt
                if arr[r][c] != 0 and arr[r][c] == arr[nr][nc]:
                    cnt += 1                
                else:
                    break
        if cnt == 4:
            if 0 <= r - d[0] < 19 and 0 <= c - d[1] < 19:
                # 자신 이전에도 자신과 똑같은 것이 있으면 다시반복
                if arr[r][c] != 0 and arr[r][c] == arr[r - d[0]][c - d[1]]:
                    continue

            if 0 <= r + d[0] * 5 < 19 and 0 <= c + d[1] * 5 < 19:
                # 오목 이후에도 하나 더 자신과 똑같은 것이 있으면 다시반복
                if arr[r][c] != 0 and arr[r][c] == arr[r + d[0] * 5][c + d[1] * 5]:
                    continue

            
            rock_list.append([arr[r][c], r + 1, c + 1])
            

# 6알 이상 연속적으로 있을 수 있으므로 리스트를 만들어 판단
rock_list = []
for r in range(19):
    for c in range(19):
        delta(r, c)
        
if len(rock_list) == 1:
    print(rock_list[0][0])
    print(*rock_list[0][1:])
else:
    print(0)