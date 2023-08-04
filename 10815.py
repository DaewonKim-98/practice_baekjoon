N = int(input())
# 시간을 줄이기 위해 집합으로 받아온다(영웅재종)
nlist = set(map(int, input().split()))
M = int(input())
mlist = list(map(int, input().split()))

# m이 nlist에 있으면 1
for m in mlist:
    if m in nlist:
        print(1, end=' ')
    else:
        print(0, end=' ')