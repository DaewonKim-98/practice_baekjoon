import sys

arr = str(input())

lst = []
for i in arr:
    lst.append(int(i))

# 카운트 정렬 각 자리수는 10 미만이므로
zlist = [0] * 10

# zlist의 인덱스의 값이 리스트에 있는 값이면 1을 추가
for j in range(len(lst)):
    zlist[lst[j]] += 1

# 각 값들을 출력
for k in range(9, -1, -1):
    if zlist[k] != 0:
        for l in range(zlist[k]):
            print(k, end='')