from collections import deque

N, K = map(int, input().split())

arr = deque(list(range(1, N + 1)))

yose = deque([])

# 요세푸스 순열이 완성될 때까지 돌리기
while len(yose) < N:
    # K번째 전까지 수를 뒤로 보내준다.
    for i in range(K - 1):
        p = arr.popleft()
        arr.append(p)
        
    # K번째를 yose에 넣고 제거
    k = arr.popleft()
    yose.append(str(k))
    
result = ', '.join(yose)
print(f'<{result}>')