N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 완전 탐색하면 무조건 시간초과 날듯
# 원소를 인덱스로 하는 0으로된 리스트를 만들어두고 시작점과 끝점을 증가시키면서 끝까지 가게끔
# 원소가 K개 이상 되면 시작점이 움직이고 이하면 끝점이 움직이면서 최댓값 찾기

idx_list = [0] * 200000
start = 0
end = 0
max_length = 0
idx_list[arr[0]] = 1
while end < N - 1:
    # print(start, end)
    # 만약 원소 개수가 K보다 많아지면 start 옮기기
    if idx_list[arr[end]] > K:
        # start를 옮길 것이므로 그 부분 원소 하나 삭제
        idx_list[arr[start]] -= 1
        start += 1
    # 아니면 end 계속 옮기기
    else:
        end += 1
        idx_list[arr[end]] += 1
    # 최대 길이 갱신
    if max_length < end - start:
        max_length = end - start

print(max_length)