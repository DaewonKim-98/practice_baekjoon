N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합
narr = [0] * N
narr[0] = arr[0]
for i in range(1, N):
    narr[i] = arr[i] + narr[i - 1]

# 배열을 돌면서 M이 되는 경우 구하기
cnt = 0
i = 0
j = 0
while i < N:
    # j가 N - 1에 도달하면 i만 늘리기
    if j == N - 1:
        if narr[j] - narr[i] + arr[i] == M:
            cnt += 1
            break
        elif narr[j] - narr[i] + arr[i] < M:
            break
        else:
            i += 1
    
    # 도달하지 않을 때에는 j늘리다가 M보다 커지면 i늘리기
    else:
        if narr[j] - narr[i] + arr[i] < M:
            j += 1
        elif narr[j] - narr[i] + arr[i] == M:
            j += 1
            cnt += 1
        else:
            i += 1
            
print(cnt)