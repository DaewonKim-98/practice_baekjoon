N = int(input())

lst = []
for f in range(0, 1669):
    for t in range(0, 1001):
        if 3 * f + 5 * t == N:
            lst.append(f + t)
            break
if len(lst) > 0:
    print(min(lst))
else:
    print(-1)
