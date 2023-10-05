N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 완전 탐색하면 무조건 시간초과 날듯
# 원소를 인덱스로 하는 0으로된 리스트를 만들어두고 시작점과 끝점을 증가시키면서 끝까지 가게끔
# 원소가 K개 이상 되면 시작점이 움직이고 이하면 끝점이 움직이면서 최댓값 찾기

idx_list = [0] * 100001
start = 0
end = 0
max_length = 0
while end < N:
    # 원소의 개수가 K개 이하이면 end를 늘리고 원소 추가
    while end < N and idx_list[arr[end - 1]] <= K:
        # print(end)
        idx_list[arr[end]] += 1
        end += 1

    # 원소의 개수가 K개가 넘어가면 end 다시 이전으로
    end -= 1
    # end가 끝에 도달했으면
    if end == N - 1 and idx_list[arr[end]] <= K:
        end += 1
        max_length = max(max_length, end - start)
        break
    
    # 수열 길이 갱신
    max_length = max(max_length, end - start)
    
    # 원소의 개수가 K개 이하가 될 때까지 start +1
    while start <= end and idx_list[arr[end]] > K:
        idx_list[arr[start]] -= 1
        start += 1
    
    end += 1
    
    
print(max_length)