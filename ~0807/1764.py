import sys

N, M = map(int, sys.stdin.readline().split())

narr = []
for i in range(N):
    narr.append(sys.stdin.readline().strip())

marr = []
for j in range(M):
    marr.append(sys.stdin.readline().strip())

# 세트로 바꾸고 교집합
narr = set(narr)
marr = set(marr)
nlc = narr & marr

# 사전순으로 정렬
nlc = list(nlc)
nlc.sort()

print(len(nlc))
for k in nlc:
    print(k)