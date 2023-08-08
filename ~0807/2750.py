N = int(input())

arr = []
for i in range(N):
    arr += [int(input())]

# 오름차순 정렬 
for j in range(N, 1, -1):
    for k in range(1, j):
        if arr[k - 1] > arr[k]:
            arr[k - 1], arr[k] = arr[k], arr[k - 1]
            
for l in arr:
    print(l)