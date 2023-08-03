
# 행렬을 만들 arr을 만든다.
arr = []

for i in range(5):
    row = list(map(str, input()))

    # row의 길이를 잰다
    len_row = 0
    for j in row:
        len_row += 1

    # 만약 row의 길이가 15보다 작으면 row의 뒤에 .을 추가해준다.
    if len_row < 15:
        for k in range(0, 15 - len_row):
            row += ['.'] 
    
    # 배열에 row를 추가해서 2차원 배열을 만든다.
    arr += [row]

# 세로로 숫자를 읽어야 하므로 행 방향으로 읽고 .이 들어가있으면 넘어가고 아니면 값을 출력
for c in range(15):
    for r in range(5):
        if arr[r][c] == '.':
            pass
        else:
            print(arr[r][c], end='')

