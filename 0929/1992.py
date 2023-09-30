# 압축한 결과 출력 함수
def pressnum(r, c, N):
    num = arr[r][c]
    for x in range(r, r + N):
        for y in range(c, c + N):
            # 중간에 숫자가 달라지면 영역을 잘라야하므로
            if arr[x][y] != num:
                num = 2
                break
    # 만약 숫자가 달라지지 않았으면 그대로 출력 가능        
    if num == 0:
        print(0, end='')
        return
    elif num == 1:
        print(1, end='')
        return
    # 숫자가 달라졌으면 괄호를 만들어서 영역 표시
    else:
        print('(', end='')
        # 재귀
        pressnum(r, c, N // 2)
        pressnum(r, c + N // 2, N // 2)
        pressnum(r + N // 2, c, N // 2)
        pressnum(r + N // 2, c + N // 2, N // 2)
        print(')', end='')

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

pressnum(0, 0, N)