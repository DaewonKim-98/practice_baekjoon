from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 아씨 너무 많나 디피로는 절대 못 풀 것 같은데 아오진짜
# 다시 천천히 ㄱㄱ
start = 0
end = 0
max_length = 0
length = 0

# 이번엔 그냥 start를 처음부터 돌리면서 딱 2로 나눠떨어지는 짝수만 찾아보자
cnt = 0

for start in range(N):
    # K개까지 홀수가 없으면
    while cnt <= K:
        # end가 N이 되면 끝이므로
        if end == N:
            break
        # 홀수를 찾으면
        if arr[end] % 2 == 1:
            if cnt == K:
                break
            cnt += 1
        # 짝수면
        else:
            length += 1
        end += 1
        
    # print(start, end, length)
    max_length = max(max_length, length)
    
    # start가 홀수를 만나면
    if arr[start] % 2 == 1:
        cnt -= 1
    
    else:
        length -= 1
        
print(max_length)