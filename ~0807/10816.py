import sys

N = int(sys.stdin.readline())
narr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
marr = list(map(int, sys.stdin.readline().split()))

# 카운팅 정렬과 비슷하게 수의 크기에맞는 리스트를 만든다.
cnt = [0] * 20000001
# 처음 받은 값들의 인덱스에 1을 추가해 리스트의 인덱스가 몇 개인지 알게 한다.
for i in narr:
    cnt[i] += 1

# 리스트의 인덱스를 출력해 개수를 센다.
for j in marr:
    print(cnt[j], end=' ')