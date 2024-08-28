N, K = map(int, input().split())
arr = list(map(int, input().split()))

i, j = 0, 0
minSet = 1000000
cnt = 0
if arr.count(1) < K:
    print(-1)
    exit()
    
while True:
    if arr[i] == 1:
        break
    i += 1
j = i

while j < N:
    # print(i, j, cnt)
    # 라이언찾으면 라이언 갯수 늘리기
    if arr[j] == 1:
        cnt += 1
    # 라이언 갯수가 K가 되면 다음 라이언까지 i 늘려주기
    if cnt == K:
        minSet = min(j - i + 1, minSet)
        while True:
            i += 1
            if arr[i] == 1:
                break
        j += 1
        cnt -= 1
    else:
        j += 1
print(minSet)