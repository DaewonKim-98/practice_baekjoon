# 종이의 개수를 찾는 함수
def findnum(r, c, N):
    global minus
    global zero
    global plus
    num = arr[r][c]
    # 쭉 돌면서 찾았을 때 다른 것이 나오면 바로 break으로 탈출하고 아래로
    for x in range(r, r + N):
        for y in range(c, c + N):
            if arr[x][y] != num:
                num = 2
                break
            
    # 만약 다 돌았을 때 다른 것이 안나왔다면 num은 -1, 0, 1 중 하나일 것이므로
    if num == -1:
        minus += 1
        return
    elif num == 0:
        zero += 1
        return
    elif num == 1:
        plus += 1
        return
    # 만약 다른 것이 나와 num=2가 된다면 재귀로 나눠서 반복
    else:
        findnum(r, c, N // 3)
        findnum(r, c + N // 3, N // 3)
        findnum(r, c + (N * 2) // 3, N // 3)
        findnum(r + N // 3, c, N // 3)
        findnum(r + N // 3, c + N // 3, N // 3)
        findnum(r + N // 3, c + (N * 2) // 3, N // 3)
        findnum(r + (N * 2) // 3, c, N // 3)
        findnum(r + (N * 2) // 3, c + N // 3, N // 3)
        findnum(r + (N * 2) // 3, c + (N * 2) // 3, N // 3)
        

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


minus = 0
zero = 0
plus = 0
findnum(0, 0, N)

print(minus)
print(zero)
print(plus)