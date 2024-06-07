N = int(input())
# 걸리는 시간, 선행 작업들
time = [0] * (N + 1)
link = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    time[i] = arr[0]
    if arr[1] != 0:
        link[i] = arr[2:]

# 총 걸리는 시간 구하기
work = [0] * (N + 1)
for i in range(1, N + 1):
    # 선행되는 작업 없으면 그냥 더하기
    if len(link[i]) == 0:
        work[i] = time[i]
    # 선행되는 작업 있으면 앞에 선행한 작업 중에서 가장 큰 값에서 더해주기
    # 제일 오래 걸린 것 뒤에 해야 하니까
    else:
        for j in link[i]:
            work[i] = max(work[j] + time[i], work[i])

print(max(work))