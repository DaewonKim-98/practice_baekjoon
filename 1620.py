N = int(input())
narr = list(map(int, input().split()))
M = int(input())
marr = list(map(int, input().split()))

# narr을 오름차순으로 정렬
narr.sort()

# 이진 탐색으로 존재하면 1, 존재하지 않으면 0 출력
for m in marr:
    # 존재하면 exist = 1
    exist = 0
    start_idx = 0
    end_idx = N - 1
    while start_idx <= end_idx:
        middle_idx = (start_idx + end_idx) // 2
        if narr[middle_idx] == m:
            exist = 1
            break
        elif narr[middle_idx] > m:
            end_idx = middle_idx - 1
        else:
            start_idx = middle_idx + 1
    # 반복해서 나오는 값이 없을 땐 exist = 0 을 출력할 것이다.
    print(exist)