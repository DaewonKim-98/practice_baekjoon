def dfs(arr, K, i):
    lst[i].append(arr[2 ** (K - 1) - 1])
    if K > 1:
        dfs(arr[:2 ** (K - 1) - 1], K - 1, i + 1)
        dfs(arr[2 ** (K - 1):], K - 1, i + 1)
    

K = int(input())
arr = list(map(int, input().split()))

# 완전 이진 트리니까 가운데가 항상 꼭대기
lst = [[] for _ in range(K)]
dfs(arr, K, 0)
for i in lst:
    for j in i:
        print(j, end=' ')
    print()