T = int(input())

for case in range(1, T + 1):
    arr = list(map(int, input().split()))

    # 오름차순으로 정렬
    for i in range(10, 0, -1):
        for j in range(1, i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    
    # 뒤에서 3번째가 3밴째 큰 값
    print(arr[-3])