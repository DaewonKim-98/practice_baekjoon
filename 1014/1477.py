N, M, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

# 최소의 휴게소 사이의 거리가 최대가 되려면 휴게소들은 균등하게 지어져야 한다.
# 이분 탐색으로 휴게소의 거리가 최대가 되는 것을 찾기

start = 1
end = L - 1

while start <= end:
    # 휴게소 사이의 거리
    middle = (end + start) // 2

    # 추가되는 휴게소의 개수
    shelter = 0
    for i in range(-1, N):
        # print(shelter)
        if i == -1:
            start_shelter = 0
        else:
            start_shelter = arr[i]
        if i == N - 1:
            last_shelter = L
        else:
            last_shelter = arr[i + 1]
        # 휴게소 사이의 거리만큼 더했을 때 다음 휴게소가 나오기 전까지
        while start_shelter + middle < last_shelter:
            # 추가되는 휴게소의 개수 추가
            shelter += 1
            start_shelter += middle
            
    # 추가되는 휴게소의 개수가 M보다 크다면     
    if M < shelter:
        # 휴게소 사이의 거리를 늘리기
        start = middle + 1
    # 추가되는 휴게소의 개수가 M보다 적거나 같다면 거리를 줄여야 하므로
    else:
        end = middle - 1
        
print(start)