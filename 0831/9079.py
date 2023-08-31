import sys
input = sys.stdin.readline
T = int(input().strip())

# 뒤집는 모든 경우의 수를 구한 다음 조합을 이용해서 찾으면 되지 않을까
def r1(lst):
    for c in range(3):
        if lst[0][c] == 'H':
            lst[0][c] = 'T'
        else:
            lst[0][c] = 'H'
def r2(lst):
    for c in range(3):
        if lst[1][c] == 'H':
            lst[1][c] = 'T'
        else:
            lst[1][c] = 'H'
def r3(lst):
    for c in range(3):
        if lst[2][c] == 'H':
            lst[2][c] = 'T'
        else:
            lst[2][c] = 'H'
def c1(lst):
    for r in range(3):
        if lst[r][0] == 'H':
            lst[r][0] = 'T'
        else:
            lst[r][0] = 'H'
def c2(lst):
    for r in range(3):
        if lst[r][1] == 'H':
            lst[r][1] = 'T'
        else:
            lst[r][1] = 'H'
def c3(lst):
    for r in range(3):
        if lst[r][2] == 'H':
            lst[r][2] = 'T'
        else:
            lst[r][2] = 'H'
def d1(lst):
    for c in range(3):
        if lst[c][c] == 'H':
            lst[c][c] = 'T'
        else:
            lst[c][c] = 'H'
def d2(lst):
    for c in range(3):
        if lst[2 - c][c] == 'H':
            lst[2 - c][c] = 'T'
        else:
            lst[2 - c][c] = 'H'

for case in range(1, T + 1):
    arr = [list(map(str, input().split())) for _ in range(3)]
    f_list = [r1, r2, r3, c1, c2, c3, d1, d2]
    
    result = -1

    # 처음부터 모두 같은 면이면
    h_cnt = 0
    for r in range(3):
            for c in range(3):
                if arr[r][c] == 'H':
                    h_cnt += 1  
    # 한번만에 된다면 0 출력
    if h_cnt == 9 or h_cnt == 0:
        result = 0


    # 최소 연산 횟수 1회
    for i in f_list:
        h_cnt = 0
        i(arr)
        for r in range(3):
            for c in range(3):
                if arr[r][c] == 'H':
                    h_cnt += 1  
        # 한번만에 된다면 1을 출력하고 그만
        if h_cnt == 9 or h_cnt == 0 and result == -1:
            result = 1
        # 아니면 다시 원상복귀
        else:
            i(arr)

    # 최소 연산 횟수 2회
    for i in f_list:
        for j in f_list:
            h_cnt = 0
            if i != j:
                i(arr)
                j(arr)
                for r in range(3):
                    for c in range(3):
                        if arr[r][c] == 'H':
                            h_cnt += 1
                # 한번만에 된다면 2를 출력하고 그만
                if (h_cnt == 9 or h_cnt == 0) and result == -1:
                    result = 2
                # 아니면 다시 원상복귀
                else:
                    i(arr)
                    j(arr)
    
    # 최소 연산 횟수 3회
    for i in f_list:
        for j in f_list:
            for k in f_list:
                h_cnt = 0
                if i != j != k:
                    i(arr)
                    j(arr)
                    k(arr)
                    for r in range(3):
                        for c in range(3):
                            if arr[r][c] == 'H':
                                h_cnt += 1
                    # 한번만에 된다면 3을 출력하고 그만
                    if (h_cnt == 9 or h_cnt == 0) and result == -1:
                        result = 3
                    # 아니면 다시 원상복귀
                    else:
                        i(arr)
                        j(arr)
                        k(arr)

    # 최소 연산 횟수 4회
    for i in f_list:
        for j in f_list:
            for k in f_list:
                for l in f_list:
                    h_cnt = 0
                    if i != j != k != l:
                        i(arr)
                        j(arr)
                        k(arr)
                        l(arr)
                        for r in range(3):
                            for c in range(3):
                                if arr[r][c] == 'H':
                                    h_cnt += 1
                        # 한번만에 된다면 4을 출력하고 그만
                        if (h_cnt == 9 or h_cnt == 0) and result == -1:
                            result = 4
                        # 아니면 다시 원상복귀
                        else:
                            i(arr)
                            j(arr)
                            k(arr)
                            l(arr)

  
    print(result)