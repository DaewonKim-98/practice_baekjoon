N = int(input())
arr = list(map(int, input().split()))

lst = [0] * N
for i in range(N):
    # 0의 개수를 셀 cnt
    cnt = 0
    j = 0
    # 자신보다 키가 큰 사람이 arr[i] 명이 왼쪽에 있어야 하므로 0을 세서 0이 arr[i] 개가 되면 넣기
    # cnt가 arr[j]보다 작을 때 계속 반복
    while cnt < arr[i]:
        if lst[j] == 0:
            cnt += 1
        j += 1

    while lst[j] != 0:
        j += 1
    lst[j] = str(i + 1)
    

print(' '.join(lst))
