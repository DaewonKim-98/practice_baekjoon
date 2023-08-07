import sys

N = int(sys.stdin.readline())
narr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
marr = list(map(int, sys.stdin.readline().split()))

cnt = [0] * 20000001
for i in narr:
    cnt[i] += 1

for j in marr:
    print(cnt[j], end=' ')