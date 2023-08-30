# 영어를 숫자로 바꾸는 딕셔너리
alpha = ['A', 'B', 'C', 'D', 'E', 'F']
idx = list(range(6))
dic = {}
for i in range(6):
    dic[alpha[i]] = idx[i]

# 체스판
arr = [[0] * 6 for _ in range(6)]
# 나이트가 움직이는 방향
dir = [[2, 1], [1, 2], [2, -1], [-1, 2], [-2, 1], [1, -2], [-1, -2], [-2, -1]]

# 나이트리스트
knight_list = [input() for _ in range(36)]


result = 'Valid'
# 돌렸을 때 나이트처럼 움직인 것이 아니면 invalid
for i in range(35):
    knight = knight_list[i]
    r, c = 6 - int(knight[1]), dic[knight[0]]
    arr[r][c] = 1
    next_knight_list = []
    for d in dir:
        nr, nc = r + d[0], c + d[1]
        next_knight_list.append([nr, nc])

    # 다음 나이트가 나이트의 방향으로 안움직이면
    next_knight = knight_list[i + 1]
    r2, c2 = 6 - int(next_knight[1]), dic[next_knight[0]]
    arr[r2][c2] = 1
    if [r2, c2] not in next_knight_list:
        result = 'Invalid'
        break

# 처음과 마지막 나이트는 서로 이동할 수 있어야 하므로
first = knight_list[0]
last = knight_list[-1]

rf, cf = 6 - int(first[1]), dic[first[0]]
arr[rf][cf] = 1
last_knight_list = []
for d in dir:
    nr, nc = rf + d[0], cf + d[1]
    last_knight_list.append([nr, nc])

# 다음 나이트가 나이트의 방향으로 안움직이면
r2, c2 = 6 - int(last[1]), dic[last[0]]
arr[r2][c2] = 1
if [r2, c2] not in last_knight_list:
    result = 'Invalid'


# 마지막에 0이 하나라도 있으면 안되므로
for r in range(6):
    for c in range(6):
        if arr[r][c] == 0:
            result = 'Invalid'
            break

print(result)