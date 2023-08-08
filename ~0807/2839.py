N = int(input())

lst = []

# 더 적은 봉지는 5kg부터 넣어야 하니까 이중 for문에서 안에 for문에 해당하는
# 변수에 5를 곱하고 3은 밖에 해당하는 거에 곱해서 N이 맞는 걸 찾는다.
# 리스트에 넣어서 아니면 -1출력
for f in range(0, 1669):
    for t in range(0, 1001):
        if 3 * f + 5 * t == N:
            lst.append(f + t)
            break
if len(lst) > 0:
    print(lst[0])
else:
    print(-1)
