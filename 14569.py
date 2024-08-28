import sys
input = sys.stdin.readline

N = int(input().strip())
lectures = [list(map(int, input().strip().split())) for _ in range(N)]
M = int(input().strip())

for _ in range(M):
    empty = list(map(int, input().strip().split()))
    time = empty.pop(0)
    cnt = 0
    # 각 강의를 돌면서 모든 time에 가능하다면 추가
    for lecture in lectures:
        canTakeClass = True
        for i in range(1, lecture[0] + 1):
            if lecture[i] not in empty:
                canTakeClass = False
                break
        if canTakeClass == True:
            cnt += 1
    print(cnt)