import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

p, m = map(int, input().split())
# 방들을 미리 만들어두기
rooms = [[] for _ in range(p)]

# 방들에 유저들이 들어오면 넣는데 처음 애랑 레벨 차이가 나면 다른 방으로
# 방이 m만큼 꽉 차면 다른 방으로
for _ in range(p):
    player = list(map(str, input().split()))
    # 방들을 돌리면서 채워넣기
    for i in range(p):
        # 방에 유저가 있고 정원이 차지 않았다면
        if 0 < len(rooms[i]) < m:
            # 새로운 유저의 레벨이 방의 유저 레벨 10 안이면 입장
            if abs(int(player[0]) - int(rooms[i][0][0])) <= 10:
                rooms[i].append(player)
                break
            # 아니면 다시 반복 돌리기
            continue
        # 정원이 찼다면 다시 반복 돌리기
        elif len(rooms[i]) == m:
            continue
        # 방에 유저가 없다면 그냥 채우기
        else:
            rooms[i].append(player)
            break

            
# 방들을 다 채웠으므로 출력
for i in range(p):
    # 빈 방이 나오면 break
    if len(rooms[i]) == 0:
        break
    # 꽉 찼으면 Started!하고 출력
    elif len(rooms[i]) == m:
        print('Started!')
        # 사전순으로 앞서는 플레이어부터 출력
        rooms[i].sort(key=lambda x: x[1])
        for j in range(m):
            for k in range(2):
                print(rooms[i][j][k], end=' ')
            print()
    # 다 차지 않았으면 Waiting! 하고 출력
    else:
        print('Waiting!')
        # 사전순으로 앞서는 플레이어부터 출력
        rooms[i].sort(key=lambda x: x[1])
        for j in range(len(rooms[i])):
            for k in range(2):
                print(rooms[i][j][k], end=' ')
            print()
        