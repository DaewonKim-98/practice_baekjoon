r1, c1, r2, c2 = map(int, input().split())

# 0 0 1
# -1 0 4
# 1 1 9
# -2 -1 16
# 2 2 25
# -3 -2 36

arr = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]

# r, c의 관계에 따라서 각 값들을 찾을 수 있을까 없을까 해보면 될까 안될까
# 일단 드가즈아!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 가장 긴 값을 찾아야지 나머지에 공백을 넣으니까 가장 긴 값 찾기
max_value = 0
for r in range(r1, r2 + 1):
    for c in range(c1, c2 + 1):
        if abs(r) < abs(c):
            if c < 0:
                arr[r - r1][c - c1] = (c * 2) ** 2 + 1 + r - c
            else:
                arr[r - r1][c - c1] = (c * 2 - 1) ** 2 + c - r

        elif abs(r) == abs(c):
            if r == c:
                if c < 0:
                    arr[r - r1][c - c1] = (c * 2) ** 2 + 1
                elif c == 0:
                    arr[r - r1][c - c1] = 1
                else:
                    arr[r - r1][c - c1] = (c * 2 + 1) ** 2
            else:
                if c < 0:
                    arr[r - r1][c - c1] = (c * 2 - 1) ** 2 + c * 2
                else:
                    arr[r - r1][c - c1] = (c * 2) ** 2 - (c * 2 - 1)
                
        else:
            if r < 0:
                arr[r - r1][c - c1] = (r * 2) ** 2 + r - c + 1
            else:
                arr[r - r1][c - c1] = (r * 2 + 1) ** 2 - r + c
        max_value = max(max_value, arr[r - r1][c - c1])

# print(arr)   
length = len(str(max_value))

for r in range(r2 - r1 + 1):
    for c in range(c2 - c1 + 1):
        arr[r][c] = str(arr[r][c])
        while len(arr[r][c]) < length:
            arr[r][c] = ' ' + arr[r][c]
        if c != c2 - c1:
            print(arr[r][c], end='')
            print(' ', end='')
        else:
            print(arr[r][c])