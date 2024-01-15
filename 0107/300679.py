N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 방향
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 오름차순으로 행
hang = []
cnt = 0

for i in range(N):
    d = 0
    # 무한 반복 판단
    infinite = True
    star = (i, 0, dir[d])
    # 별이 있었던 자리와 방향을 세트에 저장
    been = set()
    while star not in been:
        # print(star)
        been.add(star)
        # 별 이동
        r = star[0] + dir[d][0] * arr[star[0]][star[1]]
        c = star[1] + dir[d][1] * arr[star[0]][star[1]]
        
        # 이동한 별이 범위를 벗어나면 무한 반복이 아니므로 바로 끝
        if (r < 0 or N <= r) or (c < 0 or M <= c):
            infinite = False
            break
        
        # 별 갱신
        d += 1
        if d == 4:
            d = 0
        star = (r, c, dir[d])
        
    # 무한하게 반복된다면
    if infinite == True:
        cnt += 1
        hang.append(i + 1)
        
if cnt == 0:
    print(cnt)

else:
    print(cnt)
    for i in hang:
        print(i, end=' ')