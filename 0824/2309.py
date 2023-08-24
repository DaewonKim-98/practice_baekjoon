import sys
input = sys.stdin.readline

arr = [int(input().strip()) for _ in range(9)]

for i in range(8):
    for j in range(i + 1, 9):
        f = arr.pop(i)
        s = arr.pop(j - 1)
        if sum(arr) == 100:
            arr.sort()
            for k in arr:
                print(k)
            break
        else:
            arr.insert(i, f)
            arr.insert(j - 1, s)
    if sum(arr) == 100:
        break