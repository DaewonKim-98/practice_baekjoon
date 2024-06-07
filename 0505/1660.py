def dfs(i, num, cnt):
    global minCnt
    if num == N:
        minCnt = min(minCnt, cnt)
        return
    if num > N:
        return
    if cnt >= minCnt:
        return
    for j in range(i, 120):
        if arr[j] + num <= N:
            dfs(j, arr[j] + num, cnt + 1)

N = int(input())

# 삼각형의 크기
arr = [i for i in range(121)]
for i in range(2, 121):
    arr[i] += arr[i - 1]

    
# 사면체의 크기
for i in range(2, 121):
    arr[i] += arr[i - 1]

# 사면체 크기 큰것부터 해서 만들 수 있는거 찾기
arr.sort(reverse=True)
minCnt = 300000
for i in range(120):
    if N >= arr[i]:
        # print(arr[i], i)
        dfs(i, arr[i], 1)
        
print(minCnt)