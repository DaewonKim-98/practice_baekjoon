N, M = map(int, input().split())
# 기차
train = [[0] * 20 for _ in range(N)]

# 명령에 따라 기차 상태 변경
for _ in range(M):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        train[arr[1] - 1][arr[2] - 1] = 1
    elif arr[0] == 2:
        train[arr[1] - 1][arr[2] - 1] = 0
    elif arr[0] == 3:
        for i in range(19, 0, -1):
            train[arr[1] - 1][i] = train[arr[1] - 1][i - 1]
        train[arr[1] - 1][0] = 0
    else:
        for i in range(19):
            train[arr[1] - 1][i] = train[arr[1] - 1][i + 1]
        train[arr[1] - 1][19] = 0
        
# 기차 상태 set에 저장 후 있으면 넘기기
cnt = 0
record = set()
for i in range(N):
    if tuple(train[i]) in record:
        pass
    else:
        record.add(tuple(train[i]))
        cnt += 1
# print(train)
# print(record)        
print(cnt)