N = int(input())
arr = list(map(int, input().split()))

# 앞에 했던 방식대로 하면 시간초과;;
# 이분탐색 비스무리하게 가야하나?
start = 0
end = N - 1
min_value = arr[start] + arr[end]

while start < end:
    # 0 이 되면 끝이므로
    if min_value == 0:
        break
    value = arr[start] + arr[end]
    # 절댓값으로 비교
    if abs(min_value) > abs(value):
        min_value = value
    
    # 합이 0보다 작으면 start 올리기
    if value < 0:
        start += 1
        
    else:
        end -= 1
        
print(min_value)