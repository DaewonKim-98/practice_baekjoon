import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

# 아오시간초과 집합 S를 미리 접두사의 부분집합으로 만든다면?
S = set()
for _ in range(N): 
    word = input().split()[0]
    jupdu = ''
    for alpha in word:
        jupdu += alpha
        S.add(jupdu)

cnt = 0
# 문자열을 돌면서 접두사인지 판단
for _ in range(M):
    check = input().strip()
    if check in S:
        cnt += 1
        
print(cnt)