import sys

A, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


# 처음부터 교환 횟수가 작다고 생각하면 바로 -1 출력
if A * (A - 1) / 2 < K:
    print(-1)

else:    
    # 교환 횟수를 change
    change = 0
    for i in range(A, 1, -1):
        for j in range(1, A):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                change += 1
                # 교환 횟수가 K면 답처럼 출력
                if change == K:
                    print(f'{arr[j - 1]} {arr[j]}')
                    break
        if change == K:
            break
                
if change < K:
    print(-1)