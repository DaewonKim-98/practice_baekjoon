N, M = map(int, input().split())
# 리스트에 추가
nlist = []
for i in range(N):
    nlist.append(input())

# 세트로 바꿔준다
nset = set(nlist)

# 리스트에 추가
mlist = []
for j in range(M):
    mlist.append(input())

# mlist에 있는 것이 set에 있는지 찾고 있으면 1추가
cnt = 0
for m in mlist:
    if m in nset:
        cnt += 1

print(cnt)