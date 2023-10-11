M, N = map(int, input().split())
arr = list(map(int, input().split()))

# 이분 탐색
start = 1
end = 1000000000

while start <= end:
    # 과자의 크기
    mid = (start + end) // 2
    
    # 몇 명에게 줄 수 있는지
    can_give = 0
    
    # arr을 돌면서 과자의 크기로 몇명에게 줄 수 있는지 찾기
    for i in arr:
        can_give += i // mid
        
    # 줄 수 있는 인원이 M보다 많거나 같으면 과자의 크기를 더 늘리고
    if can_give >= M:
        start = mid + 1
    # 줄 수 있는 인원이 적으면 과자의 크기 줄이기
    else:
        end = mid - 1
        
print(end)